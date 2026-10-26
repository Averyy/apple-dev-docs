# resolveRecipients(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the recipients of the message.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 12.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`resolveRecipients(for:with:)`](./resolverecipients%28for,with%29-609yw.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func resolveRecipients(for intent: INSendMessageIntent, with completion: @escaping @Sendable ([INPersonResolutionResult]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func resolveRecipients(for intent: INSendMessageIntent) async -> [INPersonResolutionResult]
```

```objc
- (void) resolveRecipientsForSendMessage:(INSendMessageIntent *) intent withCompletion:(void (^)(NSArray<INPersonResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

Use this method to verify the identity of the intended recipients. Always strive toward a successful resolution of the specified users, but feel free to ask for confirmation for one or more users if there is some uncertainty.

If multiple users match the a single recipient, you might ask for disambiguation of the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider another resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object containing the details of your proposed resolution. For each successful resolution, create a resolution object that includes the [`INPerson`](../inperson.md) object representing the user who will receive the message.

## See Also

### Deprecated Methods
- [func resolveGroupName(for: INSendMessageIntent, with: (INStringResolutionResult) -> Void)](./resolvegroupname%28for,with%29.md)
  Resolves the name of the group receiving the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/resolverecipients(for:with:)-2yejx)*