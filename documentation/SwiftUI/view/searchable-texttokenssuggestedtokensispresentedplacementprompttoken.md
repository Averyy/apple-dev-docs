# searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)

**Framework**: SwiftUI  
**Kind**: method

Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable<C, T, S>(text: Binding<String>, tokens: Binding<C>, suggestedTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: S, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : MutableCollection, C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, S : StringProtocol, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md). For information about presenting a search field programmatically, see [`Managing search interface activation`](managing-search-interface-activation.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the   search field.
- `suggestedTokens`: A collection of tokens to display as suggestions.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A string representing the prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.

## See Also

- [Managing search interface activation](managing-search-interface-activation.md)
  Programmatically detect and dismiss a search field.
- [var isSearching: Bool](environmentvalues/issearching.md)
  A Boolean value that indicates when the user is searching.
- [var dismissSearch: DismissSearchAction](environmentvalues/dismisssearch.md)
  An action that ends the current search interaction.
- [struct DismissSearchAction](dismisssearchaction.md)
  An action that can end a search interaction.
- [func searchable(text:isPresented:placement:prompt:)](view/searchable(text:ispresented:placement:prompt:).md)
  Marks this view as searchable with programmatic presentation of the search field.
- [func searchable(text:tokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text and tokens, as well as programmatic presentation.
- [func searchable(text:editableTokens:isPresented:placement:prompt:token:)](view/searchable(text:editabletokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable, which configures the display of a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:))*