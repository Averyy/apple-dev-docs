# resolveBillPayee(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the payee to use during your search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveBillPayee(for intent: INSearchForBillsIntent, with completion: @escaping @Sendable (INBillPayeeResolutionResult) -> Void)
```

```swift
optional func resolveBillPayee(for intent: INSearchForBillsIntent) async -> INBillPayeeResolutionResult
```

```objc
- (void) resolveBillPayeeForSearchForBills:(INSearchForBillsIntent *) intent withCompletion:(void (^)(INBillPayeeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any questions about the payee to use during the search. Use the [`billPayee`](../insearchforbillsintent/billpayee.md) property in the `intent` object to identify the requested payee. The payee represents the entity that provided the bill to the user. The user must register all payees in advance.

If the intent doesn’t contain any payee information, return a resolution of not required from this method. During the subsequent search, don’t filter the search results based on the payee.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object containing the [`INBillPayee`](../inbillpayee.md) object that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveBillType(for: INSearchForBillsIntent, with: (INBillTypeResolutionResult) -> Void)](./resolvebilltype%28for,with%29.md)
  Resolves the bill type to use during your search.
- [func resolveDueDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolveduedaterange%28for,with%29.md)
  Resolves the due date to use during your search.
- [func resolvePaymentDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvepaymentdaterange%28for,with%29.md)
  Resolves the payment date to use during your search.
- [func resolveStatus(for: INSearchForBillsIntent, with: (INPaymentStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the bill status to use during your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/resolvebillpayee(for:with:))*