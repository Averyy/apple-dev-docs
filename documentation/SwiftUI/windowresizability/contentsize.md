# contentSize

**Framework**: SwiftUI  
**Kind**: property

A window resizability that’s derived from the window’s content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var contentSize: WindowResizability { get set }
```

#### Discussion

Windows that use this resizability have:

- A minimum size that matches the minimum size of the window’s content.
- A maximum size that matches the maximum size of the window’s content.

## See Also

- [static var automatic: WindowResizability](windowresizability/automatic.md)
  The automatic window resizability.
- [static var contentMinSize: WindowResizability](windowresizability/contentminsize.md)
  A window resizability that’s partially derived from the window’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowresizability/contentsize)*