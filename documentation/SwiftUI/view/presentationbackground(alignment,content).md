# presentationBackground(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the presentation background of the enclosing sheet to a custom view.

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
func presentationBackground<V>(alignment: Alignment = .center, @ContentBuilder content: () -> V) -> some View where V : View
```

## Discussion

The following example uses a yellow view as the sheet background:

```swift
struct ContentView: View {
    @State private var showSettings = false

    var body: some View {
        Button("View Settings") {
            showSettings = true
        }
        .sheet(isPresented: $showSettings) {
            SettingsView()
                .presentationBackground {
                    Color.yellow
                }
        }
    }
}
```

The `presentationBackground(alignment:content:)` modifier differs from the [`background(alignment:content:)`](./background%28alignment,content%29.md) modifier in several key ways. A presentation background:

- Automatically fills the entire presentation.
- Allows views behind the presentation to show through translucent areas of the `content` on supported platforms.

> **Note**: Sheet presentations on macOS do not support translucency or transparency — the background is always opaque.

## Parameters

- `alignment`: The alignment that the modifier uses to position the implicit [`ZStack`](../zstack.md) that groups the background views. The default is [`center`](../alignment/center.md).
- `content`: The view to use as the background of the presentation.

## See Also

### Styling a sheet and its background
- [func presentationCornerRadius(CGFloat?) -> some View](./presentationcornerradius%28_%29.md)
  Requests that the presentation have a specific corner radius.
- [func presentationBackground<S>(S) -> some View](./presentationbackground%28_%29.md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./presentationbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presentation.
- [struct PresentationBackgroundInteraction](../presentationbackgroundinteraction.md)
  The kinds of interaction available to views behind a presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/presentationbackground(alignment:content:))*