# resolveDueDate(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the due date of the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveDueDate(for intent: INPayBillIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveDueDate(for intent: INPayBillIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveDueDateForPayBill:(INPayBillIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the due date of the bill. The due date is usually provided by the bill payee and reflects the date after which the institution may apply late fees. If the intent doesn’t contain the due date, retrieve the due date from your own internal records and return it as part of your successful resolution. Providing the due date is always encouraged because it helps the user determine the date on which to schedule payment.

If the payee didn’t provide you with a due date, you can return a resolution indicating it the value isn’t required. However, you might want to verify that the user supplied a date on which to schedule the payment and that the provided date isn’t too far in the future.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the date range that identifies when the bill is due. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INPayBillIntent, with: (INBillPayeeResolutionResult) -> Void)](./resolvebillpayee%28for,with%29.md)
  Resolves the entity that originated the bill.
- [func resolveBillType(for: INPayBillIntent, with: (INBillTypeResolutionResult) -> Void)](./resolvebilltype%28for,with%29.md)
  Resolves the type of the bill.
- [func resolveFromAccount(for: INPayBillIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that provides the funds for paying the bill.
- [func resolveTransactionAmount(for: INPayBillIntent, with: (INPaymentAmountResolutionResult) -> Void)](./resolvetransactionamount%28for,with%29.md)
  Resolves the amount to pay toward the bill.
- [func resolveTransactionScheduledDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date for the payment to occur.
- [func resolveTransactionNote(for: INPayBillIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/resolveduedate(for:with:))*