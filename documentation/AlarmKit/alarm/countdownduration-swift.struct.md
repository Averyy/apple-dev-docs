# Alarm.CountdownDuration

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

An object that defines the durations used in an alarm that has a countdown.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct CountdownDuration
```

## Overview

Provide the countdown duration in seconds.

```swift
Alarm.CountdownDuration(preAlert: 10, postAlert: 10)
```

## Topics

### Creating a countdown duration
- [init(preAlert: TimeInterval?, postAlert: TimeInterval?)](./countdownduration-swift.struct/init%28prealert,postalert%29.md)
  Creates an instance of a countdown duration.
- [var postAlert: TimeInterval?](./countdownduration-swift.struct/postalert.md)
  The duration applied after the alarm has alerted at least once and moves back to the countdown state.
- [var preAlert: TimeInterval?](./countdownduration-swift.struct/prealert.md)
  The duration applied before the alarm fires.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Defining a countdown duration
- [var countdownDuration: Alarm.CountdownDuration?](./countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](./id.md)
  The unique identifier of the alarm.
- [Alarm.State](./state-swift.enum.md)
  An enum that lists all possible states of an alarm.
- [var state: Alarm.State](./state-swift.property.md)
  The current state of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/countdownduration-swift.struct)*