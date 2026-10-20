# showsFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell provides a visual indication that it is the first responder.

**Availability**:
- macOS

## Declaration

```swift
var showsFirstResponder: Bool { get set }
```

```objc
@property BOOL showsFirstResponder;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md) and the cell becomes the first responder, the cell performs additional drawing to indicate that it is the first responder. The `NSCell` class itself does not draw a first-responder indicator. Subclasses may use the value in this property to determine whether or not they should draw one.

## See Also

### Respond to Keyboard Events
- [var acceptsFirstResponder: Bool](./acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var refusesFirstResponder: Bool](./refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.
- [func performClick(Any?)](./performclick%28_%29.md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/showsfirstresponder)*