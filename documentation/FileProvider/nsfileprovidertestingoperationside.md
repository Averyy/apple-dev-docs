# NSFileProviderTestingOperationSide

**Framework**: File Provider  
**Kind**: enum

The location where the operation takes place.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
enum NSFileProviderTestingOperationSide
```

#### Overview

Most operations are symmetrical. They can affect either items stored locally or items in the File Provider extension’s remote storage.

## Topics

### Locations
- [NSFileProviderTestingOperationSide.disk](nsfileprovidertestingoperationside/disk.md)
  The File Provider extension’s local storage.
- [NSFileProviderTestingOperationSide.fileProvider](nsfileprovidertestingoperationside/fileprovider.md)
  The File Provider extension’s remote storage.
### Initializers
- [init?(rawValue: UInt)](nsfileprovidertestingoperationside/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSFileProviderTestingChildrenEnumeration](nsfileprovidertestingchildrenenumeration.md)
  An operation that lists a directory’s content.
- [protocol NSFileProviderTestingCollisionResolution](nsfileprovidertestingcollisionresolution.md)
  An operation that resolves a collision by renaming the new item.
- [protocol NSFileProviderTestingContentFetch](nsfileprovidertestingcontentfetch.md)
  An operation that fetches an item’s content.
- [protocol NSFileProviderTestingCreation](nsfileprovidertestingcreation.md)
  An operation that syncs the creation of the source item to the target location.
- [protocol NSFileProviderTestingDeletion](nsfileprovidertestingdeletion.md)
  An operation that syncs the deletion of the source item to the target location.
- [protocol NSFileProviderTestingIngestion](nsfileprovidertestingingestion.md)
  An operation that alerts the system to either local or remote storage changes.
- [protocol NSFileProviderTestingLookup](nsfileprovidertestinglookup.md)
  An operation that looks up an item.
- [protocol NSFileProviderTestingModification](nsfileprovidertestingmodification.md)
  An operation that syncs the modification of the source item to the target location.
- [protocol NSFileProviderTestingOperation](nsfileprovidertestingoperation.md)
  An operation that the system can schedule.
- [protocol NSFileProviderUserInteractionSuppressing](nsfileprovideruserinteractionsuppressing.md)
  Support for suppressing user-interaction alerts.
- [enum NSFileProviderTestingOperationType](nsfileprovidertestingoperationtype.md)
  The action that an operation performs.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingoperationside)*