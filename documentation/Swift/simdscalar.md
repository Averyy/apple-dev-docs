# SIMDScalar

**Framework**: Swift  
**Kind**: protocol

A type that can be used as an element in a SIMD vector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol SIMDScalar : BitwiseCopyable
```

## Topics

### Associated Types
- [associatedtype SIMD16Storage : SIMDStorage](simdscalar/simd16storage.md)
- [associatedtype SIMD2Storage : SIMDStorage](simdscalar/simd2storage.md)
- [associatedtype SIMD32Storage : SIMDStorage](simdscalar/simd32storage.md)
- [associatedtype SIMD4Storage : SIMDStorage](simdscalar/simd4storage.md)
- [associatedtype SIMD64Storage : SIMDStorage](simdscalar/simd64storage.md)
- [associatedtype SIMD8Storage : SIMDStorage](simdscalar/simd8storage.md)
- [associatedtype SIMDMaskScalar : FixedWidthInteger, SIMDScalar, SignedInteger](simdscalar/simdmaskscalar.md)

## Relationships

### Inherits From
- [BitwiseCopyable](bitwisecopyable.md)
### Conforming Types
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Int](int.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [UInt](uint.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)

## See Also

- [protocol SIMD](simd.md)
  A SIMD vector of a fixed number of elements.
- [protocol SIMDStorage](simdstorage.md)
  A type that can function as storage for a SIMD vector type.
- [struct SIMDMask](simdmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdscalar)*