# primaryActionClicked(forMessageContext:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
func primaryActionClicked(forMessageContext context: Data) async -> MEExtensionViewController?
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func primaryActionClicked(forMessageContext context: Data) async -> MEExtensionViewController?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func primaryActionClicked(forMessageContext context: Data) async -> MEExtensionViewController?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func extensionViewController(messageContext: Data) -> MEExtensionViewController?](memessagesecurityhandler/extensionviewcontroller(messagecontext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityhandler/primaryactionclicked(formessagecontext:completionhandler:))*