# getContainingTab(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func getContainingTab(completionHandler: @escaping @Sendable (SFSafariTab) -> Void)
```

```swift
func containingTab() async -> SFSafariTab
```

```objc
- (void) getContainingTabWithCompletionHandler:(void (^)(SFSafariTab *tab)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func containingTab() async -> SFSafariTab
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func getScreenshotOfVisibleArea(completionHandler: (NSImage?) -> Void)](./getscreenshotofvisiblearea%28completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaripage/getcontainingtab(completionhandler:))*