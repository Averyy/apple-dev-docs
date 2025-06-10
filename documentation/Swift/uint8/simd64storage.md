# UInt8.SIMD64Storage

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
- [init()](uint8/simd64storage/init.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](uint8/simd64storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> UInt8](uint8/simd64storage/subscript(_:).md)
  Accesses the element at the specified index.
### Type Aliases
- [UInt8.SIMD64Storage.Scalar](uint8/simd64storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [SIMDStorage](simdstorage.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/simd64storage)*