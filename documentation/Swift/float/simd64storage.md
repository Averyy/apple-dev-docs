# Float.SIMD64Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of 64 floating-point values.

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
@frozen
struct SIMD64Storage
```

## Topics

### Initializers
- [init()](float/simd64storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](float/simd64storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Float](float/simd64storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Float.SIMD64Storage.Scalar](float/simd64storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)

## See Also

- [typealias SIMDMaskScalar](float/simdmaskscalar.md)
- [struct SIMD2Storage](float/simd2storage.md)
  Storage for a vector of two floating-point values.
- [struct SIMD4Storage](float/simd4storage.md)
  Storage for a vector of four floating-point values.
- [struct SIMD8Storage](float/simd8storage.md)
  Storage for a vector of eight floating-point values.
- [struct SIMD16Storage](float/simd16storage.md)
  Storage for a vector of 16 floating-point values.
- [struct SIMD32Storage](float/simd32storage.md)
  Storage for a vector of 32 floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/simd64storage)*