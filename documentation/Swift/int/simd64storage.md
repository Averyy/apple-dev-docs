# Int.SIMD64Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of 64 integers.

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
- [init()](int/simd64storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](int/simd64storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Int](int/simd64storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Int.SIMD64Storage.Scalar](int/simd64storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [typealias SIMDMaskScalar](int/simdmaskscalar.md)
- [struct SIMD2Storage](int/simd2storage.md)
  Storage for a vector of two integers.
- [struct SIMD4Storage](int/simd4storage.md)
  Storage for a vector of four integers.
- [struct SIMD8Storage](int/simd8storage.md)
  Storage for a vector of eight integers.
- [struct SIMD16Storage](int/simd16storage.md)
  Storage for a vector of 16 integers.
- [struct SIMD32Storage](int/simd32storage.md)
  Storage for a vector of 32 integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/simd64storage)*