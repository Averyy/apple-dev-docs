# scanHexInt32(_:)

**Framework**: Foundation  
**Kind**: method

Scans for an unsigned value from a hexadecimal representation, returning a found value by reference.

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
func scanHexInt32(_ result: UnsafeMutablePointer<UInt32>?) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver finds a valid hexadecimal integer representation, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). Overflow is considered a valid hexadecimal integer representation.

#### Discussion

The hexadecimal integer representation may optionally be preceded by `0x` or `0X`. Skips past excess digits in the case of overflow, so the receiver’s position is past the entire hexadecimal representation.

Invoke this method with `NULL` as `intValue` to simply scan past a hexadecimal integer representation.

## Parameters

- `result`: Upon return, contains the scanned value. Contains   on overflow.

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanhexint32(_:))*