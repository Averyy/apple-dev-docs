# objectValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The cell’s value as an Objective-C object.

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

To be valid object value, the cell must have a formatter capable of converting the object to and from its textual representation. The value of this property is `nil` if an object has not been assigned to the cell.

## See Also

### Managing Cell Values
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
- [var floatValue: Float](./floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/objectvalue)*