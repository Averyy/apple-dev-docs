# acceptsFirstResponder

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view accepts first responder status.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var acceptsFirstResponder: Bool { get }
```

#### Discussion

An [`ARView`](../arview.md) instance sets this value to `true` by default to indicate that it does accept first responder status. See [`NSResponder`](../../AppKit/nsresponder.md) for more information about the responder chain.

## See Also

### Handling keyboard input
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the view that the user has pressed a key.
- [func keyUp(with: NSEvent)](./keyup%28with%29.md)
  Informs the view that the user has released a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/acceptsfirstresponder)*