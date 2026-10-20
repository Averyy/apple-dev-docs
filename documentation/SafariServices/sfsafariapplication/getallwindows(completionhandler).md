# getAllWindows(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Type Method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
class func getAllWindows(completionHandler: @escaping @Sendable ([SFSafariWindow]) -> Void)
```

```swift
class func allWindows() async -> [SFSafariWindow]
```

```objc
+ (void) getAllWindowsWithCompletionHandler:(void (^)(NSArray<SFSafariWindow *> *windows)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func allWindows() async -> [SFSafariWindow]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Type Methods
- [class func getHostApplication(completionHandler: (NSRunningApplication) -> Void)](./gethostapplication%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/getallwindows(completionhandler:))*