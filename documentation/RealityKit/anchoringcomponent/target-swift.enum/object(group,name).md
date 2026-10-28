# AnchoringComponent.Target.object(group:name:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An anchor point attached to the object specified by a group and a name in AR Resources.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
case object(group: String, name: String)
```

## Discussion

> **Note**: macOS, visionOS and tvOS apps don’t track this type of anchor.

## See Also

### Image and object anchor targets
- [AnchoringComponent.Target.image(group:name:)](./image%28group,name%29.md)
  An anchor point attached to the image specified by a group and a name in AR Resources.
- [case referenceImage(from: AnchoringComponent.ImageAnchoringSource)](./referenceimage%28from%29.md)
  An anchor point attached to the image specified by an image anchoring source.
- [case referenceObject(from: AnchoringComponent.ObjectAnchoringSource)](./referenceobject%28from%29.md)
  An anchor point attached to an object that matches the reference of an object anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/object(group:name:))*