# resolveCallType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the search criteria for the call type.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveCallType(for intent: INSearchCallHistoryIntent, with completion: @escaping @Sendable (INCallRecordTypeResolutionResult) -> Void)
```

```swift
optional func resolveCallType(for intent: INSearchCallHistoryIntent) async -> INCallRecordTypeResolutionResult
```

```objc
- (void) resolveCallTypeForSearchCallHistory:(INSearchCallHistoryIntent *) intent withCompletion:(void (^)(INCallRecordTypeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to let SiriKit know which types of calls you can search. Your implementation should provide a successful resolution for the call types you support and an unsupported resolution for any call types you don’t support.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution result that contains the types of calls you’re able to search.

## See Also

### Resolving the Intent Parameters
- [func resolveCallTypes(for: INSearchCallHistoryIntent, with: (INCallRecordTypeOptionsResolutionResult) -> Void)](./resolvecalltypes%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveRecipient(for: INSearchCallHistoryIntent, with: (INPersonResolutionResult) -> Void)](./resolverecipient%28for,with%29.md)
  Resolves the search criteria for the recipients.
- [func resolveDateCreated(for: INSearchCallHistoryIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatecreated%28for,with%29.md)
  Resolves the range of dates for the search.
- [func resolveUnseen(for: INSearchCallHistoryIntent, with: (INBooleanResolutionResult) -> Void)](./resolveunseen%28for,with%29.md)
  Resolves whether you can search for calls that the user hasn’t yet seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling/resolvecalltype(for:with:))*