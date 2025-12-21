# showsFirstResponder

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell provides a visual indication that it is the first responder.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var showsFirstResponder: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the cell becomes the first responder, the cell performs additional drawing to indicate that it is the first responder. The `NSCell` class itself does not draw a first-responder indicator. Subclasses may use the value in this property to determine whether or not they should draw one.

## See Also

- [var acceptsFirstResponder: Bool](nscell/acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var refusesFirstResponder: Bool](nscell/refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.
- [func performClick(Any?)](nscell/performclick(_:).md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/showsfirstresponder)*