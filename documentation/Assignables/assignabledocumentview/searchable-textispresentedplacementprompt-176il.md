# searchable(text:isPresented:placement:prompt:)

**Framework**: Assignables  
**Kind**: method

Marks this view as searchable with programmatic presentation of the search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func searchable(text: Binding<String>, isPresented: Binding<Bool>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app. For information about presenting a search field programmatically, see doc:Managing-search-interface-activation.

## Parameters

- `text`: The text to display and edit in the search field.
- `isPresenting`: A   that controls the presented state   of search.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A   view representing the prompt of the search field   which provides users with guidance on what to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/searchable(text:ispresented:placement:prompt:)-176il)*