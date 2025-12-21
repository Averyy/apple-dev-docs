# JournalingSuggestionsConfiguration

**Framework**: Journaling Suggestions  
**Kind**: class

The configuration for Journaling Suggestion notifications.

**Availability**:
- iOS 26.0+

## Declaration

```swift
class JournalingSuggestionsConfiguration
```

## Mentions

- [Receiving journaling suggestions system notifications](receiving-journaling-suggestions-from-system-notifications.md)

#### Overview

Create an instance of this class and refer to [`notificationSchedule`](journalingsuggestionsconfiguration/notificationschedule-swift.property.md), which provides a read-only view of the Journaling Suggestion notification configuration, as it resides in Settings.

## Topics

### Initializing a configuration
- [init()](journalingsuggestionsconfiguration/init.md)
  Creates an empty configuration object.
### Inspecting the notification schedule
- [var notificationSchedule: JournalingSuggestionsConfiguration.NotificationSchedule?](journalingsuggestionsconfiguration/notificationschedule-swift.property.md)
  The schedule for Journaling Suggestion notifications, as it resides in Settings.
- [JournalingSuggestionsConfiguration.NotificationSchedule](journalingsuggestionsconfiguration/notificationschedule-swift.enum.md)
  Possible values for the Journaling Suggestions notifications setting.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)

## See Also

- [Receiving journaling suggestions system notifications](receiving-journaling-suggestions-from-system-notifications.md)
  Register your app to receive journaling suggestions when a person taps a system notification.
- [struct JournalingSuggestionPresentationToken](journalingsuggestionpresentationtoken.md)
  A container for a Journaling Suggestion identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration)*