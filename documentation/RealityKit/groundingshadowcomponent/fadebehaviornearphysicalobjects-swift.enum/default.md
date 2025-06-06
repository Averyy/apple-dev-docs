# GroundingShadowComponent.FadeBehaviorNearPhysicalObjects.default

**Framework**: RealityKit  
**Kind**: case

The default grounding shadow behavior for the device’s platform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
case `default`
```

#### Discussion

In visionOS, the default case is equivalent to [`GroundingShadowComponent.FadeBehaviorNearPhysicalObjects.fade`](groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.enum/fade.md) when the the system can detect the entity represents a UI; otherwise,[`GroundingShadowComponent.FadeBehaviorNearPhysicalObjects.constant`](groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.enum/constant.md).

In iOS, the default case is equivalent to [`GroundingShadowComponent.FadeBehaviorNearPhysicalObjects.constant`](groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.enum/constant.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent/fadebehaviornearphysicalobjects-swift.enum/default)*