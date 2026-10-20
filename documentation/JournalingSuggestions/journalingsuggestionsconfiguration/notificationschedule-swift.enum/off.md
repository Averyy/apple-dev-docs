# JournalingSuggestionsConfiguration.NotificationSchedule.off

**Framework**: Journaling Suggestions  
**Kind**: case  
**Role**: Case

An option that indicates the app doesn’t receive notifications.

**Availability**:
- iOS 26.0+

## Declaration

```swift
case off
```

## Mentions

- [Receiving journaling suggestions system notifications](../../receiving-journaling-suggestions-from-system-notifications.md)

#### Discussion

This value can mean one or more possible causes:

- Journaling Suggestions aren’t enabled in Settings.
- Your app isn’t a preferred journal app in Settings.
- Journaling Suggestions are on but notifications are off in Settings.
- Your app has incomplete notification setup (for example, it’s missing the [`JSNotificationURLFormat`](../../../BundleResources/information-property-list/jsnotificationurlformat.md) target property).

## See Also

### Identifying a notification schedule
- [JournalingSuggestionsConfiguration.NotificationSchedule.smart](./smart.md)
  An option that indicates the system personalizes the notification schedule for the person.
- [JournalingSuggestionsConfiguration.NotificationSchedule.custom](./custom.md)
  An option that indicates the person chooses a specific notification schedule in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration/notificationschedule-swift.enum/off)*