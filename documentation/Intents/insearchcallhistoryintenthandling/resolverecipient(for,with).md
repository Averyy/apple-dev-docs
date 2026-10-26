# resolveRecipient(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the search criteria for the recipients.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveRecipient(for intent: INSearchCallHistoryIntent, with completion: @escaping @Sendable (INPersonResolutionResult) -> Void)
```

```swift
optional func resolveRecipient(for intent: INSearchCallHistoryIntent) async -> INPersonResolutionResult
```

```objc
- (void) resolveRecipientForSearchCallHistory:(INSearchCallHistoryIntent *) intent withCompletion:(void (^)(INPersonResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to verify the identity of any intended contacts in the search parameters. Always strive toward a successful resolution to a specific user, but feel free to ask for confirmation of the selected user if there’s some uncertainty.

If you find multiple users matching the same name, consider asking the user to disambiguate from among the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider a different resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution that includes the [`INPerson`](../inperson.md) object that you can use to identify the user later.

## See Also

### Resolving the Intent Parameters
- [func resolveCallTypes(for: INSearchCallHistoryIntent, with: (INCallRecordTypeOptionsResolutionResult) -> Void)](./resolvecalltypes%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveCallType(for: INSearchCallHistoryIntent, with: (INCallRecordTypeResolutionResult) -> Void)](./resolvecalltype%28for,with%29.md)
  Resolves the search criteria for the call type.
- [func resolveDateCreated(for: INSearchCallHistoryIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvedatecreated%28for,with%29.md)
  Resolves the range of dates for the search.
- [func resolveUnseen(for: INSearchCallHistoryIntent, with: (INBooleanResolutionResult) -> Void)](./resolveunseen%28for,with%29.md)
  Resolves whether you can search for calls that the user hasn’t yet seen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling/resolverecipient(for:with:))*