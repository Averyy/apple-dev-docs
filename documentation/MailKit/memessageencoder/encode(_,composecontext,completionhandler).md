# encode(_:composeContext:completionHandler:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 12.0+

## Declaration

```swift
func encode(_ message: MEMessage, composeContext: MEComposeContext, completionHandler: @escaping @Sendable (MEMessageEncodingResult) -> Void)
```

```swift
func encode(_ message: MEMessage, composeContext: MEComposeContext) async -> MEMessageEncodingResult
```

```objc
- (void) encodeMessage:(MEMessage *) message composeContext:(MEComposeContext *) composeContext completionHandler:(void (^)(MEMessageEncodingResult *result)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func encode(_ message: MEMessage, composeContext: MEComposeContext) async -> MEMessageEncodingResult
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Instance Methods
- [func getEncodingStatus(for: MEMessage, composeContext: MEComposeContext, completionHandler: (MEOutgoingMessageEncodingStatus) -> Void)](./getencodingstatus%28for,composecontext,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageencoder/encode(_:composecontext:completionhandler:))*