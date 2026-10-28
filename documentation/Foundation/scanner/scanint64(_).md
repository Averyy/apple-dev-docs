# scanInt64(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Scans for a long long value from a decimal representation, returning a found value by reference.

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
func scanInt64(_ result: UnsafeMutablePointer<Int64>?) -> Bool
```

```objc
- (BOOL) scanLongLong:(long long *) result;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver finds a valid decimal integer representation, otherwise [`false`](../../Swift/false.md). Overflow is considered a valid decimal integer representation.

## Discussion

All overflow digits are skipped. Skips past excess digits in the case of overflow, so the receiver’s position is past the entire decimal representation.

Invoke this method with `NULL` as `longLongValue` to simply scan past a long decimal integer representation.

## Parameters

- `result`: Upon return, contains the scanned value. Contains `LLONG_MAX` or `LLONG_MIN` on overflow.

## See Also

### Scanning Numeric Values
- [func scanDecimal(UnsafeMutablePointer<Decimal>?) -> Bool](./scandecimal%28_%29.md)
  Scans for an `NSDecimal` value, returning a found value by reference.
- [func scanDouble(UnsafeMutablePointer<Double>?) -> Bool](./scandouble%28_%29.md)
  Scans for a double value, returning a found value by reference.
- [func scanFloat(UnsafeMutablePointer<Float>?) -> Bool](./scanfloat%28_%29.md)
  Scans for a float value, returning a found value by reference.
- [func scanHexDouble(UnsafeMutablePointer<Double>?) -> Bool](./scanhexdouble%28_%29.md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexFloat(UnsafeMutablePointer<Float>?) -> Bool](./scanhexfloat%28_%29.md)
  Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt32(UnsafeMutablePointer<UInt32>?) -> Bool](./scanhexint32%28_%29.md)
  Scans for an unsigned value from a hexadecimal representation, returning a found value by reference.
- [func scanHexInt64(UnsafeMutablePointer<UInt64>?) -> Bool](./scanhexint64%28_%29.md)
  Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [func scanInt(UnsafeMutablePointer<Int>?) -> Bool](./scanint%28_%29.md)
  Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](./scanint32%28_%29.md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](./scanunsignedlonglong%28_%29.md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanint64(_:))*