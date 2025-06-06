# presentationCornerRadius(_:)

**Framework**: SwiftUI  
**Kind**: method

Requests that the presentation have a specific corner radius.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
nonisolated
func presentationCornerRadius(_ cornerRadius: CGFloat?) -> some View
```

#### Discussion

Use this modifier to change the corner radius of a presentation.

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationDetents([.medium, .large])
                .presentationCornerRadius(21)
        }
    }
}
```

## Parameters

- `cornerRadius`: The corner radius, or   to use the system   default.

## See Also

- [func presentationBackground<S>(S) -> some View](view/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](view/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [struct PresentationBackgroundInteraction](presentationbackgroundinteraction.md)
  The kinds of interaction available to views behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationcornerradius(_:))*