# getToolbarItem(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Gets the extension’s toolbar item from the target window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func getToolbarItem(completionHandler: @escaping @Sendable (SFSafariToolbarItem?) -> Void)
```

```swift
func toolbarItem() async -> SFSafariToolbarItem?
```

```objc
- (void) getToolbarItemWithCompletionHandler:(void (^)(SFSafariToolbarItem *toolbarItem)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func toolbarItem() async -> SFSafariToolbarItem?
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: A block called after the toolbar item is retrieved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow/gettoolbaritem(completionhandler:))*