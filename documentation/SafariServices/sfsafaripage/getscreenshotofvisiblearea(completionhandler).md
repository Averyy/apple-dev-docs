# getScreenshotOfVisibleArea(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func getScreenshotOfVisibleArea(completionHandler: @escaping @Sendable (NSImage?) -> Void)
```

```swift
func screenshotOfVisibleArea() async -> NSImage?
```

```objc
- (void) getScreenshotOfVisibleAreaWithCompletionHandler:(void (^)(NSImage *image)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func screenshotOfVisibleArea() async -> NSImage?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func getContainingTab(completionHandler: (SFSafariTab) -> Void)](./getcontainingtab%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage/getscreenshotofvisiblearea(completionhandler:))*