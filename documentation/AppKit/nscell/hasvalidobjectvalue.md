# hasValidObjectValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the cell has a valid object value.

**Availability**:
- macOS

## Declaration

```swift
var hasValidObjectValue: Bool { get }
```

```objc
@property (readonly) BOOL hasValidObjectValue;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell has a valid object value or [`false`](../../Swift/false.md) if it does not. A valid object value is one that the cell’s formatter can “understand.” Objects are always assumed to be valid unless they are rejected by the formatter. Invalid objects can still be accepted by the delegate of the cell’s [`NSControl`](../nscontrol.md) object (using the [`control(_:didFailToFormatString:errorDescription:)`](../nscontroltexteditingdelegate/control%28_,didfailtoformatstring,errordescription%29.md) delegate method).

## See Also

### Managing Cell Values
- [var objectValue: Any?](./objectvalue.md)
  The cell’s value as an Objective-C object.
- [var intValue: Int32](./intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](./integervalue.md)
  The cell’s value as an integer value.
- [var stringValue: String](./stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](./doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](./floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/hasvalidobjectvalue)*