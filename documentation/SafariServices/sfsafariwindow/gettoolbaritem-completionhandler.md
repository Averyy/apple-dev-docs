# getToolbarItem(completionHandler:)

**Framework**: Safari Services  
**Kind**: method

Gets the extension’s toolbar item from the target window.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func toolbarItem() async -> SFSafariToolbarItem?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func toolbarItem() async -> SFSafariToolbarItem?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func toolbarItem() async -> SFSafariToolbarItem?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A block called after the toolbar item is retrieved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariwindow/gettoolbaritem(completionhandler:))*