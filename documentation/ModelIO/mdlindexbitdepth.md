# MDLIndexBitDepth

**Framework**: Model I/O  
**Kind**: enum

Options for the size of integer data in a submesh’s index buffer, used by the [`indexType`](mdlsubmesh/indextype.md) property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLIndexBitDepth
```

#### Overview

For optimum performance, an index buffer should generally use the smallest data type that fits the number of indices it contains.

## Topics

### Constants
- [MDLIndexBitDepth.invalid](mdlindexbitdepth/invalid.md)
  The submesh has not been initialized or its data type is unknown.
- [MDLIndexBitDepth.uInt8](mdlindexbitdepth/uint8-swift.enum.case.md)
  Each index in the submesh’s index buffer is an 8-bit integer.
- [MDLIndexBitDepth.uInt16](mdlindexbitdepth/uint16-swift.enum.case.md)
  Each index in the submesh’s index buffer is a 16-bit integer.
- [MDLIndexBitDepth.uInt32](mdlindexbitdepth/uint32-swift.enum.case.md)
  Each index in the submesh’s index buffer is a 32-bit integer.
### Initializers
- [init?(rawValue: UInt)](mdlindexbitdepth/init(rawvalue:).md)
### Type Properties
- [static var uint16: MDLIndexBitDepth](mdlindexbitdepth/uint16-swift.type.property.md)
- [static var uint32: MDLIndexBitDepth](mdlindexbitdepth/uint32-swift.type.property.md)
- [static var uint8: MDLIndexBitDepth](mdlindexbitdepth/uint8-swift.type.property.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MDLGeometryType](mdlgeometrytype.md)
  Types of geometric primitives for rendering a submesh, used by the [`geometryType`](mdlsubmesh/geometrytype.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlindexbitdepth)*