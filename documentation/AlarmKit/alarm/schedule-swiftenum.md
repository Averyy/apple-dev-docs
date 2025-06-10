# Alarm.Schedule

**Framework**: AlarmKit  
**Kind**: enum

A list of all types of schedules that the framework supports.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
enum Schedule
```

## Topics

### Setting an alarm schedule
- [Alarm.Schedule.Relative](alarm/schedule-swift.enum/relative.md)
  An object that describes when an alarm alerts, relative to the device’s timezone.
- [Alarm.Schedule.fixed(_:)](alarm/schedule-swift.enum/fixed(_:).md)
  A one-shot alarm that fires at a specific time, not a time relative to the current time zone.
- [case relative(Alarm.Schedule.Relative)](alarm/schedule-swift.enum/relative(_:).md)
  An alarm that can repeat and fire at a time relative to the device’s current time zone.
### Decoding
- [init(from: any Decoder) throws](alarm/schedule-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (Alarm.Schedule, Alarm.Schedule) -> Bool](alarm/schedule-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarm/schedule-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarm/schedule-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarm/schedule-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarm/schedule-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var schedule: Alarm.Schedule?](alarm/schedule-swift.property.md)
  The schedule determines when the alarm alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum)*