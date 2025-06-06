# keyDown(with:)

**Framework**: RealityKit  
**Kind**: method

Informs the view that the user has pressed a key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic func keyDown(with event: NSEvent)
```

#### Discussion

The view handles the event instead of passing it to the next responder. See [`NSResponder`](https://developer.apple.com/documentation/AppKit/NSResponder) for more information about the responder chain.

## Parameters

- `event`: An object encapsulating information about the key-down event.

## See Also

- [var acceptsFirstResponder: Bool](arview/acceptsfirstresponder.md)
  A Boolean value that indicates whether the view accepts first responder status.
- [func keyUp(with: NSEvent)](arview/keyup(with:).md)
  Informs the view that the user has released a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/keydown(with:))*