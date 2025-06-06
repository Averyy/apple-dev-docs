# searchable(text:placement:prompt:)

**Framework**: FamilyControls  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey) -> some View
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: The preferred placement of the search field within the   containing view hierarchy.
- `prompt`: The key for the localized prompt of the search field   which provides users with guidance on what to search for.

## See Also

- [func searchable(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?) -> some View](familyactivitypicker/searchable(text:placement:prompt:)-634x8.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S) -> some View](familyactivitypicker/searchable(text:placement:prompt:)-dn5c.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: Text?, suggestions: () -> S) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-1hlnk.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: LocalizedStringKey, suggestions: () -> S) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-5gxr9.md)
  Marks this view as searchable, which configures the display of a search field.
- [func searchable<V, S>(text: Binding<String>, placement: SearchFieldPlacement, prompt: S, suggestions: () -> V) -> some View](familyactivitypicker/searchable(text:placement:prompt:suggestions:)-g7yw.md)
  Marks this view as searchable, which configures the display of a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/searchable(text:placement:prompt:)-4oday)*