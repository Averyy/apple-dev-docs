# JournalingSuggestionsConfiguration.NotificationSchedule

**Framework**: Journaling Suggestions  
**Kind**: enum

Possible values for the Journaling Suggestions notifications setting.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum NotificationSchedule
```

#### Overview

When [`notificationSchedule`](journalingsuggestionsconfiguration/notificationschedule-swift.property.md) is [`JournalingSuggestionsConfiguration.NotificationSchedule.smart`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/smart.md), the system personalizes the schedule according to the person’s unique routines. The value is [`JournalingSuggestionsConfiguration.NotificationSchedule.custom`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/custom.md) if the person chooses a specific schedule in Settings.

An [`JournalingSuggestionsConfiguration.NotificationSchedule.off`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/off.md) value can mean:

- Journaling Suggestions aren’t enabled in Settings.
- Your app isn’t a preferred journal app in Settings.
- Journaling Suggestions are on but notifications are off in Settings.
- Your app has incomplete notification setup (for example, it’s missing the [`JSNotificationURLFormat`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat) target property).

For more information on notifications, see [`Receiving journaling suggestions system notifications`](receiving-journaling-suggestions-from-system-notifications.md).

## Topics

### Identifying a notification schedule
- [JournalingSuggestionsConfiguration.NotificationSchedule.smart](journalingsuggestionsconfiguration/notificationschedule-swift.enum/smart.md)
  An option that indicates the system personalizes the notification schedule for the person.
- [JournalingSuggestionsConfiguration.NotificationSchedule.custom](journalingsuggestionsconfiguration/notificationschedule-swift.enum/custom.md)
  An option that indicates the person chooses a specific notification schedule in Settings.
- [JournalingSuggestionsConfiguration.NotificationSchedule.off](journalingsuggestionsconfiguration/notificationschedule-swift.enum/off.md)
  An option that indicates the app doesn’t receive notifications.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var notificationSchedule: JournalingSuggestionsConfiguration.NotificationSchedule?](journalingsuggestionsconfiguration/notificationschedule-swift.property.md)
  The schedule for Journaling Suggestion notifications, as it resides in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration/notificationschedule-swift.enum)*