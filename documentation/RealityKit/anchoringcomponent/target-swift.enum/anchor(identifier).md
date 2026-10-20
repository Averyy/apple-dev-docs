# AnchoringComponent.Target.anchor(identifier:)

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

An anchor point attached to the AR anchor with a given identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+

## Declaration

```swift
case anchor(identifier: UUID)
```

## See Also

### Basic anchor targets
- [AnchoringComponent.Target.world(transform:)](./world%28transform%29.md)
  An anchor point attached to a fixed position in the scene.
- [case plane(AnchoringComponent.Target.Alignment, classification: AnchoringComponent.Target.Classification, minimumBounds: SIMD2<Float>)](./plane%28_,classification,minimumbounds%29.md)
  An anchor point attached to a real world surface.
- [AnchoringComponent.Target.camera](./camera.md)
  An anchor point attached to the device’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/target-swift.enum/anchor(identifier:))*