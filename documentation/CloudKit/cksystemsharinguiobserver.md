# CKSystemSharingUIObserver

**Framework**: CloudKit  
**Kind**: class

An object the system uses to monitor changes in sharing.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CKSystemSharingUIObserver
```

#### Overview

Initialize a `CKSystemSharingUIObserver` instance with your [`CKContainer`](ckcontainer.md) when preparing to share an item using the share sheet. Use your implementation to update the local state of a shared item when your app receives a [`CKShare`](ckshare.md), or to delete a locally cached share when the system notifies your app about a share deletion.

The system only propagates changes on the local device using `CKSystemSharingUIObserver`. The system doesn’t notify your app about any remote changes on the server. For more information about how to keep your local cache in sync with remote changes, see [`Remote Records`](remote-records.md).

## Topics

### Creating a sharing observer
- [init(container: CKContainer)](cksystemsharinguiobserver/init(container:).md)
  Creates and initializes an observer using the provided container.
### Accessing sharing blocks
- [var systemSharingUIDidSaveShareBlock: ((CKRecord.ID, Result<CKShare, any Error>) -> Void)?](cksystemsharinguiobserver/systemsharinguididsaveshareblock-8c9vi.md)
  A callback block the system invokes after the success or failure of a system sharing UI save.
- [var systemSharingUIDidStopSharingBlock: ((CKRecord.ID, Result<Void, any Error>) -> Void)?](cksystemsharinguiobserver/systemsharinguididstopsharingblock-7nmiw.md)
  A callback block the system invokes after the success or failure of a system sharing UI delete.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Sharing CloudKit Data with Other iCloud Users](sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](ckshare.md)
  A specialized record type that manages a collection of shared records.
- [struct CKShareTransferRepresentation](cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKAllowedSharingOptions](ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [@MainActor class UICloudSharingController](../UIKit/UICloudSharingController.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/Information-Property-List/CKSharingSupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver)*