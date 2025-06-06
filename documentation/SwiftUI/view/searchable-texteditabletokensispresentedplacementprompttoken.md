# searchable(text:editableTokens:isPresented:placement:prompt:token:)

**Framework**: SwiftUI  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ViewBuilder token: @escaping (Binding<C.Element>) -> some View) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `editableTokens`: A collection of tokens to display and edit in the   search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: The key for the localized prompt of the search field   which provides users with guidance on what to search for.
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
- [func searchable(text:tokens:suggestedTokens:isPresented:placement:prompt:token:)](view/searchable(text:tokens:suggestedtokens:ispresented:placement:prompt:token:).md)
  Marks this view as searchable with text, tokens, and suggestions, as well as programmatic presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:editabletokens:ispresented:placement:prompt:token:))*