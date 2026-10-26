# resolveSenders(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s input when they search for messages sent by specific people.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveSenders(for intent: INSearchForMessagesIntent, with completion: @escaping @Sendable ([INPersonResolutionResult]) -> Void)
```

```swift
optional func resolveSenders(for intent: INSearchForMessagesIntent) async -> [INPersonResolutionResult]
```

```objc
- (void) resolveSendersForSearchForMessages:(INSearchForMessagesIntent *) intent withCompletion:(void (^)(NSArray<INPersonResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

This method resolves the `sender` search parameter. Use the information in the `intent` object to identify the corresponding users in your app. Always strive toward a successful resolution of the specified users, but ask for confirmation for one or more users if there is some uncertainty.

If you find multiple users matching the same name, consider asking the user to disambiguate from among the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider a different resolution.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object that contains the details of your proposed resolution. For successful resolutions, create one or more resolution objects that include the [`INPerson`](../inperson.md) objects representing the message senders to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./resolverecipients%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to specific people.
- [func resolveAttributes(for: INSearchForMessagesIntent, with: (INMessageAttributeOptionsResolutionResult) -> Void)](./resolveattributes%28for,with%29.md)
  Resolves the user’s input when they search for messages with specific attributes.
- [func resolveDateTimeRange(for: INSearchForMessagesIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatetimerange%28for,with%29.md)
  Resolves the user’s input when they search for messages sent in a specific time period.
- [func resolveSpeakableGroupNames(for: INSearchForMessagesIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvespeakablegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.
- [func resolveGroupNames(for: INSearchForMessagesIntent, with: ([INStringResolutionResult]) -> Void)](./resolvegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/resolvesenders(for:with:))*