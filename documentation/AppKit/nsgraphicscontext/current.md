# current

**Framework**: AppKit  
**Kind**: property

Returns the current graphics context of the current thread.

**Availability**:
- macOS ?+

## Declaration

```swift
class var current: NSGraphicsContext? { get set }
```

#### Return Value

The current graphics context of the current thread.

#### Discussion

Returns an instance of a concrete subclass of [`NSGraphicsContext`](nsgraphicscontext.md).

## See Also

- [var cgContext: CGContext](nsgraphicscontext/cgcontext.md)
  The Core Graphics context, which is a low-level, platform-specific graphics context.
- [var graphicsPort: UnsafeMutableRawPointer](nsgraphicscontext/graphicsport.md)
  The low-level, platform-specific graphics context represented by the graphic port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/current)*