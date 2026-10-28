# windowResizeAnchor(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the window anchor point used when the size of the view changes such that the window must resize.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
func windowResizeAnchor(_ anchor: UnitPoint?) -> some View
```

## Return Value

A view whose scene resizes on `anchor`.

## Discussion

In SwiftUI life cycle apps, this modifier can be used to control how a window anchors when animating: drive window animations by changing the size of a view in a way that causes the window size to change. Note that if the window size is decreasing and an animation is desired, it is often necessary to (temporarily, if desired) set the [`windowResizability(_:)`](../scene/windowresizability%28_%29.md) to [`contentSize`](../windowresizability/contentsize.md).

```swift
struct Scratchpad: App {
    var body: some Scene {
        WindowGroup {
            HeightResizingExample()
        }
        .windowResizability(.contentSize)
    }
}

struct HeightResizingExample: View {
    @State private var height: CGFloat = 300

    var body: some View {
        ZStack(alignment: .topLeading) {
            Color.red
                .overlay {
                    Text("Tap to toggle")
                        .foregroundStyle(.white)
                }
        }
        .onTapGesture {
            withAnimation(.easeInOut) {
                height = height == 300 ? 700 : 300
            }
        }
        .frame(width: 250, height: height)
        .windowResizeAnchor(.top)
    }
}
```

The default anchor varies by scene type and is used when `anchor` is nil. Generally, it resolves to the `.topLeading` corner.

> **Note**: Animated window resizes are only supported in SwiftUI app-lifecycle apps. However, the anchor point is respected in all cases.

> **Note**: When animating windows on macOS, it can be helpful to explicitly specify `.topLeading` to avoid pixel cracking between the hosting view and the hosting window.

## Parameters

- `anchor`: The window point fixed under programmatic size changes caused by the content size of the window changing. Defaults to a system defined value when `nil`.

## See Also

### Window behaviors
- [func windowDismissBehavior(WindowInteractionBehavior) -> some View](./windowdismissbehavior%28_%29.md)
  Configures the dismiss functionality for the window enclosing `self`.
- [func windowFullScreenBehavior(WindowInteractionBehavior) -> some View](./windowfullscreenbehavior%28_%29.md)
  Configures the full screen functionality for the window enclosing `self`.
- [func windowToolbarFullScreenVisibility(WindowToolbarFullScreenVisibility) -> some View](./windowtoolbarfullscreenvisibility%28_%29.md)
  Configures the visibility of the window toolbar when the window enters full screen mode.
- [func windowMinimizeBehavior(WindowInteractionBehavior) -> some View](./windowminimizebehavior%28_%29.md)
  Configures the minimize functionality for the window enclosing `self`.
- [func windowResizeBehavior(WindowInteractionBehavior) -> some View](./windowresizebehavior%28_%29.md)
  Configures the resize functionality for the window enclosing `self`.
- [func preferredWindowClippingMargins(_:_:)](./preferredwindowclippingmargins%28_,_%29.md)
  Requests additional margins for drawing beyond the bounds of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/windowresizeanchor(_:))*