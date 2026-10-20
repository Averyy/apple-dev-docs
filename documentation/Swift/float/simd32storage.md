# Float.SIMD32Storage

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Storage for a vector of 32 floating-point values.

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
struct SIMD32Storage
```

## Topics

### Initializers
- [init()](./simd32storage/init%28%29.md)
  Creates a vector with zero in all lanes.
### Instance Properties
- [var scalarCount: Int](./simd32storage/scalarcount.md)
  The number of scalars, or elements, in the vector.
### Subscripts
- [subscript(Int) -> Float](./simd32storage/subscript%28_%29.md)
  Accesses the element at the specified index.
### Type Aliases
- [Float.SIMD32Storage.Scalar](./simd32storage/scalar.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [SIMDStorage](../simdstorage.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### SIMD-Supporting Types
- [typealias SIMDMaskScalar](./simdmaskscalar.md)
- [struct SIMD2Storage](./simd2storage.md)
  Storage for a vector of two floating-point values.
- [struct SIMD4Storage](./simd4storage.md)
  Storage for a vector of four floating-point values.
- [struct SIMD8Storage](./simd8storage.md)
  Storage for a vector of eight floating-point values.
- [struct SIMD16Storage](./simd16storage.md)
  Storage for a vector of 16 floating-point values.
- [struct SIMD64Storage](./simd64storage.md)
  Storage for a vector of 64 floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/simd32storage)*