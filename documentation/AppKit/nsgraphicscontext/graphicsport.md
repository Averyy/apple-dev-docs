# graphicsPort

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The low-level, platform-specific graphics context represented by the graphic port.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`cgContext`](./cgcontext.md) instead.

## Declaration

```swift
var graphicsPort: UnsafeMutableRawPointer { get }
```

```objc
@property (readonly) void * graphicsPort;
```

#### Discussion

In macOS, this is the Core Graphics context, a [`CGContext`](../../CoreGraphics/cgcontext.md) object (opaque type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/graphicsport)*