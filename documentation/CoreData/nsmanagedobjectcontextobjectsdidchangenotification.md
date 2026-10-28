# NSManagedObjectContextObjectsDidChangeNotification

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A notification that posts when there are changes to context’s registered managed objects.

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
extern NSString * const NSManagedObjectContextObjectsDidChangeNotification;
```

## Discussion

> **Note**:  This notification posts only when there are changes to the context’s registered managed objects. It doesn’t post when a fetch adds managed objects to the context.

This notification’s `object` property is the changed managed object context. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](./nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [`NSManagedObjectContext.NotificationKey`](./nsmanagedobjectcontext/notificationkey.md). Don’t capture the dictionary’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextobjectsdidchangenotification)*