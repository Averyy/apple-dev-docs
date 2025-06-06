# searchable(text:placement:prompt:suggestions:)

**Framework**: SwiftUI  
**Kind**: method

Marks this view as searchable, which configures the display of a search field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey, @ViewBuilder suggestions: () -> S) -> some View where S : View
```

#### Discussion

For more information about using searchable modifiers, see [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: Where the search field should attempt to be   placed based on the containing view hierarchy.
- `prompt`: A key for the localized prompt of the search field   which provides users with guidance on what to search for.
- `suggestions`: A view builder that produces content that   populates a list of suggestions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:suggestions:))*