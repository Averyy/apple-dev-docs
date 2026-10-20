# content(forType:)

**Framework**: Journaling Suggestions  
**Kind**: method  
**Role**: Instance Method

Searches a suggestion’s items for information of the given type.

**Availability**:
- iOS 17.2+

## Declaration

```swift
func content<Content>(forType content: Content.Type) async -> [Content] where Content : JournalingSuggestionAsset
```

#### Return Value

An array that contains elements of the requested type, if they exist in the suggestion.

#### Discussion

The framework templates this method, where `Content` is [`JournalingSuggestionAsset`](../journalingsuggestionasset.md), because the `content` argument is a `Type` rather than an enumeration case, or other primitive.

> **Throws**: An error if the journaling suggestions picker encounters an unexpected issue.

## Parameters

- `content`: A type that conforms to the [`JournalingSuggestionAsset`](../journalingsuggestionasset.md) protocol.

## See Also

### Accessing suggestion data by type
- [let items: [JournalingSuggestion.ItemContent]](./items.md)
  The individual items that compose the suggestion’s content.
- [JournalingSuggestion.ItemContent](./itemcontent.md)
  A container for the information about a specific suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/content(fortype:))*