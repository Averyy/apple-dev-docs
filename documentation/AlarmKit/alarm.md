# Alarm

**Framework**: AlarmKit  
**Kind**: struct

An object that describes an alarm that can alert once or on a repeating schedule.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct Alarm
```

#### Overview

The following is an example of a 10 second timer:

```swift
let configuration = AlarmManager.AlarmConfiguration(countdownDuration:
Alarm.CountdownDuration(preAlert: 10, postAlert: 10),
schedule: nil,
attributes: attributes,
secondaryIntent: repeatIntent,
sound: .default)
```

The following is an example of an alarm that includes a 9 minute snooze option and plays the default sound:

```swift
let configuration = AlarmManager.AlarmConfiguration(countdownDuration:
Alarm.CountdownDuration(preAlert: nil, postAlert: 9 * 60),
schedule: .relative(schedule),
attributes: attributes,
secondaryIntent: snoozeIntent,
sound: .default)
```

## Topics

### Defining a countdown duration
- [struct CountdownDuration](alarm/countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var countdownDuration: Alarm.CountdownDuration?](alarm/countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](alarm/id-swift.property.md)
  The unique identifier of the alarm.
- [Alarm.State](alarm/state-swift.enum.md)
  An enum that lists all possible states of an alarm.
- [var state: Alarm.State](alarm/state-swift.property.md)
  The current state of the alarm.
### Setting an alarm schedule
- [Alarm.Schedule](alarm/schedule-swift.enum.md)
  A list of all types of schedules that the framework supports.
- [var schedule: Alarm.Schedule?](alarm/schedule-swift.property.md)
  The schedule determines when the alarm alerts.
### Decoding
- [init(from: any Decoder) throws](alarm/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](alarm/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [typealias ID](alarm/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Scheduling an alarm with AlarmKit](scheduling-an-alarm-with-alarmkit.md)
  Create prominent alerts at specified dates for your iOS app.
- [class AlarmManager](alarmmanager.md)
  An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm)*