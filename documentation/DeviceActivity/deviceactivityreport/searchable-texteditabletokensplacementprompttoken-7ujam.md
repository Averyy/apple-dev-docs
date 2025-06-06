# searchable(text:editableTokens:placement:prompt:token:)

**Framework**: DeviceActivity  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func searchable<C>(text: Binding<String>, editableTokens: Binding<C>, placement: SearchFieldPlacement = .automatic, prompt: some StringProtocol, @ViewBuilder token: @escaping (Binding<C.Element>) -> some View) -> some View where C : RandomAccessCollection, C : RangeReplaceableCollection, C.Element : Identifiable
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `editableTokens`: A collection of tokens to display and edit in the   search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A string representing the prompt of the search field   which provides users with guidance on what to search for.
- `token`: A view builder that creates a view given an element in   tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/searchable(text:editabletokens:placement:prompt:token:)-7ujam)*