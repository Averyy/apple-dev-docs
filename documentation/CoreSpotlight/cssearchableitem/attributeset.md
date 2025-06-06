# attributeSet

**Framework**: Core Spotlight  
**Kind**: property

The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var attributeSet: CSSearchableItemAttributeSet { get set }
```

## See Also

- [var uniqueIdentifier: String](cssearchableitem/uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](cssearchableitem/domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var expirationDate: Date!](cssearchableitem/expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/attributeset)*