# searchSuggestions(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Configures how to display search suggestions within this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func searchSuggestions(_ visibility: Visibility, for placements: SearchSuggestionsPlacement.Set) -> some View
```

#### Discussion

SwiftUI presents search suggestions differently depending on several factors, like the platform, the position of the search field, and the size class. Use this modifier when you want to only display suggestions in certain ways under certain conditions. For example, you might choose to display suggestions in a menu when possible, but directly filter your data source otherwise.

```swift
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

## See Also

- [Suggesting search terms](suggesting-search-terms.md)
  Provide suggestions to people searching for content in your app.
- [func searchSuggestions<S>(() -> S) -> some View](view/searchsuggestions(_:).md)
  Configures the search suggestions for this view.
- [func searchCompletion(_:)](view/searchcompletion(_:).md)
  Associates a fully formed string with the value of this view when used as a search suggestion.
- [func searchable(text:tokens:suggestedTokens:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions.
- [struct SearchSuggestionsPlacement](searchsuggestionsplacement.md)
  The ways that SwiftUI displays search suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchsuggestions(_:for:))*