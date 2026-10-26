# resolveDateTimeRange(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s input when they search for messages sent in a specific time period.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveDateTimeRange(for intent: INSearchForMessagesIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveDateTimeRange(for intent: INSearchForMessagesIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveDateTimeRangeForSearchForMessages:(INSearchForMessagesIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

#### Discussion

This method resolves the dates used to search for messages.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For successful resolutions, create a resolution with the date range that you are able to search. You may specify a value different than the one originally specified in the intent.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./resolverecipients%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to specific people.
- [func resolveSenders(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvesenders%28for,with%29.md)
  Resolves the user’s input when they search for messages sent by specific people.
- [func resolveAttributes(for: INSearchForMessagesIntent, with: (INMessageAttributeOptionsResolutionResult) -> Void)](./resolveattributes%28for,with%29.md)
  Resolves the user’s input when they search for messages with specific attributes.
- [func resolveSpeakableGroupNames(for: INSearchForMessagesIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvespeakablegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.
- [func resolveGroupNames(for: INSearchForMessagesIntent, with: ([INStringResolutionResult]) -> Void)](./resolvegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/resolvedatetimerange(for:with:))*