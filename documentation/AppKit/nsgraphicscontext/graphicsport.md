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

In macOS, this is the Core Graphics context, a [`CGContext`](https://developer.apple.com/documentation/coregraphics/cgcontext) object (opaque type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/graphicsport)*