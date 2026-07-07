# NSFileProviderTestingOperation

**Framework**: File Provider  
**Kind**: protocol

An operation that the system can schedule.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderTestingOperation : NSObjectProtocol
```

## Topics

### Access the Operation Type
- [var type: NSFileProviderTestingOperationType](nsfileprovidertestingoperation/type.md)
  The operation’s type.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSFileProviderTestingChildrenEnumeration](nsfileprovidertestingchildrenenumeration.md)
- [NSFileProviderTestingCollisionResolution](nsfileprovidertestingcollisionresolution.md)
- [NSFileProviderTestingContentFetch](nsfileprovidertestingcontentfetch.md)
- [NSFileProviderTestingCreation](nsfileprovidertestingcreation.md)
- [NSFileProviderTestingDeletion](nsfileprovidertestingdeletion.md)
- [NSFileProviderTestingIngestion](nsfileprovidertestingingestion.md)
- [NSFileProviderTestingLookup](nsfileprovidertestinglookup.md)
- [NSFileProviderTestingModification](nsfileprovidertestingmodification.md)

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
- [protocol NSFileProviderUserInteractionSuppressing](nsfileprovideruserinteractionsuppressing.md)
  Support for suppressing user-interaction alerts.
- [enum NSFileProviderTestingOperationSide](nsfileprovidertestingoperationside.md)
  The location where the operation takes place.
- [enum NSFileProviderTestingOperationType](nsfileprovidertestingoperationtype.md)
  The action that an operation performs.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingoperation)*