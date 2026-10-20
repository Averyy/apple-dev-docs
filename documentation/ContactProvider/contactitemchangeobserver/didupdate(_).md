# didUpdate(_:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an array of new and updated contact items to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didUpdate(_ items: [ContactItem])
```

#### Discussion

You can call this method multiple times to fulfill the [`suggestedBatchSize`](./suggestedbatchsize.md). The observer creates the new contact items and updates the existing contact items with their new values.

## Parameters

- `items`: The new and updated items.

## See Also

### Providing change data
- [enum ContactItem](../contactitem.md)
  An item in the contact database.
- [func didDelete([ContactItem.Identifier])](./diddelete%28_%29.md)
  Provides an array of deleted contact item identifiers to the observer.
- [ContactItem.Identifier](../contactitem/identifier.md)
  The app’s identifier for an item in the contact database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver/didupdate(_:))*