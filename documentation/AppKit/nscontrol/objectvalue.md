# objectValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The value of the receiver’s cell as an Objective-C object.

**Availability**:
- macOS

## Declaration

```swift
var objectValue: Any? { get set }
```

```objc
@property (copy, nullable) id objectValue;
```

## Discussion

If the control contains many cells (for example, `NSMatrix`), then this property contains the value of the currently selected cell. If the control is in the process of editing the affected cell, then it invokes the  [`validateEditing()`](./validateediting%28%29.md) method before getting the value.

If the cell is being edited, setting this property aborts all editing before setting the value. If the cell does not inherit from `NSActionCell`, setting this property marks the cell’s interior as needing to be redisplayed; `NSActionCell` performs its own updating of cells.

## See Also

### Accessing the Control’s Value
- [var doubleValue: Double](./doublevalue.md)
  The value of the receiver’s cell as a double-precision floating-point number.
- [var floatValue: Float](./floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
- [var intValue: Int32](./intvalue.md)
  The value of the receiver’s cell as an integer.
- [var integerValue: Int](./integervalue.md)
  The value of the receiver’s cell as an integer value.
- [var stringValue: String](./stringvalue.md)
  The value of the receiver’s cell as an `NSString` object.
- [var attributedStringValue: NSAttributedString](./attributedstringvalue.md)
  The value of the receiver’s cell as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/objectvalue)*