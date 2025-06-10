# searchSuggestions(_:for:)

**Framework**: PermissionKit  
**Kind**: method

Configures how to display search suggestions within this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
nonisolated
func searchSuggestions(_ visibility: Visibility, for placements: SearchSuggestionsPlacement.Set) -> some View
```

#### Discussion

SwiftUI presents search suggestions differently depending on several factors, like the platform, the position of the search field, and the size class. Use this modifier when you want to only display suggestions in certain ways under certain conditions. For example, you might choose to display suggestions in a menu when possible, but directly filter your data source otherwise.

```None
enum FruitSuggestion: String, Identifiable {
    case apple, banana, orange
    var id: Self { self }
}

@State private var text = ""
@State private var suggestions: [FruitSuggestion] = []

var body: some View {
    MainContent()
        .searchable(text: $text) {
            ForEach(suggestions) { suggestion
                Text(suggestion.rawValue)
                    .searchCompletion(suggestion.rawValue)
            }
            .searchSuggestions(.hidden, for: .content)
        }
}
```

## Parameters

- `visibility`: The visibility of the search suggestions   for the specified locations.
- `placements`: The set of locations in which to set the visibility of   search suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/searchsuggestions(_:for:))*