# JournalingSuggestionsConfiguration.NotificationSchedule

**Framework**: Journaling Suggestions  
**Kind**: enum

The schedule configuration of Journaling Suggestions notifications.

**Availability**:
- iOS 26.0+ (Beta)

## Declaration

```swift
enum NotificationSchedule
```

## Topics

### Identifying a notification schedule
- [JournalingSuggestionsConfiguration.NotificationSchedule.custom](journalingsuggestionsconfiguration/notificationschedule-swift.enum/custom.md)
  The notifications are enabled and configured to a custom schedule.
- [JournalingSuggestionsConfiguration.NotificationSchedule.off](journalingsuggestionsconfiguration/notificationschedule-swift.enum/off.md)
  The notifications aren’t enabled or authorized for this app.
- [JournalingSuggestionsConfiguration.NotificationSchedule.smart](journalingsuggestionsconfiguration/notificationschedule-swift.enum/smart.md)
  The notifications are enabled and configured to a Smart schedule.
### Comparing schedule settings
- [static func == (JournalingSuggestionsConfiguration.NotificationSchedule, JournalingSuggestionsConfiguration.NotificationSchedule) -> Bool](journalingsuggestionsconfiguration/notificationschedule-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](journalingsuggestionsconfiguration/notificationschedule-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](journalingsuggestionsconfiguration/notificationschedule-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](journalingsuggestionsconfiguration/notificationschedule-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var notificationSchedule: JournalingSuggestionsConfiguration.NotificationSchedule?](journalingsuggestionsconfiguration/notificationschedule-swift.property.md)
  The notification schedule configured by the person using your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration/notificationschedule-swift.enum)*