# HMCharacteristicValuePositionState

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

Possible values for the position states of an accessory like a door, window, awning, or window covering.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HMCharacteristicValuePositionState
```

```c
enum HMCharacteristicValuePositionState : NSInteger;
```

## Topics

### Position States
- [HMCharacteristicValuePositionState.closing](./hmcharacteristicvaluepositionstate/closing.md)
  The position is moving towards minimum value.
- [HMCharacteristicValuePositionState.opening](./hmcharacteristicvaluepositionstate/opening.md)
  The position is moving towards maximum value.
- [HMCharacteristicValuePositionState.stopped](./hmcharacteristicvaluepositionstate/stopped.md)
  The accessory isn’t moving.
### Initializers
- [init?(rawValue: Int)](./hmcharacteristicvaluepositionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate)*