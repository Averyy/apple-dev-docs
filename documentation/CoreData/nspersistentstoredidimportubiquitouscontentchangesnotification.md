# NSPersistentStoreDidImportUbiquitousContentChangesNotification

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

Posted after records are imported from the ubiquitous content store.

**Availability**:
- iOS 5.0+ - Deprecated in 10.0
- iPadOS 5.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```c
extern NSString * const NSPersistentStoreDidImportUbiquitousContentChangesNotification;
```

#### Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator` instance which registered the store. The notification’s `userInfo` dictionary contains the same keys as the [`NSManagedObjectContextObjectsDidChangeNotification`](./nsmanagedobjectcontextobjectsdidchangenotification.md) notification ([`NSInsertedObjectsKey`](./nsinsertedobjectskey.md), [`NSUpdatedObjectsKey`](./nsupdatedobjectskey.md), [`NSDeletedObjectsKey`](./nsdeletedobjectskey.md)), however the values are sets of [`NSManagedObjectID`](./nsmanagedobjectid.md) objects rather than sets of [`NSManagedObject`](./nsmanagedobject.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification)*