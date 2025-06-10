# Double.SIMD2Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of two floating-point values.

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
struct SIMD2Storage
```

## Topics

### Initializers
- [init()](double/simd2storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](double/simd2storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Double](double/simd2storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Double.SIMD2Storage.Scalar](double/simd2storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [typealias SIMDMaskScalar](double/simdmaskscalar.md)
- [Double.SIMD4Storage](double/simd4storage.md)
  Storage for a vector of four floating-point values.
- [Double.SIMD8Storage](double/simd8storage.md)
  Storage for a vector of eight floating-point values.
- [Double.SIMD16Storage](double/simd16storage.md)
  Storage for a vector of 16 floating-point values.
- [Double.SIMD32Storage](double/simd32storage.md)
  Storage for a vector of 32 floating-point values.
- [Double.SIMD64Storage](double/simd64storage.md)
  Storage for a vector of 64 floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/simd2storage)*