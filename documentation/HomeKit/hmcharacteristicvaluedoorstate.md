# HMCharacteristicValueDoorState

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

Possible values for the state of a door.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HMCharacteristicValueDoorState
```

```c
enum HMCharacteristicValueDoorState : NSInteger;
```

## Topics

### Door States
- [HMCharacteristicValueDoorState.open](./hmcharacteristicvaluedoorstate/open.md)
  The door is fully open.
- [HMCharacteristicValueDoorState.closed](./hmcharacteristicvaluedoorstate/closed.md)
  The door is fully closed.
- [HMCharacteristicValueDoorState.opening](./hmcharacteristicvaluedoorstate/opening.md)
  The door is actively opening.
- [HMCharacteristicValueDoorState.closing](./hmcharacteristicvaluedoorstate/closing.md)
  The door is actively closing.
- [HMCharacteristicValueDoorState.stopped](./hmcharacteristicvaluedoorstate/stopped.md)
  The door is not moving, and is neither fully open nor fully closed.
### Initializers
- [init?(rawValue: Int)](./hmcharacteristicvaluedoorstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate)*