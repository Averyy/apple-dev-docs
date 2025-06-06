# completerDidUpdateResults(_:)

**Framework**: MapKit  
**Kind**: method

Tells the method when the specified search completer updates its array of search completions.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
optional func completerDidUpdateResults(_ completer: MKLocalSearchCompleter)
```

#### Discussion

After receiving results from a query, the search completer updates its [`results`](mklocalsearchcompleter/results.md) property with the new [`MKLocalSearchCompletion`](mklocalsearchcompletion.md) objects and calls this method. Use this method to update your app’s interface based on the new search results. For example, you might update a table that you use to display search results to the user.

## Parameters

- `completer`: The search completer object with updated results.

## See Also

- [func completer(MKLocalSearchCompleter, didFailWithError: any Error)](mklocalsearchcompleterdelegate/completer(_:didfailwitherror:).md)
  Tells the method when the specified search completer is unable to generate a list of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/completerdidupdateresults(_:))*