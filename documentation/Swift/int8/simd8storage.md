# Int8.SIMD8Storage

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
- [init()](int8/simd8storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](int8/simd8storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Int8](int8/simd8storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [Int8.SIMD8Storage.Scalar](int8/simd8storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/simd8storage)*