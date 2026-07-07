# currentSyncAnchor(completionHandler:)

**Framework**: File Provider  
**Kind**: method

Returns the current sync anchor.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func currentSyncAnchor() async -> NSFileProviderSyncAnchor?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func currentSyncAnchor() async -> NSFileProviderSyncAnchor?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func enumerateItems(for: any NSFileProviderEnumerationObserver, startingAt: NSFileProviderPage)](nsfileproviderenumerator/enumerateitems(for:startingat:).md)
  Requests the next batch of items, starting at the specified page.
- [func enumerateChanges(for: any NSFileProviderChangeObserver, from: NSFileProviderSyncAnchor)](nsfileproviderenumerator/enumeratechanges(for:from:).md)
  Requests the next batch of changes after the specified sync anchor.
- [func invalidate()](nsfileproviderenumerator/invalidate.md)
  Stops the enumeration of items and changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerator/currentsyncanchor(completionhandler:))*