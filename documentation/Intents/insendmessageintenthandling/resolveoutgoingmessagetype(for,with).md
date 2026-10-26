# resolveOutgoingMessageType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Determines what type of message to send.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func resolveOutgoingMessageType(for intent: INSendMessageIntent, with completion: @escaping @Sendable (INOutgoingMessageTypeResolutionResult) -> Void)
```

```swift
optional func resolveOutgoingMessageType(for intent: INSendMessageIntent) async -> INOutgoingMessageTypeResolutionResult
```

```objc
- (void) resolveOutgoingMessageTypeForSendMessage:(INSendMessageIntent *) intent withCompletion:(void (^)(INOutgoingMessageTypeResolutionResult *resolutionResult)) completion;
```

#### Discussion

If you can’t handle messages of the type specified in the intent’s [`outgoingMessageType`](../insendmessageintent/outgoingmessagetype.md), create a result with [`unsupported()`](../inintentresolutionresult/unsupported%28%29.md) and provide that when you call the completion handler.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution object with the [`INOutgoingMessageType`](../inoutgoingmessagetype.md) for the message.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSendMessageIntent, with: ([INSendMessageRecipientResolutionResult]) -> Void)](./resolverecipients%28for,with%29-609yw.md)
  Resolves the user’s input when it isn’t clear who the recipients of the message are.
- [func resolveContent(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the contents of the message.
- [func resolveSpeakableGroupName(for: INSendMessageIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvespeakablegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolveoutgoingmessagetype(for:with:))*