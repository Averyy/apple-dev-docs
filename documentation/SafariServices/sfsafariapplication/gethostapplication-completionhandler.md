# getHostApplication(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

**Availability**:
- macOS 10.13+

## Declaration

```swift
class func hostApplication() async -> NSRunningApplication
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func hostApplication() async -> NSRunningApplication
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [class func getAllWindows(completionHandler: ([SFSafariWindow]) -> Void)](sfsafariapplication/getallwindows(completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/gethostapplication(completionhandler:))*