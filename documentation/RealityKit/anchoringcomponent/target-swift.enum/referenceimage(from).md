# AnchoringComponent.Target.referenceImage(from:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An anchor point attached to the image specified by an image anchoring source.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
case referenceImage(from: AnchoringComponent.ImageAnchoringSource)
```

## Discussion

> **Note**: macOS and tvOS apps don’t track this type of anchor.

## See Also

### Image and object anchor targets
- [AnchoringComponent.Target.image(group:name:)](./image%28group,name%29.md)
  An anchor point attached to the image specified by a group and a name in AR Resources.
- [AnchoringComponent.Target.object(group:name:)](./object%28group,name%29.md)
  An anchor point attached to the object specified by a group and a name in AR Resources.
- [case referenceObject(from: AnchoringComponent.ObjectAnchoringSource)](./referenceobject%28from%29.md)
  An anchor point attached to an object that matches the reference of an object anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/referenceimage(from:))*