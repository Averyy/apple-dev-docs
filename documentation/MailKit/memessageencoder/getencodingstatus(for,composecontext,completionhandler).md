# getEncodingStatus(for:composeContext:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func getEncodingStatus(for message: MEMessage, composeContext: MEComposeContext, completionHandler: @escaping @Sendable (MEOutgoingMessageEncodingStatus) -> Void)
```

```swift
func encodingStatus(for message: MEMessage, composeContext: MEComposeContext) async -> MEOutgoingMessageEncodingStatus
```

```objc
- (void) getEncodingStatusForMessage:(MEMessage *) message composeContext:(MEComposeContext *) composeContext completionHandler:(void (^)(MEOutgoingMessageEncodingStatus *status)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func encodingStatus(for message: MEMessage, composeContext: MEComposeContext) async -> MEOutgoingMessageEncodingStatus
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func encode(MEMessage, composeContext: MEComposeContext, completionHandler: (MEMessageEncodingResult) -> Void)](./encode%28_,composecontext,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencoder/getencodingstatus(for:composecontext:completionhandler:))*