# resolveDueDateRange(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the due date to use during your search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveDueDateRange(for intent: INSearchForBillsIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveDueDateRange(for intent: INSearchForBillsIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveDueDateRangeForSearchForBills:(INSearchForBillsIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any questions about the due date for a bill. Use the [`dueDateRange`](../insearchforbillsintent/duedaterange.md) property of the intent object to identify the date range to search. If a date range is available and usable, return a successful resolution with that date range. You can also make adjustments to the date range as needed and ask the user for confirmation.

If the user didn’t specify a date range, return a resolution of not required from this method. When the user didn’t specify a date range, you must decide how you want to filter results when performing the subsequent search. For example, you might want to return only the currently due bills. Alternatively, you could return all bills from the past month or from the past year.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object containing the [`INDateComponentsRange`](../indatecomponentsrange.md) object that you intend to use during the search.

## See Also

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INSearchForBillsIntent, with: (INBillPayeeResolutionResult) -> Void)](./resolvebillpayee%28for,with%29.md)
  Resolves the payee to use during your search.
- [func resolveBillType(for: INSearchForBillsIntent, with: (INBillTypeResolutionResult) -> Void)](./resolvebilltype%28for,with%29.md)
  Resolves the bill type to use during your search.
- [func resolvePaymentDateRange(for: INSearchForBillsIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvepaymentdaterange%28for,with%29.md)
  Resolves the payment date to use during your search.
- [func resolveStatus(for: INSearchForBillsIntent, with: (INPaymentStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the bill status to use during your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/resolveduedaterange(for:with:))*