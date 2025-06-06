# Float16.SIMD16Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of 16 floating-point values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct SIMD16Storage
```

## Topics

### Initializers
- [init()](float16/simd16storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](float16/simd16storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Float16](float16/simd16storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Float16.SIMD16Storage.Scalar](float16/simd16storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/simd16storage)*