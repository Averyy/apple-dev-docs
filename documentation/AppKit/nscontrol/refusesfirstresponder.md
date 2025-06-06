# refusesFirstResponder

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the receiver refuses the first responder role.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var refusesFirstResponder: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the receiver refuses the first responder role; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [var doubleValue: Double](nscontrol/doublevalue.md)
  The value of the receiver’s cell as a double-precision floating-point number.
- [var floatValue: Float](nscontrol/floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
- [func performClick(Any?)](nscontrol/performclick(_:).md)
  Simulates a single mouse click on the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/refusesfirstresponder)*