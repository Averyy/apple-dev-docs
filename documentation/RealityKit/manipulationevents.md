# ManipulationEvents

**Framework**: RealityKit  
**Kind**: enum

Events that occur while a person manipulates an entity.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ManipulationEvents
```

#### Overview

You can subscribe to these events using [`subscribe(to:on:_:)`](realityviewcontentprotocol/subscribe(to:on:_:).md). For example, you can change the color of an entity’s material when the manipulation gesture begins and ends.

```swift
_ = content.subscribe(to: ManipulationEvents.WillBegin.self) { event in
    event.entity.components[ModelComponent.self]?.materials[0] = SimpleMaterial(color: .blue, isMetallic: false)
}
_ = content.subscribe(to: ManipulationEvents.WillEnd.self)  { event in
    event.entity.components[ModelComponent.self]?.materials[0] = SimpleMaterial(color: .red, isMetallic: false)
}
```

## Topics

### Detecting manipulation gesture events
- [ManipulationEvents.WillBegin](manipulationevents/willbegin.md)
  A event triggered when an interaction is about to begin on a `ManipulationComponent`’s entity.
- [ManipulationEvents.DidUpdateTransform](manipulationevents/didupdatetransform.md)
  An event triggered when an entity’s transform was updated during a `ManipulationComponent`.
- [ManipulationEvents.DidHandOff](manipulationevents/didhandoff.md)
  An event triggered when the object is directly handed off from one hand to another
- [ManipulationEvents.WillRelease](manipulationevents/willrelease.md)
  A event triggered when an entity was released.
- [ManipulationEvents.WillEnd](manipulationevents/willend.md)
  An event triggered when the object has reached its destination and will no longer be updated.
### Type Aliases
- [ManipulationEvents.InputDeviceSet](manipulationevents/inputdeviceset.md)

## See Also

- [enum AccessibilityEvents](accessibilityevents.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/manipulationevents)*