# didFinishEnumeratingChanges(upTo:moreComing:)

**Framework**: ContactProvider  
**Kind**: method  
**Required**: Yes

Marks a sync anchor of changed contact items as completed.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didFinishEnumeratingChanges(upTo syncAnchor: ContactItemSyncAnchor, moreComing: Bool)
```

#### Discussion

A change enumeration can resume in the future, continuing from this sync anchor. Calling this method saves the current batch of changed items to the system Contacts database.

## Parameters

- `syncAnchor`: The   where the next change enumeration should start from.
- `moreComing`: If  , the enumerator receives another call to  .

## See Also

- [struct ContactItemSyncAnchor](contactitemsyncanchor.md)
  A snapshot point into enumerating changed contact items.
- [func didFinishEnumeratingChangesWithError(any Error)](contactitemchangeobserver/didfinishenumeratingchangeswitherror(_:).md)
  Finishes the change enumeration with an error, indicating failure, to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver/didfinishenumeratingchanges(upto:morecoming:))*