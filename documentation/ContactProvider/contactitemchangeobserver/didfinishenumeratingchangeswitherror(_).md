# didFinishEnumeratingChangesWithError(_:)

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finishes the change enumeration with an error, indicating failure, to the observer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func didFinishEnumeratingChangesWithError(_: any Error)
```

## Discussion

Use `ContactProviderError.changeAnchorExpired` to restart the content enumeration.

## See Also

### Ending enumeration
- [func didFinishEnumeratingChanges(upTo: ContactItemSyncAnchor, moreComing: Bool)](./didfinishenumeratingchanges%28upto,morecoming%29.md)
  Marks a sync anchor of changed contact items as completed.
- [struct ContactItemSyncAnchor](../contactitemsyncanchor.md)
  A snapshot point into enumerating changed contact items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver/didfinishenumeratingchangeswitherror(_:))*