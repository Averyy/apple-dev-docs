# scanDouble(_:)

**Framework**: Foundation  
**Kind**: method

Scans for a double value, returning a found value by reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func scanDouble(_ result: UnsafeMutablePointer<Double>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver finds a valid floating-point representation, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). Overflow or underflow are both considered valid floating-point representations.

#### Discussion

Skips past excess digits in the case of overflow, so the scanner’s position is past the entire floating-point representation.

Invoke this method with `NULL` as `doubleValue` to simply scan past a double value representation. Floating-point representations are assumed to be IEEE compliant.

## Parameters

- `result`: Upon return, contains the scanned value. Contains   or   on overflow, or   on underflow.

## See Also

- [var doubleValue: Double](nsstring/doublevalue.md)
  The floating-point value of the string as a `double`.
- [func scanDecimal(UnsafeMutablePointer<Decimal>?) -> Bool](scanner/scandecimal(_:).md)
  Scans for an `NSDecimal` value, returning a found value by reference.
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
- [func scanInt(UnsafeMutablePointer<Int>?) -> Bool](scanner/scanint(_:).md)
  Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](scanner/scanint32(_:).md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [func scanInt64(UnsafeMutablePointer<Int64>?) -> Bool](scanner/scanint64(_:).md)
  Scans for a long long value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](scanner/scanunsignedlonglong(_:).md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scandouble(_:))*