# scanHexInt32(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Scans for an unsigned value from a hexadecimal representation, returning a found value by reference.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
func scanHexInt32(_ result: UnsafeMutablePointer<UInt32>?) -> Bool
```

```objc
- (BOOL) scanHexInt:(unsigned int *) result;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the receiver finds a valid hexadecimal integer representation, otherwise [`false`](../../Swift/false.md). Overflow is considered a valid hexadecimal integer representation.

## Discussion

The hexadecimal integer representation may optionally be preceded by `0x` or `0X`. Skips past excess digits in the case of overflow, so the receiver’s position is past the entire hexadecimal representation.

Invoke this method with `NULL` as `intValue` to simply scan past a hexadecimal integer representation.

## Parameters

- `result`: Upon return, contains the scanned value. Contains `UINT_MAX` on overflow.

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
- [func scanHexInt64(UnsafeMutablePointer<UInt64>?) -> Bool](./scanhexint64%28_%29.md)
  Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [func scanInt(UnsafeMutablePointer<Int>?) -> Bool](./scanint%28_%29.md)
  Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [func scanInt32(UnsafeMutablePointer<Int32>?) -> Bool](./scanint32%28_%29.md)
  Scans for an int value from a decimal representation, returning a found value by reference.
- [func scanInt64(UnsafeMutablePointer<Int64>?) -> Bool](./scanint64%28_%29.md)
  Scans for a long long value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](./scanunsignedlonglong%28_%29.md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanhexint32(_:))*