# getContainingWindow(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func getContainingWindow(completionHandler: @escaping @Sendable (SFSafariWindow?) -> Void)
```

```swift
func containingWindow() async -> SFSafariWindow?
```

```objc
- (void) getContainingWindowWithCompletionHandler:(void (^)(SFSafariWindow *window)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func containingWindow() async -> SFSafariWindow?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func close()](./close%28%29.md)
- [func navigate(to: URL)](./navigate%28to%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getcontainingwindow(completionhandler:))*