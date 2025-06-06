# getEncodingStatus(for:composeContext:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func encodingStatus(for message: MEMessage, composeContext: MEComposeContext) async -> MEOutgoingMessageEncodingStatus
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func encodingStatus(for message: MEMessage, composeContext: MEComposeContext) async -> MEOutgoingMessageEncodingStatus
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func encodingStatus(for message: MEMessage, composeContext: MEComposeContext) async -> MEOutgoingMessageEncodingStatus
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [func encode(MEMessage, composeContext: MEComposeContext, completionHandler: (MEMessageEncodingResult) -> Void)](memessageencoder/encode(_:composecontext:completionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencoder/getencodingstatus(for:composecontext:completionhandler:))*