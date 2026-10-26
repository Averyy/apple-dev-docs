# resolveSpeakableGroupName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the group receiving the message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveSpeakableGroupName(for intent: INSendMessageIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveSpeakableGroupName(for intent: INSendMessageIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveSpeakableGroupNameForSendMessage:(INSendMessageIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method if your app supports the sending messages to named groups. You can specify a group instead of, or in addition to, individual recipients.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For successful resolutions, create a resolution with the [`NSString`](../../Foundation/nsstring.md) object that contains the name of the group recognized by your app.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSendMessageIntent, with: ([INSendMessageRecipientResolutionResult]) -> Void)](./resolverecipients%28for,with%29-609yw.md)
  Resolves the user’s input when it isn’t clear who the recipients of the message are.
- [func resolveOutgoingMessageType(for: INSendMessageIntent, with: (INOutgoingMessageTypeResolutionResult) -> Void)](./resolveoutgoingmessagetype%28for,with%29.md)
  Determines what type of message to send.
- [func resolveContent(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the contents of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolvespeakablegroupname(for:with:))*