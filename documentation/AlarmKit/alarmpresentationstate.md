# AlarmPresentationState

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the mutable content of the alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct AlarmPresentationState
```

#### Overview

This structure includes alerting, countdown, and paused states. Live Activities consists of two types of information: immutable attributes and mutable content. For example, in a live activity that’s showing the score of a soccer game the immutable attributes are the names of the teams involved in the game and the mutable content is the current score.

For alarms, immutable content is information you supply through your own processes, including information such as the tint color and the snooze button label. While mutable content comes from AlarmKit and contains information from the system, such as the alarm alert date and the alarm mode.

## Topics

### Creating an alarm state
- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](alarmpresentationstate/init(alarmid:mode:).md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](alarmpresentationstate/alarmid.md)
  The unique ID of the alarm.
- [var mode: AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.
- [AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.enum.md)
  A list of all modes the alarm can be in: either alert, countdown, or paused.
### Decoding
- [init(from: any Decoder) throws](alarmpresentationstate/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (AlarmPresentationState, AlarmPresentationState) -> Bool](alarmpresentationstate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarmpresentationstate/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarmpresentationstate/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarmpresentationstate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarmpresentationstate/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AlarmPresentation](alarmpresentation.md)
  An object that describes the content required for the alarm UI.
- [struct AlarmAttributes](alarmattributes.md)
  An object that contains all information necessary for the alarm UI.
- [protocol AlarmMetadata](alarmmetadata.md)
  A metadata object that contains information about an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate)*