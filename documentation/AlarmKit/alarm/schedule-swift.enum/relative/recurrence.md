# Alarm.Schedule.Relative.Recurrence

**Framework**: AlarmKit  
**Kind**: enum

Describes the cadence at which an alarm will repeat, if any.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
enum Recurrence
```

## Topics

### Recurring alarms
- [Alarm.Schedule.Relative.Recurrence.never](alarm/schedule-swift.enum/relative/recurrence/never.md)
  An alarm that never repeats.
- [Alarm.Schedule.Relative.Recurrence.weekly(_:)](alarm/schedule-swift.enum/relative/recurrence/weekly(_:).md)
  An alarm that repeats weekly, on the specified day.
### Decoding
- [init(from: any Decoder) throws](alarm/schedule-swift.enum/relative/recurrence/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (Alarm.Schedule.Relative.Recurrence, Alarm.Schedule.Relative.Recurrence) -> Bool](alarm/schedule-swift.enum/relative/recurrence/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarm/schedule-swift.enum/relative/recurrence/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarm/schedule-swift.enum/relative/recurrence/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarm/schedule-swift.enum/relative/recurrence/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarm/schedule-swift.enum/relative/recurrence/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var repeats: Alarm.Schedule.Relative.Recurrence](alarm/schedule-swift.enum/relative/repeats.md)
  The cadence at which the alarm repeats, if any.
- [var time: Alarm.Schedule.Relative.Time](alarm/schedule-swift.enum/relative/time-swift.property.md)
  The hour and minute at which the alarm alerts, relative to the device’s current timezone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/recurrence)*