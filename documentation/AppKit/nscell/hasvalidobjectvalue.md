# hasValidObjectValue

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the cell has a valid object value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var hasValidObjectValue: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the cell has a valid object value or [`false`](https://developer.apple.com/documentation/swift/false) if it does not. A valid object value is one that the cell’s formatter can “understand.” Objects are always assumed to be valid unless they are rejected by the formatter. Invalid objects can still be accepted by the delegate of the cell’s [`NSControl`](nscontrol.md) object (using the [`control(_:didFailToFormatString:errorDescription:)`](nscontroltexteditingdelegate/control(_:didfailtoformatstring:errordescription:).md) delegate method).

## See Also

- [var objectValue: Any?](nscell/objectvalue.md)
  The cell’s value as an Objective-C object.
- [var intValue: Int32](nscell/intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](nscell/integervalue.md)
  The cell’s value as an [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) type.
- [var stringValue: String](nscell/stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/hasvalidobjectvalue)*