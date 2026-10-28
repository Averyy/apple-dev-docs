# getActivePage(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Calls the completion handler passing the active page in the tab.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func getActivePage(completionHandler: @escaping @Sendable (SFSafariPage?) -> Void)
```

```swift
func activePage() async -> SFSafariPage?
```

```objc
- (void) getActivePageWithCompletionHandler:(void (^)(SFSafariPage *activePage)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func activePage() async -> SFSafariPage?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: A block to call when the active page is retrieved.

## See Also

### Accessing Pages
- [func getPagesWithCompletionHandler(([SFSafariPage]?) -> Void)](./getpageswithcompletionhandler%28_%29.md)
  Calls the completion handler with all of the tab’s active and preloading pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getactivepage(completionhandler:))*