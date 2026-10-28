# getHostApplication(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 10.13+

## Declaration

```swift
class func getHostApplication(completionHandler: @escaping @Sendable (NSRunningApplication) -> Void)
```

```swift
class func hostApplication() async -> NSRunningApplication
```

```objc
+ (void) getHostApplicationWithCompletionHandler:(void (^)(NSRunningApplication *hostApplication)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func hostApplication() async -> NSRunningApplication
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Type Methods
- [class func getAllWindows(completionHandler: ([SFSafariWindow]) -> Void)](./getallwindows%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/gethostapplication(completionhandler:))*