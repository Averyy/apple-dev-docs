# snapshotAndReplace(applyToAllLayers:)

**Framework**: RealityKit  
**Kind**: method

Stops the current animation and uses the current value of that animation as the blend value for the transition to the new animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func snapshotAndReplace(applyToAllLayers: Bool = true) -> AnimationHandoffType
```

#### Discussion

If `applyToAllLayers` is `false`, the handoff only replaces current animations that have the same `layerId` as the `blendLayerOffset` parameter in the `playAnimation()` call.

If `applyToAllLayers` is `true`, the handoff replaces all animations regardless of the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationhandofftype/snapshotandreplace(applytoalllayers:))*