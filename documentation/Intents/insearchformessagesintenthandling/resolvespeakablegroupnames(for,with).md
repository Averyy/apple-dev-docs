# resolveSpeakableGroupNames(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s input when they search for messages sent to a specific group of people.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveSpeakableGroupNames(for intent: INSearchForMessagesIntent, with completion: @escaping @Sendable ([INSpeakableStringResolutionResult]) -> Void)
```

```swift
optional func resolveSpeakableGroupNames(for intent: INSearchForMessagesIntent) async -> [INSpeakableStringResolutionResult]
```

```objc
- (void) resolveSpeakableGroupNamesForSearchForMessages:(INSearchForMessagesIntent *) intent withCompletion:(void (^)(NSArray<INSpeakableStringResolutionResult *> *resolutionResults)) completion;
```

## Discussion

This method resolves the names of any groups that were recipients of the messages.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object that contains the details of your proposed resolution. For successful resolutions, create one or more resolution objects with the [`NSString`](../../Foundation/nsstring.md) objects that contain the recognized group names.

## See Also

### Resolving the Intent Parameters
- [func resolveRecipients(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./resolverecipients%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to specific people.
- [func resolveSenders(for: INSearchForMessagesIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvesenders%28for,with%29.md)
  Resolves the user’s input when they search for messages sent by specific people.
- [func resolveAttributes(for: INSearchForMessagesIntent, with: (INMessageAttributeOptionsResolutionResult) -> Void)](./resolveattributes%28for,with%29.md)
  Resolves the user’s input when they search for messages with specific attributes.
- [func resolveDateTimeRange(for: INSearchForMessagesIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatetimerange%28for,with%29.md)
  Resolves the user’s input when they search for messages sent in a specific time period.
- [func resolveGroupNames(for: INSearchForMessagesIntent, with: ([INStringResolutionResult]) -> Void)](./resolvegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/resolvespeakablegroupnames(for:with:))*