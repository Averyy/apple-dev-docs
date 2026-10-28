# resolveGroupName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the group receiving the message.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 12.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`resolveSpeakableGroupName(for:with:)`](./resolvespeakablegroupname%28for,with%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func resolveGroupName(for intent: INSendMessageIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func resolveGroupName(for intent: INSendMessageIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveGroupNameForSendMessage:(INSendMessageIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method if your app supports the sending messages to named groups. A group may be specified instead of, or in addition to, individual recipients.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution with the [`NSString`](../../Foundation/nsstring.md) object that contains the name of the group recognized by your app.

## See Also

### Deprecated Methods
- [func resolveRecipients(for: INSendMessageIntent, with: ([INPersonResolutionResult]) -> Void)](./resolverecipients%28for,with%29-2yejx.md)
  Resolves the recipients of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolvegroupname(for:with:))*