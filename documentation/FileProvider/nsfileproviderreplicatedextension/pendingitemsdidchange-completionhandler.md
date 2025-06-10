# pendingItemsDidChange(completionHandler:)

**Framework**: File Provider  
**Kind**: method

Tells the file provider extension that the set of pending items has changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
optional func pendingItemsDidChange() async
```

#### Discussion

> ❗ **Important**:  You can implement this method as a synchronous method that takes a completion handler, as shown on this page, or as an asynchronous method that has the following declaration: ```swift
optional func pendingItemsDidChange() async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The system calls this method whenever the set of pending items changes. It updates the pending set regularly, but only when there are meaningful changes, such as:

- New items are now pending.
- The system has successfully synced one or more pending items.
- The domain version changed when the pending item set wasn’t empty.

To enumerate the pending set, create an object that adopts the [`NSFileProviderEnumerationObserver`](nsfileproviderenumerationobserver.md) and [`NSFileProviderChangeObserver`](nsfileproviderchangeobserver.md) protocols. Then pass this item to the [`enumeratorForPendingItems()`](nsfileprovidermanager/enumeratorforpendingitems().md) method on a [`NSFileProviderManager`](nsfileprovidermanager.md) instance for your domain. The system then calls your observer object’s methods when the pending set changes.

> 💡 **Tip**:  Calls to the observer object may not happen immediately. Don’t use the pending set to detect changes.

## Parameters

- `completionHandler`: A block that you call after you finish processing the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension/pendingitemsdidchange(completionhandler:))*