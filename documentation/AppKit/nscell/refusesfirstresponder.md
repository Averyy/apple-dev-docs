# refusesFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell refuses the first responder status.

**Availability**:
- macOS

## Declaration

```swift
var refusesFirstResponder: Bool { get set }
```

```objc
@property BOOL refusesFirstResponder;
```

## Discussion

Set the value of this property to [`true`](../../Swift/true.md) to prevent the cell from becoming the first responder. To determine whether the cell can become first responder right now, get the value of the [`acceptsFirstResponder`](./acceptsfirstresponder.md) property.

## See Also

### Respond to Keyboard Events
- [var acceptsFirstResponder: Bool](./acceptsfirstresponder.md)
  A Boolean value indicating whether the cell accepts first responder status.
- [var showsFirstResponder: Bool](./showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [func performClick(Any?)](./performclick%28_%29.md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/refusesfirstresponder)*