# NSFileProviderTestingCreation

**Framework**: File Provider  
**Kind**: protocol

An operation that syncs the creation of the source item to the target location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderTestingCreation : NSFileProviderTestingOperation
```

## Topics

### Accessing the Operation’s Data
- [var sourceItem: NSFileProviderItem](nsfileprovidertestingcreation/sourceitem.md)
  A description of the item stored at the source.
- [var targetSide: NSFileProviderTestingOperationSide](nsfileprovidertestingcreation/targetside.md)
  The target location for the new item.
- [var domainVersion: NSFileProviderDomainVersion?](nsfileprovidertestingcreation/domainversion.md)
  The domain’s version when the system discovered the item at the source location.

## Relationships

### Inherits From
- [NSFileProviderTestingOperation](nsfileprovidertestingoperation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFileProviderTestingChildrenEnumeration](nsfileprovidertestingchildrenenumeration.md)
  An operation that lists a directory’s content.
- [protocol NSFileProviderTestingCollisionResolution](nsfileprovidertestingcollisionresolution.md)
  An operation that resolves a collision by renaming the new item.
- [protocol NSFileProviderTestingContentFetch](nsfileprovidertestingcontentfetch.md)
  An operation that fetches an item’s content.
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
- [enum NSFileProviderTestingOperationSide](nsfileprovidertestingoperationside.md)
  The location where the operation takes place.
- [enum NSFileProviderTestingOperationType](nsfileprovidertestingoperationtype.md)
  The action that an operation performs.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingcreation)*