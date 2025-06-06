# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic window resizability.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var automatic: WindowResizability { get set }
```

#### Discussion

When you use automatic resizability, SwiftUI applies a resizing strategy that’s appropriate for the scene type:

- Windows from [`WindowGroup`](windowgroup.md), [`Window`](window.md), and [`DocumentGroup`](documentgroup.md) scene declarations use the [`contentMinSize`](windowresizability/contentminsize.md) strategy.
- A window from a [`Settings`](settings.md) scene declaration uses the [`contentSize`](windowresizability/contentsize.md) strategy.
- Windows on visionOS with a window style of [`volumetric`](windowstyle/volumetric.md) use the [`contentSize`](windowresizability/contentsize.md) strategy.

Automatic resizability is the default if you don’t specify another value using the [`windowResizability(_:)`](scene/windowresizability(_:).md) scene modifier.

## See Also

- [static var contentMinSize: WindowResizability](windowresizability/contentminsize.md)
  A window resizability that’s partially derived from the window’s content.
- [static var contentSize: WindowResizability](windowresizability/contentsize.md)
  A window resizability that’s derived from the window’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowresizability/automatic)*