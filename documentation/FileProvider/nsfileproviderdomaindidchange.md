# NSFileProviderDomainDidChange

**Framework**: File Provider  
**Kind**: var

A notification that posts when a file provider’s domain changes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
extern NSNotificationName const NSFileProviderDomainDidChange;
```

#### Discussion

The system only posts this notification after the first call to [`getDomainsWithCompletionHandler(_:)`](nsfileprovidermanager/getdomainswithcompletionhandler(_:).md). After receiving this notification, call [`getDomainsWithCompletionHandler(_:)`](nsfileprovidermanager/getdomainswithcompletionhandler(_:).md) again to determine what the changes are.

## See Also

- [NSFileProviderMaterializedSetDidChange](nsfileprovidermaterializedsetdidchange.md)
  A notification that the system posts when the set of materialized items changes for your file provider extension.
- [NSFileProviderPendingSetDidChange](nsfileproviderpendingsetdidchange.md)
  A notification that the system posts when the set of pending items changes for your file provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomaindidchange)*