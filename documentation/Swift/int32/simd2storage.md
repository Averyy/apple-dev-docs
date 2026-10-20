# Int32.SIMD2Storage

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Storage for a vector of two integers.

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
- [init()](./simd2storage/init%28%29.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](./simd2storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Int32](./simd2storage/subscript%28_%29.md)
  Accesses the element at the specified index.
### Type Aliases
- [Int32.SIMD2Storage.Scalar](./simd2storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [SIMDStorage](../simdstorage.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/simd2storage)*