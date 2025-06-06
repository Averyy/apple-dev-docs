# searchable(text:placement:prompt:suggestions:)

**Framework**: RealityKit  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil, @ViewBuilder suggestions: () -> S) -> some View where S : View
```

#### Discussion

For more information about using searchable modifiers, see doc:Adding-a-search-interface-to-your-app.

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: Where the search field should attempt to be   placed based on the containing view hierarchy.
- `prompt`: A   view representing the prompt of the search field   which provides users with guidance on what to search for.
- `suggestions`: A view builder that produces content that   populates a list of suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/searchable(text:placement:prompt:suggestions:)-38v6q)*