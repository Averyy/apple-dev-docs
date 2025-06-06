# searchable(text:tokens:placement:prompt:token:)

**Framework**: SwiftUI  
**Kind**: method

Marks this view as searchable with text and tokens.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: S, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
```

## Mentions

- [Performing a search operation](performing-a-search-operation.md)

#### Discussion

For more information about using searchable modifiers, see [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the   search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A string representing the prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.

## See Also

- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)
  Present an interface that people can use to search for content in your app.
- [Performing a search operation](performing-a-search-operation.md)
  Update search results based on search text and optional tokens that you store.
- [func searchable(text:placement:prompt:)](view/searchable(text:placement:prompt:).md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable(text:editableTokens:placement:prompt:token:)](view/searchable(text:editabletokens:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.
- [struct SearchFieldPlacement](searchfieldplacement.md)
  The placement of a search field in a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:placement:prompt:token:))*