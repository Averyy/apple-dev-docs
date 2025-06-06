# SIMDStorage

**Framework**: Swift  
**Kind**: protocol

A type that can function as storage for a SIMD vector type.

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
protocol SIMDStorage
```

#### Overview

The `SIMDStorage` protocol defines a storage layout and provides elementwise accesses. Computational operations are defined on the `SIMD` protocol, which refines this protocol, and on the concrete types that conform to `SIMD`.

## Topics

### Associated Types
- [associatedtype Scalar : Decodable, Encodable, Hashable](simdstorage/scalar.md)
### Initializers
- [init()](simdstorage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](simdstorage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Self.Scalar](simdstorage/subscript(_:).md)
  Accesses the element at the specified index.

## Relationships

### Inherited By
- [SIMD](simd.md)
### Conforming Types
- [Double.SIMD16Storage](double/simd16storage.md)
- [Double.SIMD2Storage](double/simd2storage.md)
- [Double.SIMD32Storage](double/simd32storage.md)
- [Double.SIMD4Storage](double/simd4storage.md)
- [Double.SIMD64Storage](double/simd64storage.md)
- [Double.SIMD8Storage](double/simd8storage.md)
- [Float.SIMD16Storage](float/simd16storage.md)
- [Float.SIMD2Storage](float/simd2storage.md)
- [Float.SIMD32Storage](float/simd32storage.md)
- [Float.SIMD4Storage](float/simd4storage.md)
- [Float.SIMD64Storage](float/simd64storage.md)
- [Float.SIMD8Storage](float/simd8storage.md)
- [Float16.SIMD16Storage](float16/simd16storage.md)
- [Float16.SIMD2Storage](float16/simd2storage.md)
- [Float16.SIMD32Storage](float16/simd32storage.md)
- [Float16.SIMD4Storage](float16/simd4storage.md)
- [Float16.SIMD64Storage](float16/simd64storage.md)
- [Float16.SIMD8Storage](float16/simd8storage.md)
- [Int.SIMD16Storage](int/simd16storage.md)
- [Int.SIMD2Storage](int/simd2storage.md)
- [Int.SIMD32Storage](int/simd32storage.md)
- [Int.SIMD4Storage](int/simd4storage.md)
- [Int.SIMD64Storage](int/simd64storage.md)
- [Int.SIMD8Storage](int/simd8storage.md)
- [Int16.SIMD16Storage](int16/simd16storage.md)
- [Int16.SIMD2Storage](int16/simd2storage.md)
- [Int16.SIMD32Storage](int16/simd32storage.md)
- [Int16.SIMD4Storage](int16/simd4storage.md)
- [Int16.SIMD64Storage](int16/simd64storage.md)
- [Int16.SIMD8Storage](int16/simd8storage.md)
- [Int32.SIMD16Storage](int32/simd16storage.md)
- [Int32.SIMD2Storage](int32/simd2storage.md)
- [Int32.SIMD32Storage](int32/simd32storage.md)
- [Int32.SIMD4Storage](int32/simd4storage.md)
- [Int32.SIMD64Storage](int32/simd64storage.md)
- [Int32.SIMD8Storage](int32/simd8storage.md)
- [Int64.SIMD16Storage](int64/simd16storage.md)
- [Int64.SIMD2Storage](int64/simd2storage.md)
- [Int64.SIMD32Storage](int64/simd32storage.md)
- [Int64.SIMD4Storage](int64/simd4storage.md)
- [Int64.SIMD64Storage](int64/simd64storage.md)
- [Int64.SIMD8Storage](int64/simd8storage.md)
- [Int8.SIMD16Storage](int8/simd16storage.md)
- [Int8.SIMD2Storage](int8/simd2storage.md)
- [Int8.SIMD32Storage](int8/simd32storage.md)
- [Int8.SIMD4Storage](int8/simd4storage.md)
- [Int8.SIMD64Storage](int8/simd64storage.md)
- [Int8.SIMD8Storage](int8/simd8storage.md)
- [SIMD16](simd16.md)
- [SIMD2](simd2.md)
- [SIMD3](simd3.md)
- [SIMD32](simd32.md)
- [SIMD4](simd4.md)
- [SIMD64](simd64.md)
- [SIMD8](simd8.md)
- [SIMDMask](simdmask.md)
- [UInt.SIMD16Storage](uint/simd16storage.md)
- [UInt.SIMD2Storage](uint/simd2storage.md)
- [UInt.SIMD32Storage](uint/simd32storage.md)
- [UInt.SIMD4Storage](uint/simd4storage.md)
- [UInt.SIMD64Storage](uint/simd64storage.md)
- [UInt.SIMD8Storage](uint/simd8storage.md)
- [UInt16.SIMD16Storage](uint16/simd16storage.md)
- [UInt16.SIMD2Storage](uint16/simd2storage.md)
- [UInt16.SIMD32Storage](uint16/simd32storage.md)
- [UInt16.SIMD4Storage](uint16/simd4storage.md)
- [UInt16.SIMD64Storage](uint16/simd64storage.md)
- [UInt16.SIMD8Storage](uint16/simd8storage.md)
- [UInt32.SIMD16Storage](uint32/simd16storage.md)
- [UInt32.SIMD2Storage](uint32/simd2storage.md)
- [UInt32.SIMD32Storage](uint32/simd32storage.md)
- [UInt32.SIMD4Storage](uint32/simd4storage.md)
- [UInt32.SIMD64Storage](uint32/simd64storage.md)
- [UInt32.SIMD8Storage](uint32/simd8storage.md)
- [UInt64.SIMD16Storage](uint64/simd16storage.md)
- [UInt64.SIMD2Storage](uint64/simd2storage.md)
- [UInt64.SIMD32Storage](uint64/simd32storage.md)
- [UInt64.SIMD4Storage](uint64/simd4storage.md)
- [UInt64.SIMD64Storage](uint64/simd64storage.md)
- [UInt64.SIMD8Storage](uint64/simd8storage.md)
- [UInt8.SIMD16Storage](uint8/simd16storage.md)
- [UInt8.SIMD2Storage](uint8/simd2storage.md)
- [UInt8.SIMD32Storage](uint8/simd32storage.md)
- [UInt8.SIMD4Storage](uint8/simd4storage.md)
- [UInt8.SIMD64Storage](uint8/simd64storage.md)
- [UInt8.SIMD8Storage](uint8/simd8storage.md)

## See Also

- [protocol SIMD](simd.md)
  A SIMD vector of a fixed number of elements.
- [protocol SIMDScalar](simdscalar.md)
  A type that can be used as an element in a SIMD vector.
- [struct SIMDMask](simdmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdstorage)*