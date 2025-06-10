# searchable(text:tokens:isPresented:placement:prompt:token:)

**Framework**: FinanceKitUI  
**Kind**: method

Marks this view as searchable with text and tokens, as well as programmatic presentation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func searchable<C, T>(text: Binding<String>, tokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource, @ViewBuilder token: @escaping (C.Element) -> T) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, T : View, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app. For information about presenting a search field programmatically, see doc:Managing-search-interface-activation.

## Parameters

- `text`: The text to display and edit in the search field.
- `tokens`: A collection of tokens to display and edit in the   search field.
- `isPresenting`: A   that controls the presented state   of search.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: Text resource for the localized prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/searchable(text:tokens:ispresented:placement:prompt:token:)-4d8c6)*