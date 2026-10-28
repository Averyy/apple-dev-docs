# ContactItemChangeObserver

**Framework**: ContactProvider  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines a system observer that receives a resumable enumeration of changed contact items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactItemChangeObserver
```

## Overview

Your implementation of [`enumerateChanges(startingAt:for:)`](./contactitemenumerator/enumeratechanges%28startingat,for%29.md) receives an observer that conforms to this type. As you enumerate over your contacts, you provide them to the observer with the [`didUpdate(_:)`](./contactitemchangeobserver/didupdate%28_%29.md) and [`didDelete(_:)`](./contactitemchangeobserver/diddelete%28_%29.md) methods.

## Topics

### Providing change data
- [func didUpdate([ContactItem])](./contactitemchangeobserver/didupdate%28_%29.md)
  Provides an array of new and updated contact items to the observer.
- [enum ContactItem](./contactitem.md)
  An item in the contact database.
- [func didDelete([ContactItem.Identifier])](./contactitemchangeobserver/diddelete%28_%29.md)
  Provides an array of deleted contact item identifiers to the observer.
- [ContactItem.Identifier](./contactitem/identifier.md)
  The app’s identifier for an item in the contact database.
### Ending enumeration
- [func didFinishEnumeratingChanges(upTo: ContactItemSyncAnchor, moreComing: Bool)](./contactitemchangeobserver/didfinishenumeratingchanges%28upto,morecoming%29.md)
  Marks a sync anchor of changed contact items as completed.
- [struct ContactItemSyncAnchor](./contactitemsyncanchor.md)
  A snapshot point into enumerating changed contact items.
- [func didFinishEnumeratingChangesWithError(any Error)](./contactitemchangeobserver/didfinishenumeratingchangeswitherror%28_%29.md)
  Finishes the change enumeration with an error, indicating failure, to the observer.
### Optimizing observer batching
- [var suggestedBatchSize: Int](./contactitemchangeobserver/suggestedbatchsize.md)
  Retrieves the suggested number of changed contact items to include in a batch.

## See Also

### Receiving contacts
- [protocol ContactItemContentObserver](./contactitemcontentobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of all items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver)*