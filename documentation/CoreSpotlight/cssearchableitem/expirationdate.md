# expirationDate

**Framework**: Core Spotlight  
**Kind**: property

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

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Discussion

If you don’t set the [`expirationDate`](cssearchableitem/expirationdate.md) property appropriately, the system automatically expires the item after a period of time.

## See Also

- [var uniqueIdentifier: String](cssearchableitem/uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](cssearchableitem/domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](cssearchableitem/attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/expirationdate)*