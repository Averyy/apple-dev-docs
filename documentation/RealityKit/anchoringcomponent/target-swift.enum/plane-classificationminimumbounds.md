# AnchoringComponent.Target.plane(_:classification:minimumBounds:)

**Framework**: RealityKit  
**Kind**: case

An anchor point attached to a real world surface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case plane(AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)
```

#### Discussion

> **Note**: macOS and tvOS apps don’t track this type of anchor.

## See Also

- [AnchoringComponent.Target.world(transform:)](anchoringcomponent/target-swift.enum/world(transform:).md)
  An anchor point attached to a fixed position in the scene.
- [AnchoringComponent.Target.camera](anchoringcomponent/target-swift.enum/camera.md)
  An anchor point attached to the device’s camera.
- [AnchoringComponent.Target.anchor(identifier:)](anchoringcomponent/target-swift.enum/anchor(identifier:).md)
  An anchor point attached to the AR anchor with a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/plane(_:classification:minimumbounds:))*