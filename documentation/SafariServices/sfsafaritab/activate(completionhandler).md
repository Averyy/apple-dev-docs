# activate(completionHandler:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Activates the tab.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func activate(completionHandler: (@Sendable () -> Void)? = nil)
```

```swift
func activate() async
```

```objc
- (void) activateWithCompletionHandler:(void (^)()) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func activate() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: A block to call when the tab is activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafaritab/activate(completionhandler:))*