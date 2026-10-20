# didDelete(_:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides an array of deleted contact item identifiers to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didDelete(_ identifiers: [ContactItem.Identifier])
```

#### Discussion

You can call this method multiple times to fulfill the [`suggestedBatchSize`](./suggestedbatchsize.md).

## Parameters

- `identifiers`: The identifiers of the deleted items.

## See Also

### Providing change data
- [func didUpdate([ContactItem])](./didupdate%28_%29.md)
  Provides an array of new and updated contact items to the observer.
- [enum ContactItem](../contactitem.md)
  An item in the contact database.
- [ContactItem.Identifier](../contactitem/identifier.md)
  The app’s identifier for an item in the contact database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver/diddelete(_:))*