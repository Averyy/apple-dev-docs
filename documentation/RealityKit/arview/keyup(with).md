# keyUp(with:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that the user has released a key.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func keyUp(with event: NSEvent)
```

## Discussion

The view handles the event instead of passing it to the next responder. See [`NSResponder`](../../AppKit/nsresponder.md) for more information about the responder chain.

## Parameters

- `event`: An object encapsulating information about the key-up event.

## See Also

### Handling keyboard input
- [var acceptsFirstResponder: Bool](./acceptsfirstresponder.md)
  A Boolean value that indicates whether the view accepts first responder status.
- [func keyDown(with: NSEvent)](./keydown%28with%29.md)
  Informs the view that the user has pressed a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/keyup(with:))*