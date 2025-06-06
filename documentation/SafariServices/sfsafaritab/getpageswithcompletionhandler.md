# getPagesWithCompletionHandler(_:)

**Framework**: Safari Services  
**Kind**: method

Calls the completion handler with all of the tab’s active and preloading pages.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func pages() async -> [SFSafariPage]?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func pages() async -> [SFSafariPage]?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func pages() async -> [SFSafariPage]?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The tab’s pages include the active page and other pages that Safari might be loading in the background; for example, Top Hits.

## Parameters

- `completionHandler`: A block to call when the tab’s pages are retrieved.

## See Also

- [func getActivePage(completionHandler: (SFSafariPage?) -> Void)](sfsafaritab/getactivepage(completionhandler:).md)
  Calls the completion handler passing the active page in the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getpageswithcompletionhandler(_:))*