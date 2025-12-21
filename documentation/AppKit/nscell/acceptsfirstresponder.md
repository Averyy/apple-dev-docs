# acceptsFirstResponder

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell accepts first responder status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var acceptsFirstResponder: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the cell is able to become the first responder. The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the cell is enabled. Subclasses may override this method to return a different value.

## See Also

- [var showsFirstResponder: Bool](nscell/showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [var refusesFirstResponder: Bool](nscell/refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.
- [func performClick(Any?)](nscell/performclick(_:).md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/acceptsfirstresponder)*