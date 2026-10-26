# CKSharePreparationCompletionHandler

**Framework**: CloudKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef void (^)(CKShare *, NSError *) CKSharePreparationCompletionHandler;
```

## See Also

### Collaboration
- [Sharing CloudKit Data with Other iCloud Users](./sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](./ckshare.md)
  A specialized record type that manages a collection of shared records.
- [class CKAllowedSharingOptions](./ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [class CKSystemSharingUIObserver](./cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [class UICloudSharingController](../UIKit/uicloudsharingcontroller.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharePreparationHandler](./cksharepreparationhandler.md)
- [CKSharingSupported](../BundleResources/information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharepreparationcompletionhandler)*