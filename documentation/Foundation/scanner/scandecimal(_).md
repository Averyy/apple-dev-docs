# scanDecimal(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Scans for an `NSDecimal` value, returning a found value by reference.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func scanDecimal(_ dcm: UnsafeMutablePointer<Decimal>?) -> Bool
```

```objc
- (BOOL) scanDecimal:(NSDecimal *) dcm;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver finds a valid `NSDecimal` representation, otherwise [`false`](../../Swift/false.md).

#### Discussion

Invoke this method with `NULL` as `decimalValue` to simply scan past an `NSDecimal` representation.

## Parameters

- `dcm`: Upon return, contains the scanned value. See the [`NSDecimalNumber`](../nsdecimalnumber.md) class specification for more information about `NSDecimal` values.

## See Also

### Scanning Numeric Values
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
- [func scanInt64(UnsafeMutablePointer<Int64>?) -> Bool](./scanint64%28_%29.md)
  Scans for a long long value from a decimal representation, returning a found value by reference.
- [func scanUnsignedLongLong(UnsafeMutablePointer<UInt64>?) -> Bool](./scanunsignedlonglong%28_%29.md)
  Scans for an unsigned long long value from a decimal representation, returning a found value by reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scandecimal(_:))*