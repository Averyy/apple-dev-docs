# resolveContent(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the contents of the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveContent(for intent: INSendMessageIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveContent(for intent: INSendMessageIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveContentForSendMessage:(INSendMessageIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

This method resolves the contents of the message.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For successful resolutions, create a resolution with the [`NSString`](../../Foundation/nsstring.md) object that contains the proposed content of the message.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSendMessageIntent, with: ([INSendMessageRecipientResolutionResult]) -> Void)](./resolverecipients%28for,with%29-609yw.md)
  Resolves the user’s input when it isn’t clear who the recipients of the message are.
- [func resolveOutgoingMessageType(for: INSendMessageIntent, with: (INOutgoingMessageTypeResolutionResult) -> Void)](./resolveoutgoingmessagetype%28for,with%29.md)
  Determines what type of message to send.
- [func resolveSpeakableGroupName(for: INSendMessageIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvespeakablegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolvecontent(for:with:))*