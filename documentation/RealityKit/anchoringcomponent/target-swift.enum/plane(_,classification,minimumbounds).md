# AnchoringComponent.Target.plane(_:classification:minimumBounds:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An anchor point attached to a real world surface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case plane(AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)
```

## Discussion

> **Note**: macOS and tvOS apps don’t track this type of anchor.

## See Also

### Basic anchor targets
- [AnchoringComponent.Target.world(transform:)](./world%28transform%29.md)
  An anchor point attached to a fixed position in the scene.
- [AnchoringComponent.Target.camera](./camera.md)
  An anchor point attached to the device’s camera.
- [AnchoringComponent.Target.anchor(identifier:)](./anchor%28identifier%29.md)
  An anchor point attached to the AR anchor with a given identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/plane(_:classification:minimumbounds:))*