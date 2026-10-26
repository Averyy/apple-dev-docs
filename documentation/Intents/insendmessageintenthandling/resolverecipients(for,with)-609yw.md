# resolveRecipients(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s input when it isn’t clear who the recipients of the message are.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveRecipients(for intent: INSendMessageIntent, with completion: @escaping @Sendable ([INSendMessageRecipientResolutionResult]) -> Void)
```

```swift
optional func resolveRecipients(for intent: INSendMessageIntent) async -> [INSendMessageRecipientResolutionResult]
```

```objc
- (void) resolveRecipientsForSendMessage:(INSendMessageIntent *) intent completion:(void (^)(NSArray<INSendMessageRecipientResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

This method verifies the identity of the intended recipients. Always strive toward a successful resolution of the specified users, but ask for confirmation for one or more users if there is some uncertainty.

If multiple users match a single recipient, you might ask for disambiguation of the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider another resolution.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object that contains the details of your proposed resolution. For each successful resolution, create a resolution object that includes the [`INPerson`](../inperson.md) object representing the user who will receive the message.

## See Also

### Resolving the Intent Parameters
- [func resolveOutgoingMessageType(for: INSendMessageIntent, with: (INOutgoingMessageTypeResolutionResult) -> Void)](./resolveoutgoingmessagetype%28for,with%29.md)
  Determines what type of message to send.
- [func resolveContent(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./resolvecontent%28for,with%29.md)
  Resolves the contents of the message.
- [func resolveSpeakableGroupName(for: INSendMessageIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvespeakablegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolverecipients(for:with:)-609yw)*