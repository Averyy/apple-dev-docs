# onInteractiveResizeChange(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when the enclosing window is being interactively resized.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func onInteractiveResizeChange(_ action: @escaping (Bool) -> Void) -> some View
```

#### Discussion

Use this modifier to adjust how your view behaves when a window is in the process of being resized by the user. The action provided to this modifier will be called when the resize action begins and ends.

For example, you can adjust the frame rate of a custom Metal renderer during interactive resize:

```swift
struct RootView: View {
    var renderer: MetalRenderer
    var body: some View {
        MetalRepresentable(renderer: renderer)
           .onInteractiveResizeChange { isResizing in
               // Let the renderer know the window is being actively
               // resized, so that it can adjust frame rate,
               // pause animations, etc.
               renderer.handleWindowResize(isResizing: isResizing)
           }
    }
}
```

## Parameters

- `action`: A closure to run when the state of the window’s   interactive resize changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oninteractiveresizechange(_:))*