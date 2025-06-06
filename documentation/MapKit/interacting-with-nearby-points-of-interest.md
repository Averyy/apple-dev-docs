# Interacting with nearby points of interest

**Framework**: MapKit

Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- visionOS 2.2+
- Xcode 16.2+

#### Overview

This sample code project demonstrates how to programmatically search for map-based addresses and points of interest using a natural language string, and how to get more information about points of interest that a person selects on the map. The search results center around the locations visible in the map view.

##### Request Search Completions

[`MKLocalSearchCompleter`](mklocalsearchcompleter.md) retrieves autocomplete suggestions for a partial search query within a map region. A person can type “cof”, and a search completion suggests “coffee” as the query string. As the person types a query into a search bar, the sample app updates the query. In SwiftUI, the sample creates the search field using the [`searchable(text:placement:prompt:)`](https://developer.apple.com/documentation/SwiftUI/View/searchable(text:placement:prompt:)) modifier.

```swift
.searchable(text: $searchQuery, placement: .navigationBarDrawer(displayMode: .always), prompt: searchPrompt)
```

As someone types a query into a search bar, the sample app updates the [`queryFragment`](mklocalsearchcompleter/queryfragment.md) for the search completion through the `searchQuery` binding.

```swift
/// Ask for completion suggestions based on the query text.
func provideCompletionSuggestions(for query: String) {
    /**
     Configure the search to return completion results based only on the options in the app. For example,
     someone can configure the app to exclude specific point-of-interest categories, or to only return results for addresses.
     */
    searchCompleter?.resultTypes = mapConfiguration.resultType.completionResultType
    searchCompleter?.regionPriority = mapConfiguration.regionPriority.localSearchRegionPriority
    if mapConfiguration.resultType == .pointsOfInterest {
        searchCompleter?.pointOfInterestFilter = mapConfiguration.pointOfInterestOptions.filter
    } else if mapConfiguration.resultType == .addresses {
        searchCompleter?.addressFilter = mapConfiguration.addressOptions.filter
    }
    
    searchCompleter?.region = mapConfiguration.region
    searchCompleter?.queryFragment = query
}
```

##### Receive Completion Results

Completion results represent fully formed query strings based on the query fragment someone types. The sample app uses completion results to populate UI elements to quickly fill in a search query. The app receives the latest completion results as an array of [`MKLocalSearchCompletion`](mklocalsearchcompletion.md) objects by adopting the [`MKLocalSearchCompleterDelegate`](mklocalsearchcompleterdelegate.md) protocol.

```swift
nonisolated func completerDidUpdateResults(_ completer: MKLocalSearchCompleter) {
    Task { @MainActor in
        /**
         As a person types, new completion suggestions continuously return to this method. Update the property storing the current
         results, so that the app UI can observe the change and display the updated suggestions.
         */
        let suggestedCompletions = completer.results
        resultStreamContinuation?.yield(suggestedCompletions)
    }
}
```

The app uses an [`AsyncStream`](https://developer.apple.com/documentation/Swift/AsyncStream) to deliver the completion results to the UI, which the `SidebarView`  stores in its `searchCompletions` property. The app displays the search suggestions with the [`searchSuggestions(_:)`](https://developer.apple.com/documentation/SwiftUI/View/searchSuggestions(_:)) modifier, which takes a binding to the `searchCompletions` property.

```swift
.searchSuggestions {
    // Treat each `MKMapItem` object as unique, using `\.self` for the identity. The `identifier` property of `MKMapItem`
    // is an optional value, and the meaning of the identifier for `MKMapItem` doesn't have the same semantics as
    // the `Identifable` protocol that `ForEach` requires.
    ForEach($searchCompletions, id: \.self) { completion in
        SearchCompletionItemView(completion: completion.wrappedValue)
        .onTapGesture {
            convertSearchCompletionToSearchResults(completion.wrappedValue)
        }
    }
}
```

##### Highlight the Relationship of a Query Fragment to the Suggestion

Within the UI elements that represent each query result, the sample code uses the [`titleHighlightRanges`](mklocalsearchcompletion/titlehighlightranges.md) on an `MKLocalSearchCompletion` to show how the query someone enters relates to the suggested result. For example, the following code applies a highlight with [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString):

```swift
private func createHighlightedString(text: String, rangeValues: [NSValue]) -> NSAttributedString {
    let attributes = [NSAttributedString.Key.backgroundColor: UIColor(named: "suggestionHighlight")!]
    let highlightedString = NSMutableAttributedString(string: text)

    // Each `NSValue` wraps an `NSRange` that functions as a style attribute's range with `NSAttributedString`.
    let ranges = rangeValues.map { $0.rangeValue }
    for range in ranges {
        highlightedString.addAttributes(attributes, range: range)
    }

    return highlightedString
}
```

##### Search for Map Items

An `MKLocalSearch.Request` takes either an `MKLocalSearchCompletion` or a natural language query string, and returns an array of [`MKMapItem`](mkmapitem.md) objects. Each `MKMapItem` represents a geographic location, like a specific address, that matches the search query. The sample code asynchronously retrieves the array of `MKMapItem` objects by calling [`start(completionHandler:)`](mklocalsearch/start(completionhandler:).md) on [`MKLocalSearch`](mklocalsearch.md).

```swift
let search = MKLocalSearch(request: request)
currentSearch = search
defer {
    // After the search completes, the reference is no longer needed.
    currentSearch = nil
}

var results: [MKMapItem]

do {
    let response = try await search.start()
    results = response.mapItems
} catch let error {
    searchLogging.error("Search error: \(error.localizedDescription)")
    results = []
}
```

##### Allow Someone to Select Points of Interest on the Map

If a person is exploring the map, they can get information for a point of interest by tapping it. To provide these interactions, the sample code enables selectable map features as follows:

```swift
// Use the standard map style, with an option to display specific point-of-interest categories.
.mapStyle(.standard(pointsOfInterest: mapModel.searchConfiguration.pointOfInterestOptions.categories))

// Only allow selection for points of interest, and disable selection of other labels, like city names.
.mapFeatureSelectionDisabled { feature in
    feature.kind != MapFeature.FeatureKind.pointOfInterest
}

/*
 The selection accessory allows people to tap on map features and get more detailed information, which displays
 as either a sheet or a callout according to the `style` parameter. Along with the `selection` binding, this determines
 which feature to display additional information for.
 
 This modifier differs from the `mapItemDetailSelectionAccessory(:_) modifier, which enables the same selection
 behaviors on annotations that the app adds to `Map` for search results.
 */
.mapFeatureSelectionAccessory(.automatic)
```

When someone taps a point of interest, the system presents the map item’s details, including information like a phone number, business hours, and buttons to start navigation to the location using Apple Maps. The system presents the information using the style that the `mapFeatureSelectionAccessory(_:)` modifier configures. The sample app uses the [`automatic`](mapitemdetailselectionaccessorystyle/automatic.md) style, but the [`MapItemDetailSelectionAccessoryStyle`](mapitemdetailselectionaccessorystyle.md) structure offers several other options.

##### Persist and Retrieve Map Items

If someone is exploring the map, they may want the app to store places they looked at so that they can come back to them later, including across app launches. `MKMapItem` has an [`identifier`](mkmapitem/identifier-swift.property.md) property, which the app stores in its `VisitedPlace` model using `SwiftData`.

```swift
guard let identifier = mapItem.identifier else { return }
let visit = VisitedPlace(id: identifier.rawValue)
```

When the app launches, it retrieves the history of visited locations from SwiftData. To get the `MKMapItem` from the previously stored identifier, the app creates an [`MKMapItemRequest`](mkmapitemrequest.md) with the stored identifier and calls [`getMapItem(completionHandler:)`](mkmapitemrequest/getmapitem(completionhandler:).md).

```swift
@MainActor
func convertToMapItem() async -> MKMapItem? {
    guard let identifier = MKMapItem.Identifier(rawValue: id) else { return nil }
    let request = MKMapItemRequest(mapItemIdentifier: identifier)
    var mapItem: MKMapItem? = nil
    do {
        mapItem = try await request.mapItem
    } catch let error {
        let logger = Logger(subsystem: Bundle.main.bundleIdentifier!, category: "Map Item Requests")
        logger.error("Getting map item from identifier failed. Error: \(error.localizedDescription)")
    }
    return mapItem
}
```

## See Also

- [enum MKLocalSearchRegionPriority](mklocalsearchregionpriority.md)
  A value that indicates the importance of the configured region.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.
- [class MKLocalSearch](mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class MKAddressFilter](mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.
- [class MKLocalPointsOfInterestRequest](mklocalpointsofinterestrequest.md)
  A structured request to use when searching for points of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/interacting-with-nearby-points-of-interest)*