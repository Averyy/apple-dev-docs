# AccessibilityEvents.RotorNavigation

**Framework**: RealityKit  
**Kind**: struct

An accessibility event associated with a rotor navigation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct RotorNavigation
```

## Topics

### Initializers
- [init(rotorType: AccessibilityComponent.RotorType, hostEntity: Entity, currentItem: Any?, searchDirection: UIAccessibilityCustomRotor.Direction, resultHandler: (Any) -> Void)](accessibilityevents/rotornavigation/init(rotortype:hostentity:currentitem:searchdirection:resulthandler:).md)
### Instance Properties
- [let currentItem: Any?](accessibilityevents/rotornavigation/currentitem.md)
  The current element of the search.
- [let hostEntity: Entity](accessibilityevents/rotornavigation/hostentity.md)
  The entity containing the component declaring support for this rotor type.
- [let resultHandler: (Any) -> Void](accessibilityevents/rotornavigation/resulthandler.md)
  The handler for the result of the current search. When observing RotorNavigation events
- [let rotorType: AccessibilityComponent.RotorType](accessibilityevents/rotornavigation/rotortype.md)
  The type of the rotor associated with the event.
- [let searchDirection: UIAccessibilityCustomRotor.Direction](accessibilityevents/rotornavigation/searchdirection.md)
  The direction in which to search.

## Relationships

### Conforms To
- [Event](event.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/accessibilityevents/rotornavigation)*