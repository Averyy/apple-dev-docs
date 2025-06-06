# JournalingSuggestion.ItemContent

**Framework**: Journaling Suggestions  
**Kind**: struct

A container for the information about a specific suggestion.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct ItemContent
```

## Mentions

- [Presenting the suggestions picker and processing a selection](presenting-the-suggestions-picker-and-processing-a-selection.md)

#### Overview

When a person selects an event in the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md), the system invokes the `onCompletion` handler that your app declares for the picker and passes in a [`JournalingSuggestion`](journalingsuggestion.md) instance. The journaling suggestion contains an array of structures of this type in its [`items`](journalingsuggestion/items.md) property. Each instance of this structure contains one or more concrete instances of [`JournalingSuggestionAsset`](journalingsuggestionasset.md) that represent the selection in the picker.

## Topics

### Identifying item contents
- [var id: UUID](journalingsuggestion/itemcontent/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [var representations: [any JournalingSuggestionAsset.Type]](journalingsuggestion/itemcontent/representations.md)
  An array of content types that a particular suggestion includes.
### Accessing suggestion data by type
- [func content<Content>(forType: Content.Type) async throws -> Content?](journalingsuggestion/itemcontent/content(fortype:).md)
  Retrieves a suggestion’s contents by returning a structure specific to the given content type.
- [func hasContent<Content>(ofType: Content.Type) -> Bool](journalingsuggestion/itemcontent/hascontent(oftype:).md)
  Checks if the suggestion contains information for the given type.
### Type Aliases
- [JournalingSuggestion.ItemContent.ID](journalingsuggestion/itemcontent/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [let items: [JournalingSuggestion.ItemContent]](journalingsuggestion/items.md)
  The individual items that compose the suggestion’s content.
- [func content<Content>(forType: Content.Type) async -> [Content]](journalingsuggestion/content(fortype:).md)
  Searches a suggestion’s items for information of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/itemcontent)*