# stringValue

**Framework**: AppKit  
**Kind**: property

The cell’s value as a string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var stringValue: String { get set }
```

#### Discussion

This property uses the [`objectValue`](nscell/objectvalue.md) property to access the actual value. If no formatter is assigned to the cell or if the formatter cannot “translate” a new string appropriately, the cell is flagged as having an invalid object. If the cell’s object is not an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object or cannot be converted to one, this property contains an empty string. If the cell is not a text-type cell, this method converts it to one before setting the object value.

If you use a class that has an [`attributedStringValue`](nscell/attributedstringvalue.md) property, the cell gets the string from that property instead of this one.

## See Also

- [var objectValue: Any?](nscell/objectvalue.md)
  The cell’s value as an Objective-C object.
- [var hasValidObjectValue: Bool](nscell/hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](nscell/intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](nscell/integervalue.md)
  The cell’s value as an integer value.
- [var doubleValue: Double](nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stringvalue)*