# acceptsFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell accepts first responder status.

**Availability**:
- macOS

## Declaration

```swift
var acceptsFirstResponder: Bool { get }
```

```objc
@property (readonly) BOOL acceptsFirstResponder;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the cell is able to become the first responder. The default value of this property is [`true`](../../Swift/true.md) when the cell is enabled. Subclasses may override this method to return a different value.

## See Also

### Respond to Keyboard Events
- [var showsFirstResponder: Bool](./showsfirstresponder.md)
  A Boolean value indicating whether the cell provides a visual indication that it is the first responder.
- [var refusesFirstResponder: Bool](./refusesfirstresponder.md)
  A Boolean value indicating whether the cell refuses the first responder status.
- [func performClick(Any?)](./performclick%28_%29.md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/acceptsfirstresponder)*