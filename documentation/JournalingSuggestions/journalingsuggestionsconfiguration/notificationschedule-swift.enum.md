# JournalingSuggestionsConfiguration.NotificationSchedule

**Framework**: Journaling Suggestions  
**Kind**: enum  
**Role**: Enumeration

Possible values for the Journaling Suggestions notifications setting.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum NotificationSchedule
```

## Overview

When [`notificationSchedule`](./notificationschedule-swift.property.md) is [`JournalingSuggestionsConfiguration.NotificationSchedule.smart`](./notificationschedule-swift.enum/smart.md), the system personalizes the schedule according to the person’s unique routines. The value is [`JournalingSuggestionsConfiguration.NotificationSchedule.custom`](./notificationschedule-swift.enum/custom.md) if the person chooses a specific schedule in Settings.

An [`JournalingSuggestionsConfiguration.NotificationSchedule.off`](./notificationschedule-swift.enum/off.md) value can mean:

- Journaling Suggestions aren’t enabled in Settings.
- Your app isn’t a preferred journal app in Settings.
- Journaling Suggestions are on but notifications are off in Settings.
- Your app has incomplete notification setup (for example, it’s missing the [`JSNotificationURLFormat`](../../BundleResources/information-property-list/jsnotificationurlformat.md) target property).

For more information on notifications, see [Receiving journaling suggestions system notifications](../receiving-journaling-suggestions-from-system-notifications.md).

## Topics

### Identifying a notification schedule
- [JournalingSuggestionsConfiguration.NotificationSchedule.smart](./notificationschedule-swift.enum/smart.md)
  An option that indicates the system personalizes the notification schedule for the person.
- [JournalingSuggestionsConfiguration.NotificationSchedule.custom](./notificationschedule-swift.enum/custom.md)
  An option that indicates the person chooses a specific notification schedule in Settings.
- [JournalingSuggestionsConfiguration.NotificationSchedule.off](./notificationschedule-swift.enum/off.md)
  An option that indicates the app doesn’t receive notifications.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Inspecting the notification schedule
- [var notificationSchedule: JournalingSuggestionsConfiguration.NotificationSchedule?](./notificationschedule-swift.property.md)
  The schedule for Journaling Suggestion notifications, as it resides in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration/notificationschedule-swift.enum)*