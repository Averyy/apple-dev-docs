# JournalingSuggestionsPicker

**Framework**: Journaling Suggestions  
**Kind**: struct

A view that lists different types of recent events in a person’s life.

**Availability**:
- iOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency struct JournalingSuggestionsPicker<Label> where Label : View
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

This interface displays several grids of content that layout visual mementos, each representing unique, personal events that occur in a person’s life. It enables a person to reflect and choose a particular event as a topic for derivative work. For example, a workout can serve as the beginnings of a new journal entry or illustration.

The first time the picker appears, a modal sheet introduces the concept of journaling suggestions. After a person selects a suggestion in the picker, the system shares only the information associated with the chosen suggestion with your app.

For more information, see [`Presenting the suggestions picker and processing a selection`](presenting-the-suggestions-picker-and-processing-a-selection.md).

## Topics

### Creating a suggestions picker
- [init(label: () -> Label, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(label:oncompletion:).md)
  Creates a suggestions picker within the given view.
- [init(LocalizedStringKey, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(_:oncompletion:)-7uxov.md)
  Creates a suggestions picker with button text defined by the given localized string key.
- [init<S>(S, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(_:oncompletion:)-4e82p.md)
  Creates a suggestions picker with button text defined by the given string.
### Displaying a suggestions picker
- [var body: some View](journalingsuggestionspicker/body-swift.property.md)
  The content and behavior of the view.
### Type Aliases
- [JournalingSuggestionsPicker.Body](journalingsuggestionspicker/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](journalingsuggestionspicker/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct JournalingSuggestion](journalingsuggestion.md)
  High-level information about a suggestion that a person chooses in the journaling suggestions picker.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The scheduled configuration settings for your app.
- [protocol JournalingSuggestionAsset](journalingsuggestionasset.md)
  An interface for the content that the suggestions picker presents.
- [struct JournalingSuggestionPresentationToken](journalingsuggestionpresentationtoken.md)
  A token you use to modify the content of the presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker)*