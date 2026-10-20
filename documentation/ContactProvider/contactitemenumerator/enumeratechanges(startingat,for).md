# enumerateChanges(startingAt:for:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Enumerates items changed since the last sync.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func enumerateChanges(startingAt syncAnchor: ContactItemSyncAnchor, for observer: any ContactItemChangeObserver) async
```

#### Discussion

The system calls `enumerateChanges(startingAt:for:)` for each batch of changed items to enumerate. After enumerating each batch of changed items, your implementation calls [`didFinishEnumeratingChanges(upTo:moreComing:)`](../contactitemchangeobserver/didfinishenumeratingchanges%28upto,morecoming%29.md) .

Your implementation can enumerate items in any order, but that order must be deterministic and resumable.

## Parameters

- `syncAnchor`: The sync anchor to enumerate changed items from.
- `observer`: The system observer that receives the change items and enumeration state.

## See Also

### Enumerating item changes
- [struct ContactItemSyncAnchor](../contactitemsyncanchor.md)
  A snapshot point into enumerating changed contact items.
- [protocol ContactItemChangeObserver](../contactitemchangeobserver.md)
  A protocol that defines a system observer that receives a resumable enumeration of changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemenumerator/enumeratechanges(startingat:for:))*