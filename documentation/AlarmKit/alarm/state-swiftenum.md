# Alarm.State

**Framework**: AlarmKit  
**Kind**: enum

An enum that lists all possible states of an alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
enum State
```

## Topics

### Setting alarm states
- [Alarm.State.alerting](alarm/state-swift.enum/alerting.md)
  The alarm is currently firing.
- [Alarm.State.countdown](alarm/state-swift.enum/countdown.md)
  The alarm is counting down to its alert time.
- [Alarm.State.paused](alarm/state-swift.enum/paused.md)
  A person paused the countdown.
- [Alarm.State.scheduled](alarm/state-swift.enum/scheduled.md)
  The alarm is scheduled and ready to alert at the appropriate time.
### Decoding
- [init(from: any Decoder) throws](alarm/state-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (Alarm.State, Alarm.State) -> Bool](alarm/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarm/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarm/state-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarm/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarm/state-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CountdownDuration](alarm/countdownduration-swift.struct.md)
  An object that defines the durations used in an alarm that has a countdown.
- [var countdownDuration: Alarm.CountdownDuration?](alarm/countdownduration-swift.property.md)
  The time left before an alert, in seconds.
- [var id: UUID](alarm/id-swift.property.md)
  The unique identifier of the alarm.
- [var state: Alarm.State](alarm/state-swift.property.md)
  The current state of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/state-swift.enum)*