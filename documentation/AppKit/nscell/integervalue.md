# integerValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s value as an integer value.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var integerValue: Int { get set }
```

```objc
@property NSInteger integerValue;
```

## Discussion

This property uses the [`objectValue`](./objectvalue.md) property to access the actual value. If the cell is not a text-type cell or its contents are not scannable, the value in this property is `0`.

## See Also

### Managing Cell Values
- [var objectValue: Any?](./objectvalue.md)
  The cell’s value as an Objective-C object.
- [var hasValidObjectValue: Bool](./hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](./intvalue.md)
  The cell’s value as an integer.
- [var stringValue: String](./stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](./doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](./floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/integervalue)*