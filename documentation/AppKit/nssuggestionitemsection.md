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
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemsection)*