# expirationDate

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The date after which the searchable item should no longer exist.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var expirationDate: Date! { get set }
```

```objc
@property (copy, null_resettable) NSDate * expirationDate;
```

## Mentions

- [Adding your app’s content to Spotlight indexes](../adding-your-app-s-content-to-spotlight-indexes.md)

#### Discussion

If you don’t set the [`expirationDate`](./expirationdate.md) property appropriately, the system automatically expires the item after a period of time.

## See Also

### Setting attributes on a searchable item
- [var uniqueIdentifier: String](./uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](./domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](./attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](../cssearchableitemattributeset.md) object.
- [var isUpdate: Bool](./isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.
- [var updateListenerOptions: CSSearchableItem.UpdateListenerOptions](./updatelisteneroptions-swift.property.md)
  The types of notifications to request from Spotlight.
- [CSSearchableItem.UpdateListenerOptions](./updatelisteneroptions-swift.struct.md)
  The options to generate summarization or prioritization information for a searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/expirationdate)*