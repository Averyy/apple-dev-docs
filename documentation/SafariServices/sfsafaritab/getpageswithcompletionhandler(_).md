# getPagesWithCompletionHandler(_:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Calls the completion handler with all of the tab’s active and preloading pages.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func getPagesWithCompletionHandler(_ completionHandler: @escaping @Sendable ([SFSafariPage]?) -> Void)
```

```swift
func pages() async -> [SFSafariPage]?
```

```objc
- (void) getPagesWithCompletionHandler:(void (^)(NSArray<SFSafariPage *> *pages)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func pages() async -> [SFSafariPage]?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

The tab’s pages include the active page and other pages that Safari might be loading in the background; for example, Top Hits.

## Parameters

- `completionHandler`: A block to call when the tab’s pages are retrieved.

## See Also

### Accessing Pages
- [func getActivePage(completionHandler: (SFSafariPage?) -> Void)](./getactivepage%28completionhandler%29.md)
  Calls the completion handler passing the active page in the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/getpageswithcompletionhandler(_:))*