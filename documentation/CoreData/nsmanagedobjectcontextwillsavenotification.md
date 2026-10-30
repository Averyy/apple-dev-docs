# NSManagedObjectContextWillSaveNotification

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

A notification that posts before a context writes unsaved changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern NSString * const NSManagedObjectContextWillSaveNotification;
```

## Discussion

This notification’s `object` is the context that’s about to save. Only use the notification to operate on the in-process save operation. For example, to insert additional managed objects. Don’t peform any asynchronous work or block the calling thread. [`NSManagedObjectContext`](./nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

There is no `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextwillsavenotification)*