# JournalingSuggestionPresentationToken

**Framework**: Journaling Suggestions  
**Kind**: struct

A token you use to modify the content of the presentation.

**Availability**:
- iOS 26.0+ (Beta)

## Declaration

```swift
struct JournalingSuggestionPresentationToken
```

## Topics

### Initializing a presentation token
- [init(suggestionIdentifier: UUID?)](journalingsuggestionpresentationtoken/init(suggestionidentifier:).md)
  Creates a token used to modify the content of JournalingSuggestionsPicker presentation.
### Comparing tokens
- [static func == (JournalingSuggestionPresentationToken, JournalingSuggestionPresentationToken) -> Bool](journalingsuggestionpresentationtoken/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](journalingsuggestionpresentationtoken/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct JournalingSuggestionsPicker](journalingsuggestionspicker.md)
  A view that lists different types of recent events in a person’s life.
- [struct JournalingSuggestion](journalingsuggestion.md)
  High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The scheduled configuration settings for your app.
- [protocol JournalingSuggestionAsset](journalingsuggestionasset.md)
  An interface for the content that the suggestions picker presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionpresentationtoken)*