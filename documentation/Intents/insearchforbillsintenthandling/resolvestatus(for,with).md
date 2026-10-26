# resolveStatus(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the bill status to use during your search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveStatus(for intent: INSearchForBillsIntent, with completion: @escaping @Sendable (INPaymentStatusResolutionResult) -> Void)
```

```swift
optional func resolveStatus(for intent: INSearchForBillsIntent) async -> INPaymentStatusResolutionResult
```

```objc
- (void) resolveStatusForSearchForBills:(INSearchForBillsIntent *) intent withCompletion:(void (^)(INPaymentStatusResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve any questions about the status of a bill. Use the status property of the intent object to identify the status type to search. If the specified status type is one that your app supports, return a successful resolution with that type.

If the status type is [`INPaymentStatus.unknown`](../inpaymentstatus/unknown.md), return a resolution of not required from this method. When the status type is unknown, don’t filter the subsequent search results based on the bill’s current status. Instead, return all bills whether they’re pending, completed, canceled, or failed.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object containing the [`INPaymentStatus`](../inpaymentstatus.md) value that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INSearchForBillsIntent, with: (INBillPayeeResolutionResult) -> Void)](./resolvebillpayee%28for,with%29.md)
  Resolves the payee to use during your search.
- [func resolveBillType(for: INSearchForBillsIntent, with: (INBillTypeResolutionResult) -> Void)](./resolvebilltype%28for,with%29.md)
  Resolves the bill type to use during your search.
- [func resolveDueDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolveduedaterange%28for,with%29.md)
  Resolves the due date to use during your search.
- [func resolvePaymentDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvepaymentdaterange%28for,with%29.md)
  Resolves the payment date to use during your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/resolvestatus(for:with:))*