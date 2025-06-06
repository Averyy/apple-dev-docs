# presentationBackground(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the presentation background of the enclosing sheet using a shape style.

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
func presentationBackground<S>(_ style: S) -> some View where S : ShapeStyle
```

#### Discussion

The following example uses the [`thick`](material/thick.md) material as the sheet background:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationBackground(.thickMaterial)
        }
    }
}
```

The `presentationBackground(_:)` modifier differs from the [`background(_:ignoresSafeAreaEdges:)`](view/background(_:ignoressafeareaedges:).md) modifier in several key ways. A presentation background:

- Automatically fills the entire presentation.
- Allows views behind the presentation to show through translucent styles.

## Parameters

- `style`: The shape style to use as the presentation   background.

## See Also

- [func presentationCornerRadius(CGFloat?) -> some View](view/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](view/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [struct PresentationBackgroundInteraction](presentationbackgroundinteraction.md)
  The kinds of interaction available to views behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationbackground(_:))*