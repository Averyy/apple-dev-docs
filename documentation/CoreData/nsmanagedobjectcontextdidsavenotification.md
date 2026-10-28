# NSManagedObjectContextDidSaveNotification

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a context finishes writing unsaved changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSString * const NSManagedObjectContextDidSaveNotification;
```

## Discussion

> ❗ **Important**:  Use [`NSManagedObjectContextDidSaveObjectIDsNotification`](./nsmanagedobjectcontextdidsaveobjectidsnotification.md) instead of this notification.

This notification’s `object` is the saved context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](./nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the inserted, updated, and deleted managed objects of the completed save. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](./nsmanagedobjectcontext/notificationkey.md). Don’t capture the dictionary’s contents.

To safely use the provided managed objects on the current thread, create a new context and use its [`mergeChanges(fromContextDidSave:)`](./nsmanagedobjectcontext/mergechanges%28fromcontextdidsave%29.md) method to merge in the notification’s changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsavenotification)*