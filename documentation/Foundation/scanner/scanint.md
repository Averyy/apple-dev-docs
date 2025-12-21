# scanInt(_:)

**Framework**: Foundation  
**Kind**: method

Scans for an NSInteger value from a decimal representation, returning a found value by reference

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
func scanInt(_ result: UnsafeMutablePointer<Int>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver finds a valid integer representation, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). Overflow is considered a valid integer representation.

#### Discussion

Skips past excess digits in the case of overflow, so the receiver’s position is past the entire integer representation.

Invoke this method with `NULL` as `value` to simply scan past a decimal integer representation.

## Parameters

- `result`: Upon return, contains the scanned value. Contains   or   on overflow.

## See Also

- [var integerValue: Int](nsstring/integervalue.md)
  The `NSInteger` value of the string.
- [func scanDecimal(UnsafeMutablePointer<Decimal>?) -> Bool](scanner/scandecimal(_:).md)
  Scans for an `NSDecimal` value, returning a found value by reference.
- [func scanDouble(UnsafeMutablePointer<Double>?) -> Bool](scanner/scandouble(_:).md)
  Scans for a double value, returning a found value by reference.
- [func scanFloat(UnsafeMutablePointer<Float>?) -> Bool](scanner/scanfloat(_:).md)
  Scans for a float value, returning a found value by reference.
- [func scanHexDouble(UnsafeMutablePointer<Double>?) -> Bool](scanner/scanhexdouble(_:).md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexFloat(UnsafeMutablePointer<Float>?) -> Bool](scanner/scanhexfloat(_:).md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt32(UnsafeMutablePointer<UInt32>?) -> Bool](scanner/scanhexint32(_:).md)
  Scans for an unsigned value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt64(UnsafeMutablePointer<UInt64>?) -> Bool](scanner/scanhexint64(_:).md)
  Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](scanner/scanint32(_:).md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [func scanInt64(UnsafeMutablePointer<Int64>?) -> Bool](scanner/scanint64(_:).md)
  Scans for a long long value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](scanner/scanunsignedlonglong(_:).md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanint(_:))*