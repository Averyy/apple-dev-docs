# Int.SIMD8Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of eight integers.

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
struct SIMD8Storage
```

## Topics

### Initializers
- [init()](int/simd8storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](int/simd8storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Int](int/simd8storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Int.SIMD8Storage.Scalar](int/simd8storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)

## See Also

- [typealias SIMDMaskScalar](int/simdmaskscalar.md)
- [struct SIMD2Storage](int/simd2storage.md)
  Storage for a vector of two integers.
- [struct SIMD4Storage](int/simd4storage.md)
  Storage for a vector of four integers.
- [struct SIMD16Storage](int/simd16storage.md)
  Storage for a vector of 16 integers.
- [struct SIMD32Storage](int/simd32storage.md)
  Storage for a vector of 32 integers.
- [struct SIMD64Storage](int/simd64storage.md)
  Storage for a vector of 64 integers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/simd8storage)*