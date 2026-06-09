# LowLevelDeformation.Descriptor.Renormalizing

**Framework**: RealityKit  
**Kind**: struct

The renormalization data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Renormalizing
```

## Topics

### Creating a descriptor
- [init(adjacenciesCount: Int, indexCount: Int)](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.struct/init(adjacenciescount:indexcount:).md)
  Creates a renormalizing descriptor.
### Accessing adjacency data
- [var adjacenciesCount: Int](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.struct/adjacenciescount.md)
  The total number of triangle-adjacency entries across all vertices.
### Instance Properties
- [var indexCount: Int](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.struct/indexcount.md)
  The number of indices in the triangle index buffer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var renormalizing: LowLevelDeformation.Descriptor.Renormalizing?](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.property.md)
  The renormalization configuration, or `nil` if renormalization is not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct/renormalizing-swift.struct)*