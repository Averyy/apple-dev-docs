# content(forType:)

**Framework**: Journalingsuggestions  
**Kind**: method

Retrieves a suggestion’s contents by returning a structure specific to the given content type.

**Availability**:
- iOS 17.2+

## Declaration

```swift
func content<Content>(forType content: Content.Type) async throws -> Content? where Content : JournalingSuggestionAsset
```

#### Return Value

An instance of the requested type, if it exists in the suggestion.

#### Discussion

The framework templates this method, where `Content` is [`JournalingSuggestionAsset`](journalingsuggestionasset.md), because the `content` argument is a `Type` rather than an enumeration case, or other primitive.

> **Note**: An error if the journaling suggestions picker encounters an unexpected issue.

## Parameters

- `content`: A type conforming to   protocol.

## See Also

- [func hasContent<Content>(ofType: Content.Type) -> Bool](journalingsuggestion/itemcontent/hascontent(oftype:).md)
  Checks if the suggestion contains information for the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/itemcontent/content(fortype:))*