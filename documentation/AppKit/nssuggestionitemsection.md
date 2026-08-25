# NSSuggestionItemSection

**Framework**: AppKit  
**Kind**: struct

Describes a section of suggestions items in a suggestions menu

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct NSSuggestionItemSection<SuggestionItemType>
```

## Topics

### Initializers
- [init(items: [NSSuggestionItemSection<SuggestionItemType>.Item])](nssuggestionitemsection/init(items:).md)
- [init(title: String?, items: [NSSuggestionItemSection<SuggestionItemType>.Item])](nssuggestionitemsection/init(title:items:).md)
### Instance Properties
- [var items: [NSSuggestionItemSection<SuggestionItemType>.Item]](nssuggestionitemsection/items.md)
  The items that appear in this section
- [var title: String?](nssuggestionitemsection/title.md)
  The title of this section of items, or `nil` to have a untitled section of items
### Type Aliases
- [NSSuggestionItemSection.Item](nssuggestionitemsection/item.md)
  A suggestion item with the same suggestion item type as the section

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [var isAutomaticTextCompletionEnabled: Bool](nstextfield/isautomatictextcompletionenabled.md)
  A Boolean value that indicates whether the text field automatically completes text as the user types.
- [var suggestionsDelegate: (any NSTextSuggestionsDelegate)?](nstextfield/suggestionsdelegate.md)
  The delegate that provides text suggestions for the receiving text field and responds to the user highlighting and selecting items.
- [protocol NSTextSuggestionsDelegate](nstextsuggestionsdelegate.md)
  A protocol for suggestion delegates of text fields to conform to in order to provide text suggestions in response to the user typing.
- [struct NSSuggestionItem](nssuggestionitem.md)
  The items that appear in suggestion menus.
- [struct NSSuggestionItemResponse](nssuggestionitemresponse.md)
  Describes the result of a batch of suggestion items from a search


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemsection)*