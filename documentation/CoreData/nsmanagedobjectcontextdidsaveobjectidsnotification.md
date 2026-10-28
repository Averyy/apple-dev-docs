# NSManagedObjectContextDidSaveObjectIDsNotification

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a context finishes writing changes.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```c
extern NSString * const NSManagedObjectContextDidSaveObjectIDsNotification;
```

## Discussion

This notification’s `object` is the saved context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](./nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](./nsmanagedobjectcontext/notificationkey.md). It’s safe to capture the dictionary’s contents.

Use this notification instead of [`NSManagedObjectContextDidSaveNotification`](./nsmanagedobjectcontextdidsavenotification.md) if you intend to process the changed managed object on a different thread. It’s safe to pass instances of [`NSManagedObjectID`](./nsmanagedobjectid.md) across thread boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsaveobjectidsnotification)*