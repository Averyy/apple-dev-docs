# domainIdentifier

**Framework**: Core Spotlight  
**Kind**: property

An optional identifier that represents the domain or owner of the item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var domainIdentifier: String? { get set }
```

#### Discussion

Specify a domain identifier to group items together and to make it easy to delete groups of items from the index. For example, you might specify an identifier for a mailbox in an account whose indexed data you want to remove when the account is deleted. In this example, [`domainIdentifier`](cssearchableitem/domainidentifier.md) should be of the form `<account-id>.<mailbox-id>`, where neither `<account-id>` nor `<mailbox-id>` contain periods. To delete all items associated with the specified account and mailbox, you can call [`deleteSearchableItems(withDomainIdentifiers:completionHandler:)`](cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:).md) with a [`domainIdentifier`](cssearchableitem/domainidentifier.md) of `<account-id>.<mailbox-id>`. Or to delete all items associated with all mailboxes in the specified account, you can call [`deleteSearchableItems(withDomainIdentifiers:completionHandler:)`](cssearchableindex/deletesearchableitems(withdomainidentifiers:completionhandler:).md) with a [`domainIdentifier`](cssearchableitem/domainidentifier.md) of `<account-id>`.

## See Also

- [var uniqueIdentifier: String](cssearchableitem/uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var attributeSet: CSSearchableItemAttributeSet](cssearchableitem/attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.
- [var expirationDate: Date!](cssearchableitem/expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/domainidentifier)*