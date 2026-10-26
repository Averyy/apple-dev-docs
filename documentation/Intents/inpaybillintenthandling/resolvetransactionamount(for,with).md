# resolveTransactionAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the amount to pay toward the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionAmount(for intent: INPayBillIntent, with completion: @escaping @Sendable (INPaymentAmountResolutionResult) -> Void)
```

```swift
optional func resolveTransactionAmount(for intent: INPayBillIntent) async -> INPaymentAmountResolutionResult
```

```objc
- (void) resolveTransactionAmountForPayBill:(INPayBillIntent *) intent withCompletion:(void (^)(INPaymentAmountResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the precise amount of the bill. The [`transactionAmount`](../inpaybillintent/transactionamount.md) property of the intent contains information about how much the user wants to pay, which might be a precise amount or might be a relative amount such as the minimum due or the current balance. If a precise amount wasn’t specified, use the details provided by the payee to fill in the precise amount in the [`INPaymentAmount`](../inpaymentamount.md) object you create. For example, if the user asks to pay the minimum due and the payee indicates that the minimum due is $25, include both values in the resulting [`INPaymentAmount`](../inpaymentamount.md) object.

Return a successful resolution if you’re able to identify the payment amount. Use other resolutions to prompt the user for more information if you’re unable to determine the precise amount to apply to the bill.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPaymentAmount`](../inpaymentamount.md) object containing the amount that the user intends to pay. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveBillPayee(for: INPayBillIntent, with: (INBillPayeeResolutionResult) -> Void)](./resolvebillpayee%28for,with%29.md)
  Resolves the entity that originated the bill.
- [func resolveBillType(for: INPayBillIntent, with: (INBillTypeResolutionResult) -> Void)](./resolvebilltype%28for,with%29.md)
  Resolves the type of the bill.
- [func resolveFromAccount(for: INPayBillIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that provides the funds for paying the bill.
- [func resolveDueDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolveduedate%28for,with%29.md)
  Resolves the due date of the bill.
- [func resolveTransactionScheduledDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date for the payment to occur.
- [func resolveTransactionNote(for: INPayBillIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/resolvetransactionamount(for:with:))*