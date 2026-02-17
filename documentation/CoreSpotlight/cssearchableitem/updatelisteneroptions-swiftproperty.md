# updateListenerOptions

**Framework**: Core Spotlight  
**Kind**: property

The types of notifications to request from Spotlight.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var updateListenerOptions: CSSearchableItem.UpdateListenerOptions { get set }
```

## Mentions

- [Generating summary and priority data for indexed items](generating-summary-and-priority-data-for-indexed-items.md)

#### Discussion

As Spotlight indexes your app’s searchable items, it can notify your Spotlight delegate app extension when specific information becomes available. For example, Spotlight can notify your delegate when Apple Intelligence generates a summary for your items. Use this property to tell Spotlight which types of notifications you want to receive for this item.

For more information, see [`Generating summary and priority data for indexed items`](generating-summary-and-priority-data-for-indexed-items.md).

## See Also

- [var uniqueIdentifier: String](cssearchableitem/uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](cssearchableitem/domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](cssearchableitem/attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.
- [var expirationDate: Date!](cssearchableitem/expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.
- [CSSearchableItem.UpdateListenerOptions](cssearchableitem/updatelisteneroptions-swift.struct.md)
  The options to generate summarization or prioritization information for a searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/updatelisteneroptions-swift.property)*