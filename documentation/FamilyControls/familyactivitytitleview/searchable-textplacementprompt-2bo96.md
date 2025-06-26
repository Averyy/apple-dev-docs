# searchable(text:placement:prompt:)

**Framework**: FamilyControls  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource) -> some View
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: Text resource for the localized prompt of the search field   which provides users with guidance on what to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/searchable(text:placement:prompt:)-2bo96)*