# CKSystemSharingUIObserver

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CKSystemSharingUIObserver : NSObject
```

#### Overview

Initialize a `CKSystemSharingUIObserver` instance with your [`CKContainer`](./ckcontainer.md) when preparing to share an item using the share sheet. Use your implementation to update the local state of a shared item when your app receives a [`CKShare`](./ckshare.md), or to delete a locally cached share when the system notifies your app about a share deletion.

The system only propagates changes on the local device using `CKSystemSharingUIObserver`. The system doesn’t notify your app about any remote changes on the server. For more information about how to keep your local cache in sync with remote changes, see [Remote Records](./remote-records.md).

## Topics

### Creating a sharing observer
- [init(container: CKContainer)](./cksystemsharinguiobserver/init%28container%29.md)
  Creates and initializes an observer using the provided container.
### Accessing sharing blocks
- [var systemSharingUIDidSaveShareBlock: ((CKRecord.ID, Result<CKShare, any Error>) -> Void)?](./cksystemsharinguiobserver/systemsharinguididsaveshareblock-8c9vi.md)
  A callback block the system invokes after the success or failure of a share save by the system sharing UI.
- [var systemSharingUIDidStopSharingBlock: ((CKRecord.ID, Result<Void, any Error>) -> Void)?](./cksystemsharinguiobserver/systemsharinguididstopsharingblock-7nmiw.md)
  A callback block the system invokes after the success or failure of a share delete by the system sharing UI.
- [systemSharingUIDidSaveShareBlock](./cksystemsharinguiobserver/systemsharinguididsaveshareblock-39zlv.md)
  A callback block the system invokes after the success or failure of a share save by the system sharing UI.
- [systemSharingUIDidStopSharingBlock](./cksystemsharinguiobserver/systemsharinguididstopsharingblock-4g5bn.md)
  A callback block the system invokes after the success or failure of a share delete by the system sharing UI.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collaboration
- [Sharing CloudKit Data with Other iCloud Users](./sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](./ckshare.md)
  A specialized record type that manages a collection of shared records.
- [struct CKShareTransferRepresentation](./cksharetransferrepresentation.md)
  A transfer representation the system uses to share an item.
- [class CKAllowedSharingOptions](./ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [class UICloudSharingController](../UIKit/uicloudsharingcontroller.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/information-property-list/cksharingsupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.
- [CKSharePreparationCompletionHandler](./cksharepreparationcompletionhandler.md)
- [CKSharePreparationHandler](./cksharepreparationhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksystemsharinguiobserver)*