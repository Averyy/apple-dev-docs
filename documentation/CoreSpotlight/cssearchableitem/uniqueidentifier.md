# uniqueIdentifier

**Framework**: Core Spotlight  
**Kind**: property

The value that uniquely identifies the searchable item within your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var uniqueIdentifier: String { get set }
```

#### Discussion

This property is required because it’s the only way to identify searchable items in the index when you need to access or delete them. When you create a searchable item, the system generates a UUID by default, but you can replace the default value with a unique identifier that makes sense in the context of your app. If you want to use a custom value for [`uniqueIdentifier`](cssearchableitem/uniqueidentifier.md), be sure to set it before the item is indexed for the first time.

## See Also

- [var domainIdentifier: String?](cssearchableitem/domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](cssearchableitem/attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.
- [var expirationDate: Date!](cssearchableitem/expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/uniqueidentifier)*