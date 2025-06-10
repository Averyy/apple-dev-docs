# UInt.SIMD16Storage

**Framework**: Swift  
**Kind**: struct

Storage for a vector of 16 integers.

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
struct SIMD16Storage
```

## Topics

### Initializers
- [init()](uint/simd16storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](uint/simd16storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> UInt](uint/simd16storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [UInt.SIMD16Storage.Scalar](uint/simd16storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/simd16storage)*