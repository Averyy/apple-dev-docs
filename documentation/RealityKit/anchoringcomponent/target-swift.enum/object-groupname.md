# AnchoringComponent.Target.object(group:name:)

**Framework**: RealityKit  
**Kind**: case

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

#### Discussion

> **Note**: macOS, visionOS and tvOS apps don’t track this type of anchor.

## See Also

- [AnchoringComponent.Target.image(group:name:)](anchoringcomponent/target-swift.enum/image(group:name:).md)
  An anchor point attached to the image specified by a group and a name in AR Resources.
- [case referenceImage(from: AnchoringComponent.ImageAnchoringSource)](anchoringcomponent/target-swift.enum/referenceimage(from:).md)
  An anchor point attached to the image specified by an image anchoring source.
- [case referenceObject(from: AnchoringComponent.ObjectAnchoringSource)](anchoringcomponent/target-swift.enum/referenceobject(from:).md)
  An anchor point attached to an object that matches the reference of an object anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/object(group:name:))*