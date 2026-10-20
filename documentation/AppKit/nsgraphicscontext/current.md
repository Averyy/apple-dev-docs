# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the current graphics context of the current thread.

**Availability**:
- macOS

## Declaration

```swift
class var current: NSGraphicsContext? { get set }
```

```objc
@property (class, strong, nullable) NSGraphicsContext * currentContext;
```

#### Return Value

The current graphics context of the current thread.

#### Discussion

Returns an instance of a concrete subclass of [`NSGraphicsContext`](../nsgraphicscontext.md).

## See Also

### Managing the Current Context
- [var cgContext: CGContext](./cgcontext.md)
  The Core Graphics context, which is a low-level, platform-specific graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/current)*