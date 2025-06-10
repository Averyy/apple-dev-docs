# searchable(text:editableTokens:isPresented:placement:prompt:token:)

**Framework**: App Intents  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ViewBuilder token: @escaping (Binding<C.Element>) -> some View) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `editableTokens`: A collection of tokens to display and edit in the   search field.
- `isPresenting`: A   which controls the presented state   of search.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A   view representing the prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/searchable(text:editabletokens:ispresented:placement:prompt:token:)-6n2un)*