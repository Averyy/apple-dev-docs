# boolValue

**Framework**: Foundation  
**Kind**: property

The Boolean value of the string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boolValue: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/swift/true) on encountering one of “Y”, “y”, “T”, “t”, or a digit 1-9—the method ignores any trailing characters. This property is [`false`](https://developer.apple.com/documentation/swift/false) if the receiver doesn’t begin with a valid decimal text representation of a number.

The property assumes a decimal representation and skips whitespace at the beginning of the string. It also skips initial whitespace characters, or optional -/+ sign followed by zeroes.

## See Also

- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](scanner/scanint32(_:).md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [var doubleValue: Double](nsstring/doublevalue.md)
  The floating-point value of the string as a `double`.
- [var floatValue: Float](nsstring/floatvalue.md)
  The floating-point value of the string as a `float`.
- [var intValue: Int32](nsstring/intvalue.md)
  The integer value of the string.
- [var integerValue: Int](nsstring/integervalue.md)
  The `NSInteger` value of the string.
- [var longLongValue: Int64](nsstring/longlongvalue.md)
  The `long long` value of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/boolvalue)*