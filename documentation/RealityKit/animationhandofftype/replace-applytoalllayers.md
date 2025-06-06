# replace(applyToAllLayers:)

**Framework**: RealityKit  
**Kind**: method

Keeps playing the current animation during the transition time and uses the value from that animation as the blend value for the transition to the new animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static func replace(applyToAllLayers: Bool = true) -> AnimationHandoffType
```

#### Discussion

If `applyToAllLayers` is `false`, the handoff only replaces current animations that have the same `layerId` as the `blendLayerOffset` parameter in the `playAnimation()` call.

If `applyToAllLayers` is `true`, the handoff replaces all animations regardless of the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationhandofftype/replace(applytoalllayers:))*