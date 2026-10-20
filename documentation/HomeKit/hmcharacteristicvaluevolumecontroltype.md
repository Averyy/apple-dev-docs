# HMCharacteristicValueVolumeControlType

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

Values for the type of volume control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum HMCharacteristicValueVolumeControlType
```

```c
enum HMCharacteristicValueVolumeControlType : NSInteger;
```

## Topics

### Volume types
- [HMCharacteristicValueVolumeControlType.absolute](./hmcharacteristicvaluevolumecontroltype/absolute.md)
  The volume sets to a specific level.
- [HMCharacteristicValueVolumeControlType.none](./hmcharacteristicvaluevolumecontroltype/none.md)
  The device doesn’t have volume control functionality.
- [HMCharacteristicValueVolumeControlType.relative](./hmcharacteristicvaluevolumecontroltype/relative.md)
  The volume adjusts incrementally, without taking the current level into consideration.
- [HMCharacteristicValueVolumeControlType.relativeWithCurrent](./hmcharacteristicvaluevolumecontroltype/relativewithcurrent.md)
  The volume adjusts incrementally, relative to current level.
### Initializers
- [init?(rawValue: Int)](./hmcharacteristicvaluevolumecontroltype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluevolumecontroltype)*