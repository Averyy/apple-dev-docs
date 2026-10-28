# searchable(text:placement:prompt:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func searchable<S>(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: S) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringResource) -> some View
```

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: LocalizedStringKey) -> some View
```

```swift
nonisolated
func searchable(text: Binding<String>, placement: SearchFieldPlacement = .automatic, prompt: Text? = nil) -> some View
```

## Discussion

For more information about using searchable modifiers, see [Adding a search interface to your app](../adding-a-search-interface-to-your-app.md).

## Parameters

- `text`: The text to display and edit in the search field.
- `placement`: The preferred placement of the search field within the containing view hierarchy.
- `prompt`: A string representing the prompt of the search field which provides users with guidance on what to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)-co5e)*