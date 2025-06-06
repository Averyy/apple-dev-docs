# graphicsPort

**Framework**: AppKit  
**Kind**: property

The low-level, platform-specific graphics context represented by the graphic port.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var graphicsPort: UnsafeMutableRawPointer { get }
```

#### Discussion

In macOS, this is the Core Graphics context, a [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) object (opaque type).

## See Also

- [class var current: NSGraphicsContext?](nsgraphicscontext/current.md)
  Returns the current graphics context of the current thread.
- [var cgContext: CGContext](nsgraphicscontext/cgcontext.md)
  The Core Graphics context, which is a low-level, platform-specific graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/graphicsport)*