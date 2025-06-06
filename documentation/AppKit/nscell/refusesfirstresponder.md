# refusesFirstResponder

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell refuses the first responder status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var refusesFirstResponder: Bool { get set }
```

#### Discussion

Set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) to prevent the cell from becoming the first responder. To determine whether the cell can become first responder right now, get the value of the [`acceptsFirstResponder`](nscell/acceptsfirstresponder.md) property.

## See Also

- [var acceptsFirstResponder: Bool](nscell/acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var showsFirstResponder: Bool](nscell/showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [func performClick(Any?)](nscell/performclick(_:).md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/refusesfirstresponder)*