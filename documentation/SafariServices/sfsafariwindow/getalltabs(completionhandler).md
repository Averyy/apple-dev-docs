# getAllTabs(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.14.4+

## Declaration

```swift
func getAllTabs(completionHandler: @escaping @Sendable ([SFSafariTab]) -> Void)
```

```swift
func allTabs() async -> [SFSafariTab]
```

```objc
- (void) getAllTabsWithCompletionHandler:(void (^)(NSArray<SFSafariTab *> *tabs)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func allTabs() async -> [SFSafariTab]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func close()](./close%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow/getalltabs(completionhandler:))*