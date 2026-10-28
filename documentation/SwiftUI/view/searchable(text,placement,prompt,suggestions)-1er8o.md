# searchable(text:placement:prompt:suggestions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+ - Deprecated in 27.2
- iPadOS 15.0+ - Deprecated in 27.2
- Mac Catalyst 15.0+ - Deprecated in 27.2
- macOS 12.0+ - Deprecated in 27.2
- tvOS 15.0+ - Deprecated in 27.2
- visionOS 1.0+
- watchOS 8.0+ - Deprecated in 27.2

> **Deprecated**: Use the searchable modifier with the searchSuggestions modifier

## Declaration

```swift
nonisolated
func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: S, @ContentBuilder suggestions: () -> V) -> some View where V : View, S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ContentBuilder suggestions: () -> S) -> some View where S : View
```

```swift
nonisolated
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ContentBuilder suggestions: () -> S) -> some View where S : View
```

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: Where the search field should attempt to be placed based on the containing view hierarchy.
- `prompt`: A string representing the prompt of the search field which provides users with guidance on what to search for.
- `suggestions`: A content builder that produces content that populates a list of suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:suggestions:)-1er8o)*