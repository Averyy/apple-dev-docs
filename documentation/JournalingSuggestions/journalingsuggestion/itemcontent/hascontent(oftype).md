# hasContent(ofType:)

**Framework**: Journaling Suggestions  
**Kind**: method

Checks if the suggestion contains information for the given type.

**Availability**:
- iOS 17.2+

## Declaration

```swift
func hasContent<Content>(ofType content: Content.Type) -> Bool where Content : JournalingSuggestionAsset
```

#### Return Value

`true`, if the suggestion contains information for the given type; otherwise, `false`.

#### Discussion

The framework templates this method, where `Content` is [`JournalingSuggestionAsset`](journalingsuggestionasset.md), because the `content` argument is a `Type` rather than an enumeration case, or other primitive.

## Parameters

- `content`: The type of information to check for.

## See Also

- [func content<Content>(forType: Content.Type) async throws -> Content?](journalingsuggestion/itemcontent/content(fortype:).md)
  Retrieves a suggestion’s contents by returning a structure specific to the given content type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/itemcontent/hascontent(oftype:))*