# getActivePage(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Calls the completion handler passing the active page in the tab.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func activePage() async -> SFSafariPage?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func activePage() async -> SFSafariPage?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A block to call when the active page is retrieved.

## See Also

- [func getPagesWithCompletionHandler(([SFSafariPage]?) -> Void)](sfsafaritab/getpageswithcompletionhandler(_:).md)
  Calls the completion handler with all of the tab’s active and preloading pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getactivepage(completionhandler:))*