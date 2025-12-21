# JournalingSuggestionPresentationToken

**Framework**: Journaling Suggestions  
**Kind**: struct

A container for a Journaling Suggestion identifier.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct JournalingSuggestionPresentationToken
```

## Mentions

- [Receiving journaling suggestions system notifications](receiving-journaling-suggestions-from-system-notifications.md)

#### Overview

When your app receives a Journaling Suggestion notification, the system launches your app and provides an ID that refers to a specific suggestion from the notification.

Create an instance of this class and display a [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md) by passing the token to the `JournalingSuggestionsPicker/journalingSuggestionsPicker(isPresented:onCompletion:)` view modifier, which enables the picker to preload its contents with the notified suggestion.

## Topics

### Initializing a presentation token
- [init(suggestionIdentifier: UUID?)](journalingsuggestionpresentationtoken/init(suggestionidentifier:).md)
  Creates a token used to modify the content of JournalingSuggestionsPicker presentation.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Receiving journaling suggestions system notifications](receiving-journaling-suggestions-from-system-notifications.md)
  Register your app to receive journaling suggestions when a person taps a system notification.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The configuration for Journaling Suggestion notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionpresentationtoken)*