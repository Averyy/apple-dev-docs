# refusesFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver refuses the first responder role.

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

The value of this property is [`true`](../../Swift/true.md) if the receiver refuses the first responder role; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var objectValue: Any?](./objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [var doubleValue: Double](./doublevalue.md)
  The value of the receiver’s cell as a double-precision floating-point number.
- [var floatValue: Float](./floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
### Activating from the Keyboard
- [func performClick(Any?)](./performclick%28_%29.md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/refusesfirstresponder)*