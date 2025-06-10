# windowResizeAnchor(_:)

**Framework**: MusicKit  
**Kind**: method

Sets the window anchor point used when the size of the view changes such that the window must resize.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func windowResizeAnchor(_ anchor: UnitPoint?) -> some View
```

#### Return Value

A view whose scene resizes on `anchor`.

#### Discussion

In SwiftUI life cycle apps, this modifier can be used to control how a window anchors when animating: drive window animations by changing the size of a view in a way that causes the window size to change. Note that if the window size is decreasing and an animation is desired, it is often necessary to (temporarily, if desired) set the `Scene/windowResizability(_:)` to `WindowResizability/contentSize`.

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

The default anchor varies by scene type and is used when `anchor` is nil. Generally, it defaults to `.topLeading`.

> **Note**: Animated window resizes are only supported in SwiftUI app-lifecycle apps. However, the anchor point is respected in all cases.

## Parameters

- `anchor`: The window point fixed under programmtic size   changes caused by the content size of the window changing.   Defaults to a system defined value when  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/windowresizeanchor(_:))*