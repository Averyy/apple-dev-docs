# resolveDateCreated(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the range of dates for the search.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveDateCreated(for intent: INSearchCallHistoryIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveDateCreated(for intent: INSearchCallHistoryIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveDateCreatedForSearchCallHistory:(INSearchCallHistoryIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

#### Discussion

When resolving the set of dates, always strive toward a successful resolution, but feel free to return a different result where appropriate. For example, if you don’t support searching for records that are more than one year old, you could return an unsupported resolution if the user specifies a date that’s more than one year in the past.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution with the date range that you’re able to search.

## See Also

### Resolving the Intent Parameters
- [func resolveCallTypes(for: INSearchCallHistoryIntent, with: (INCallRecordTypeOptionsResolutionResult) -> Void)](./resolvecalltypes%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveCallType(for: INSearchCallHistoryIntent, with: (INCallRecordTypeResolutionResult) -> Void)](./resolvecalltype%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveRecipient(for: INSearchCallHistoryIntent, with: (INPersonResolutionResult) -> Void)](./resolverecipient%28for,with%29.md)
  Resolves the search criteria for the recipients.
- [func resolveUnseen(for: INSearchCallHistoryIntent, with: (INBooleanResolutionResult) -> Void)](./resolveunseen%28for,with%29.md)
  Resolves whether you can search for calls that the user hasn’t yet seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling/resolvedatecreated(for:with:))*