# resolveBillType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the bill type to use during your search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveBillType(for intent: INSearchForBillsIntent, with completion: @escaping @Sendable (INBillTypeResolutionResult) -> Void)
```

```swift
optional func resolveBillType(for intent: INSearchForBillsIntent) async -> INBillTypeResolutionResult
```

```objc
- (void) resolveBillTypeForSearchForBills:(INSearchForBillsIntent *) intent withCompletion:(void (^)(INBillTypeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve any questions about the bill type for the search. Use the [`billType`](../insearchforbillsintent/billtype.md) property in the intent object to identify the requested bill type. If the bill type is [`INBillType.unknown`](../inbilltype/unknown.md), you may return a resolution of success with that value or you may return a resolution of not required. In either case, when the bill type is [`INBillType.unknown`](../inbilltype/unknown.md), your subsequent search should return all bills regardless of their type.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object containing the [`INBillType`](../inbilltype.md) value that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INSearchForBillsIntent, with: (INBillPayeeResolutionResult) -> Void)](./resolvebillpayee%28for,with%29.md)
  Resolves the payee to use during your search.
- [func resolveDueDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolveduedaterange%28for,with%29.md)
  Resolves the due date to use during your search.
- [func resolvePaymentDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvepaymentdaterange%28for,with%29.md)
  Resolves the payment date to use during your search.
- [func resolveStatus(for: INSearchForBillsIntent, with: (INPaymentStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the bill status to use during your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/resolvebilltype(for:with:))*