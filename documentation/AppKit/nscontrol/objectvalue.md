# objectValue

**Framework**: AppKit  
**Kind**: property

The value of the receiver’s cell as an Objective-C object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var objectValue: Any? { get set }
```

#### Discussion

If the control contains many cells (for example, `NSMatrix`), then this property contains the value of the currently selected cell. If the control is in the process of editing the affected cell, then it invokes the  [`validateEditing()`](nscontrol/validateediting().md) method before getting the value.

If the cell is being edited, setting this property aborts all editing before setting the value. If the cell does not inherit from `NSActionCell`, setting this property marks the cell’s interior as needing to be redisplayed; `NSActionCell` performs its own updating of cells.

## See Also

- [var doubleValue: Double](nscontrol/doublevalue.md)
  The value of the receiver’s cell as a double-precision floating-point number.
- [var floatValue: Float](nscontrol/floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
- [var intValue: Int32](nscontrol/intvalue.md)
  The value of the receiver’s cell as an integer.
- [var integerValue: Int](nscontrol/integervalue.md)
  The value of the receiver’s cell as an [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) value.
- [var stringValue: String](nscontrol/stringvalue.md)
  The value of the receiver’s cell as an `NSString` object.
- [var attributedStringValue: NSAttributedString](nscontrol/attributedstringvalue.md)
  The value of the receiver’s cell as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/objectvalue)*