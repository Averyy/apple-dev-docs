# AnchoringComponent.ObjectAnchoringSource

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Defines the source of object anchoring target based on how it is created.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ObjectAnchoringSource
```

## Topics

### Creating an object anchoring source
- [init(referenceObject: Data)](./objectanchoringsource/init%28referenceobject%29.md)
  Creates the object anchoring source by reference object file data.
### Initializers
- [init(URL)](./objectanchoringsource/init%28_%29.md)
  Creates the object anchoring source by reference object file URL.
- [init(group: String, name: String)](./objectanchoringsource/init%28group,name%29.md)
  Creates the object anchoring source by group and name in AR Resources.
- [init(name: String, in: Bundle)](./objectanchoringsource/init%28name,in%29.md)
  Creates the object anchoring source by reference object file asset with provided name and bundle.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Image and object tracking
- [AnchoringComponent.ImageAnchoringSource](./imageanchoringsource.md)
  Defines the source of image anchoring target based on how it is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/objectanchoringsource)*