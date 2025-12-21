# objectValue

**Framework**: AppKit  
**Kind**: property

The cell’s value as an Objective-C object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var objectValue: Any? { get set }
```

#### Discussion

To be valid object value, the cell must have a formatter capable of converting the object to and from its textual representation. The value of this property is `nil` if an object has not been assigned to the cell.

## See Also

- [var hasValidObjectValue: Bool](nscell/hasvalidobjectvalue.md)
  A Boolean value that indicates whether the cell has a valid object value.
- [var intValue: Int32](nscell/intvalue.md)
  The cell’s value as an integer.
- [var integerValue: Int](nscell/integervalue.md)
  The cell’s value as an integer value.
- [var stringValue: String](nscell/stringvalue.md)
  The cell’s value as a string.
- [var doubleValue: Double](nscell/doublevalue.md)
  The cell’s value as a double-precision floating-point number.
- [var floatValue: Float](nscell/floatvalue.md)
  The cell’s value as a single-precision floating-point number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/objectvalue)*