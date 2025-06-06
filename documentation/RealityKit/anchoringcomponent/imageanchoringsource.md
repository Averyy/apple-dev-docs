# AnchoringComponent.ImageAnchoringSource

**Framework**: RealityKit  
**Kind**: struct

Defines the source of object anchoring target based on how it is created.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ImageAnchoringSource
```

## Topics

### Operators
- [static func == (AnchoringComponent.ImageAnchoringSource, AnchoringComponent.ImageAnchoringSource) -> Bool](anchoringcomponent/imageanchoringsource/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(URL, physicalSize: SIMD2<Float>)](anchoringcomponent/imageanchoringsource/init(_:physicalsize:).md)
  Creates the image anchoring source from image file URL.
- [init(group: String, name: String)](anchoringcomponent/imageanchoringsource/init(group:name:).md)
  Creates the image anchoring source by group and name in AR Resources.
### Instance Properties
- [var hashValue: Int](anchoringcomponent/imageanchoringsource/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anchoringcomponent/imageanchoringsource/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/imageanchoringsource/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [AnchoringComponent.ObjectAnchoringSource](anchoringcomponent/objectanchoringsource.md)
  Defines the source of object anchoring target based on how it is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/imageanchoringsource)*