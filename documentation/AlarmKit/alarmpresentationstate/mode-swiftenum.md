# AlarmPresentationState.Mode

**Framework**: AlarmKit  
**Kind**: enum

A list of all modes the alarm can be in: either alert, countdown, or paused.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
enum Mode
```

#### Overview

This value is sent as part of [`AlarmPresentationState`](alarmpresentationstate.md) to the widget extension, so that it can produce the appropriate UI for the current state of the alarm.

## Topics

### Creating a countdown
- [AlarmPresentationState.Mode.Countdown](alarmpresentationstate/mode-swift.enum/countdown.md)
  An object that specifies a countdown is in progress.
- [case countdown(AlarmPresentationState.Mode.Countdown)](alarmpresentationstate/mode-swift.enum/countdown(_:).md)
  A mode indicating the alarm timer is active.
### Creating an alert
- [AlarmPresentationState.Mode.Alert](alarmpresentationstate/mode-swift.enum/alert.md)
  A value that indicates the current state of an alarm.
- [case alert(AlarmPresentationState.Mode.Alert)](alarmpresentationstate/mode-swift.enum/alert(_:).md)
  A mode indicating an alarm emits an alert.
### Pausing an alarm
- [AlarmPresentationState.Mode.Paused](alarmpresentationstate/mode-swift.enum/paused.md)
  An object that specifies the current state of the alarm is paused.
- [case paused(AlarmPresentationState.Mode.Paused)](alarmpresentationstate/mode-swift.enum/paused(_:).md)
  A mode indicating the alarm isn’t active.
### Decoding
- [init(from: any Decoder) throws](alarmpresentationstate/mode-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (AlarmPresentationState.Mode, AlarmPresentationState.Mode) -> Bool](alarmpresentationstate/mode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarmpresentationstate/mode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarmpresentationstate/mode-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarmpresentationstate/mode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarmpresentationstate/mode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(alarmID: Alarm.ID, mode: AlarmPresentationState.Mode)](alarmpresentationstate/init(alarmid:mode:).md)
  Creates an instance of an alarm state.
- [var alarmID: Alarm.ID](alarmpresentationstate/alarmid.md)
  The unique ID of the alarm.
- [var mode: AlarmPresentationState.Mode](alarmpresentationstate/mode-swift.property.md)
  The specific state of the alarm, either alerting, countdown, or paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum)*