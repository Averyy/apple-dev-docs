# Alarm.Schedule.Relative.Time

**Framework**: AlarmKit  
**Kind**: struct

An object that describes the hour and minute at which an alarm alerts.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
struct Time
```

## Topics

### Creating a scheduled time
- [init(hour: Int, minute: Int)](alarm/schedule-swift.enum/relative/time-swift.struct/init(hour:minute:).md)
  Creates an instance of time.
- [var hour: Int](alarm/schedule-swift.enum/relative/time-swift.struct/hour.md)
  The hour mark the alarm alerts.
- [var minute: Int](alarm/schedule-swift.enum/relative/time-swift.struct/minute.md)
  The minute of the hour the alarm alerts.
### Decoding
- [init(from: any Decoder) throws](alarm/schedule-swift.enum/relative/time-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (Alarm.Schedule.Relative.Time, Alarm.Schedule.Relative.Time) -> Bool](alarm/schedule-swift.enum/relative/time-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarm/schedule-swift.enum/relative/time-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarm/schedule-swift.enum/relative/time-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarm/schedule-swift.enum/relative/time-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarm/schedule-swift.enum/relative/time-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(time: Alarm.Schedule.Relative.Time, repeats: Alarm.Schedule.Relative.Recurrence)](alarm/schedule-swift.enum/relative/init(time:repeats:).md)
  Creates an alarm that alerts at a specific 


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarm/schedule-swift.enum/relative/time-swift.struct)*