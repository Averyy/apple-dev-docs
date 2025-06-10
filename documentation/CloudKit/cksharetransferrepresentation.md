# CKShareTransferRepresentation

**Framework**: CloudKit  
**Kind**: struct

A transfer representation the system uses to share an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
struct CKShareTransferRepresentation<Item> where Item : Transferable
```

## Topics

### Creating a transfer representation
- [init(exporter: (Item) throws -> CKShareTransferRepresentation<Item>.ExportedShare)](cksharetransferrepresentation/init(exporter:).md)
  Creates and initializes a transfer representation.
### Accessing transfer representation attributes
- [CKShareTransferRepresentation.ExportedShare](cksharetransferrepresentation/exportedshare.md)
  An intermediate structure that returns an existing share or prepares a new one if it doesn’t exist.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TransferRepresentation](../CoreTransferable/TransferRepresentation.md)

## See Also

- [Sharing CloudKit Data with Other iCloud Users](sharing-cloudkit-data-with-other-icloud-users.md)
  Create and share private CloudKit data with other users by implementing the sharing UI.
- [Sharing Core Data objects between iCloud users](../CoreData/sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.
- [class CKShare](ckshare.md)
  A specialized record type that manages a collection of shared records.
- [class CKAllowedSharingOptions](ckallowedsharingoptions.md)
  An object that controls participant access and permission options.
- [class CKSystemSharingUIObserver](cksystemsharinguiobserver.md)
  An object the system uses to monitor changes in sharing.
- [@MainActor class UICloudSharingController](../UIKit/UICloudSharingController.md)
  A view controller that presents standard screens for adding and removing people from a CloudKit share record.
- [CKSharingSupported](../BundleResources/Information-Property-List/CKSharingSupported.md)
  A Boolean value that indicates your app supports CloudKit Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharetransferrepresentation)*