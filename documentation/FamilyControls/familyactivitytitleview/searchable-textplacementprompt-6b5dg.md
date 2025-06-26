# searchable(text:placement:prompt:)

**Framework**: FamilyControls  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: A   view representing the prompt of the search field   which provides users with guidance on what to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/searchable(text:placement:prompt:)-6b5dg)*