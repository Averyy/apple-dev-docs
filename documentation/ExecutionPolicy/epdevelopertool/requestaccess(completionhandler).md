# requestAccess(completionHandler:)

**Framework**: Execution Policy  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
func requestAccess(completionHandler handler: @escaping @Sendable (Bool) -> Void)
```

```swift
func requestAccess() async -> Bool
```

```objc
- (void) requestDeveloperToolAccessWithCompletionHandler:(void (^)(BOOL granted)) handler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestAccess() async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/executionpolicy/epdevelopertool/requestaccess(completionhandler:))*