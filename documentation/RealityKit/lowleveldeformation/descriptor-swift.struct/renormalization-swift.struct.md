# LowLevelDeformation.Descriptor.Renormalization

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The renormalization data dimensions for a [`LowLevelDeformation`](../../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Renormalization
```

## Topics

### Creating a descriptor
- [init(adjacenciesCount: Int, indexCount: Int)](./renormalization-swift.struct/init%28adjacenciescount,indexcount%29.md)
  Creates a renormalization descriptor.
### Accessing adjacency data
- [var adjacenciesCount: Int](./renormalization-swift.struct/adjacenciescount.md)
  The total number of triangle-adjacency entries across all vertices.
### Instance Properties
- [var indexCount: Int](./renormalization-swift.struct/indexcount.md)
  The number of indices in the triangle index buffer.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring renormalization
- [var renormalization: LowLevelDeformation.Descriptor.Renormalization?](./renormalization-swift.property.md)
  The renormalization configuration, or `nil` if renormalization is not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct/renormalization-swift.struct)*