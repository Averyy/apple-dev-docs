# intValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) int intValue;
```

#### Discussion

The integer value of the string, assuming a decimal representation and skipping whitespace at the beginning of the string. This property is `INT_MAX` or `INT_MIN` on overflow. This property is `0` if the string doesn’t begin with a valid decimal text representation of a number.

This property uses formatting information stored in the non-localized value; use an [`Scanner`](../scanner.md) object for localized scanning of numeric values from a string.

##### Special Considerations

In macOS 10.5 and later, use [`integerValue`](./integervalue.md) instead.

## See Also

### Related Documentation
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](../scanner/scanint32%28_%29.md)
  Scans for an int value from a decimal representation, returning a found value by reference.
### Getting Numeric Values
- [var doubleValue: Double](./doublevalue.md)
  The floating-point value of the string as a `double`.
- [var floatValue: Float](./floatvalue.md)
  The floating-point value of the string as a `float`.
- [var integerValue: Int](./integervalue.md)
  The `NSInteger` value of the string.
- [var longLongValue: Int64](./longlongvalue.md)
  The `long long` value of the string.
- [var boolValue: Bool](./boolvalue.md)
  The Boolean value of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/intvalue)*