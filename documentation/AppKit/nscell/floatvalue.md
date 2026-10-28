# floatValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s value as a single-precision floating-point number.

**Availability**:
- macOS

## Declaration

```swift
var floatValue: Float { get set }
```

```objc
@property float floatValue;
```

## Discussion

This property uses the [`objectValue`](./objectvalue.md) property to access the actual value. If the cell is not a text-type cell or the cell’s value is not scannable, this property contains the value `0`.

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
- [var stringValue: String](./stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](./doublevalue.md)
  The cell’s value as a double-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/floatvalue)*