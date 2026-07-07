# mayAlreadyExist

**Framework**: File Provider  
**Kind**: property

An option indicating that the item may already exist in your remote storage.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var mayAlreadyExist: NSFileProviderCreateItemOptions { get }
```

#### Discussion

Your extension should examine the item and determine whether it exists in your remote storage. Because the system may try to reimport a large number of items at once, avoid performing any computationally expensive tasks while trying to match items.

The system attempts to create an item using this flag in the following situations:

- The system reimports its items after an action that might cause it to lose synchronization with your remote storage, such as when restoring a backup or migrating to a new device.
- When merging two directories, the system attempts to create each child object passing the [`mayAlreadyExist`](nsfileprovidercreateitemoptions/mayalreadyexist.md) flag. Your extension can then recursively merge the child items.

After processing all the imported items, the system calls the [`importDidFinish(completionHandler:)`](nsfileproviderreplicatedextension/importdidfinish(completionhandler:).md) method.

## See Also

- [static var deletionConflicted: NSFileProviderCreateItemOptions](nsfileprovidercreateitemoptions/deletionconflicted.md)
  A value indicating a conflict for a deleted item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercreateitemoptions/mayalreadyexist)*