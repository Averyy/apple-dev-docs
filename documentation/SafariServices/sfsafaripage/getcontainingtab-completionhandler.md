# getContainingTab(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func containingTab() async -> SFSafariTab
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func containingTab() async -> SFSafariTab
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func containingTab() async -> SFSafariTab
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func getScreenshotOfVisibleArea(completionHandler: (NSImage?) -> Void)](sfsafaripage/getscreenshotofvisiblearea(completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage/getcontainingtab(completionhandler:))*