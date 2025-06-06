# intValue

**Framework**: Foundation  
**Kind**: property

The integer value of the string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var intValue: Int32 { get }
```

#### Discussion

The integer value of the string, assuming a decimal representation and skipping whitespace at the beginning of the string. This property is `INT_MAX` or `INT_MIN` on overflow. This property is `0` if the string doesn’t begin with a valid decimal text representation of a number.

This property uses formatting information stored in the non-localized value; use an [`Scanner`](scanner.md) object for localized scanning of numeric values from a string.

##### Special Considerations

In macOS 10.5 and later, use [`integerValue`](nsstring/integervalue.md) instead.

## See Also

- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](scanner/scanint32(_:).md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [var doubleValue: Double](nsstring/doublevalue.md)
  The floating-point value of the string as a `double`.
- [var floatValue: Float](nsstring/floatvalue.md)
  The floating-point value of the string as a `float`.
- [var integerValue: Int](nsstring/integervalue.md)
  The `NSInteger` value of the string.
- [var longLongValue: Int64](nsstring/longlongvalue.md)
  The `long long` value of the string.
- [var boolValue: Bool](nsstring/boolvalue.md)
  The Boolean value of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/intvalue)*