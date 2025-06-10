# AnchoringComponent.PhysicsSimulation.none

**Framework**: RealityKit  
**Kind**: case

Opts out the entity and its descendants from having their own physics space.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case none
```

#### Discussion

`none` implies the anchor entity does not have its own physics simulation.

It will use the regular rules to determine which physics simulation the entity is a part of. For more about the rules, please check [`PhysicsSimulationComponent`](physicssimulationcomponent.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/physicssimulation-9f9sg/none)*