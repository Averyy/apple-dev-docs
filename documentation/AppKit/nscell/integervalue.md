# integerValue

**Framework**: AppKit  
**Kind**: property

The cell’s value as an integer value.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var integerValue: Int { get set }
```

#### Discussion

This property uses the [`objectValue`](nscell/objectvalue.md) property to access the actual value. If the cell is not a text-type cell or its contents are not scannable, the value in this property is `0`.

## See Also

- [var objectValue: Any?](nscell/objectvalue.md)
  The cell’s value as an Objective-C object.
- [var hasValidObjectValue: Bool](nscell/hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](nscell/intvalue.md)
  The cell’s value as an integer.
- [var stringValue: String](nscell/stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/integervalue)*