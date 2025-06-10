# materializedItemsDidChange(completionHandler:)

**Framework**: File Provider  
**Kind**: method

Tells the file provider that the set of materialized items changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func materializedItemsDidChange() async
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func materializedItemsDidChange() async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The system calls this method when the set of materialized items changes, such as when the system downloads the content of a dataless item, or deletes the contents of a materialized item.

> **Note**:  The system doesn’t call this method when the item’s content changes.

Keep track of the items in the working set—the set of items that the system has downloaded and is managing on disk—to optimize updates. Your file provider must let the system know about any changes to the working set. If you don’t track the working set, then you need to let the system know about any changes to any items in the remote storage.

For more information, see [`Synchronizing the File Provider Extension`](synchronizing-the-file-provider-extension.md).

## Parameters

- `completionHandler`: A block that you call after you finish processing the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/materializeditemsdidchange(completionhandler:))*