# NSFileProviderTestingChildrenEnumeration

**Framework**: File Provider  
**Kind**: protocol

An operation that lists a directory’s content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderTestingChildrenEnumeration : NSFileProviderTestingOperation
```

## Topics

### Accessing The Operation’s Data
- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovidertestingchildrenenumeration/itemidentifier.md)
  The containing identifier’s unique identifier.
- [var side: NSFileProviderTestingOperationSide](nsfileprovidertestingchildrenenumeration/side.md)
  The item’s location.

## Relationships

### Inherits From
- [NSFileProviderTestingOperation](nsfileprovidertestingoperation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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
- [enum NSFileProviderTestingOperationSide](nsfileprovidertestingoperationside.md)
  The location where the operation takes place.
- [enum NSFileProviderTestingOperationType](nsfileprovidertestingoperationtype.md)
  The action that an operation performs.
- [com.apple.developer.fileprovider.testing-mode](../BundleResources/Entitlements/com.apple.developer.fileprovider.testing-mode.md)
  A Boolean value that indicates whether you can place domains in testing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertestingchildrenenumeration)*