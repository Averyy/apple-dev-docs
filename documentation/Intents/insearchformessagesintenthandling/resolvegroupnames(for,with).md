# resolveGroupNames(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s input when they search for messages sent to a specific group of people.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: resolveGroupNamesForSearchForMessages:withCompletion: is deprecated. Use resolveSpeakableGroupNamesForSearchForMessages:withCompletion: instead

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```swift
optional func resolveGroupNames(for intent: INSearchForMessagesIntent, with completion: @escaping @Sendable ([INStringResolutionResult]) -> Void)
```

*Mac Catalyst, visionOS*

```swift
optional func resolveGroupNames(for intent: INSearchForMessagesIntent) async -> [INStringResolutionResult]
```

```objc
- (void) resolveGroupNamesForSearchForMessages:(INSearchForMessagesIntent *) intent withCompletion:(void (^)(NSArray<INStringResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResults**: The object containing the details of your proposed resolution. For successful resolutions, create one or more resolution objects with the [`NSString`](../../Foundation/nsstring.md) objects that contain the recognized group names.

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
- [func resolveSpeakableGroupNames(for: INSearchForMessagesIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvespeakablegroupnames%28for,with%29.md)
  Resolves the user’s input when they search for messages sent to a specific group of people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/resolvegroupnames(for:with:))*