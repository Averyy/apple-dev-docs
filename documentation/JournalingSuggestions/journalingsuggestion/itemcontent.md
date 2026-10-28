# JournalingSuggestion.ItemContent

**Framework**: Journaling Suggestions  
**Kind**: struct  
**Role**: Structure

A container for the information about a specific suggestion.

**Availability**:
- iOS 17.2+

## Declaration

```swift
struct ItemContent
```

## Mentions

- [Presenting the suggestions picker and processing a selection](../presenting-the-suggestions-picker-and-processing-a-selection.md)

## Overview

When a person selects an event in the [`JournalingSuggestionsPicker`](../journalingsuggestionspicker.md), the system invokes the `onCompletion` handler that your app declares for the picker and passes in a [`JournalingSuggestion`](../journalingsuggestion.md) instance. The journaling suggestion contains an array of structures of this type in its [`items`](./items.md) property. Each instance of this structure contains one or more concrete instances of [`JournalingSuggestionAsset`](../journalingsuggestionasset.md) that represent the selection in the picker.

## Topics

### Identifying item contents
- [var representations: [any JournalingSuggestionAsset.Type]](./itemcontent/representations.md)
  An array of content types that a particular suggestion includes.
### Accessing suggestion data by type
- [func content<Content>(forType: Content.Type) async throws -> Content?](./itemcontent/content%28fortype%29.md)
  Retrieves a suggestion’s contents by returning a structure specific to the given content type.
- [func hasContent<Content>(ofType: Content.Type) -> Bool](./itemcontent/hascontent%28oftype%29.md)
  Checks if the suggestion contains information for the given type.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Accessing suggestion data by type
- [let items: [JournalingSuggestion.ItemContent]](./items.md)
  The individual items that compose the suggestion’s content.
- [func content<Content>(forType: Content.Type) async -> [Content]](./content%28fortype%29.md)
  Searches a suggestion’s items for information of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/itemcontent)*