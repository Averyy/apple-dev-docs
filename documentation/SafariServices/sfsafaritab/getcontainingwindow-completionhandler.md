# getContainingWindow(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func containingWindow() async -> SFSafariWindow?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func containingWindow() async -> SFSafariWindow?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func containingWindow() async -> SFSafariWindow?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func close()](sfsafaritab/close.md)
- [func navigate(to: URL)](sfsafaritab/navigate(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getcontainingwindow(completionhandler:))*