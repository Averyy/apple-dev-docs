# stringValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s value as a string.

**Availability**:
- macOS

## Declaration

```swift
var stringValue: String { get set }
```

```objc
@property (copy) NSString * stringValue;
```

## Discussion

This property uses the [`objectValue`](./objectvalue.md) property to access the actual value. If no formatter is assigned to the cell or if the formatter cannot “translate” a new string appropriately, the cell is flagged as having an invalid object. If the cell’s object is not an [`NSString`](../../Foundation/nsstring.md) object or cannot be converted to one, this property contains an empty string. If the cell is not a text-type cell, this method converts it to one before setting the object value.

If you use a class that has an [`attributedStringValue`](./attributedstringvalue.md) property, the cell gets the string from that property instead of this one.

## See Also

### Managing Cell Values
- [var objectValue: Any?](./objectvalue.md)
  The cell’s value as an Objective-C object.
- [var hasValidObjectValue: Bool](./hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](./intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](./integervalue.md)
  The cell’s value as an integer value.
- [var doubleValue: Double](./doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](./floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/stringvalue)*