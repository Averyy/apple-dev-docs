# resolveTransactionScheduledDate(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the date for the payment to occur.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionScheduledDate(for intent: INPayBillIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveTransactionScheduledDate(for intent: INPayBillIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveTransactionScheduledDateForPayBill:(INPayBillIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the date on which to transfer money from the user’s account to the payee. The user can optionally specify a date on which to schedule payment. If the user doesn’t specify a date, assume that the user wants to pay the bill immediately. Don’t check to see if the scheduled date occurs before the bill’s due date. Instead, use this method only to identify the date on which you can perform the transaction.

Return a successful resolution if you’re able to schedule the transaction on the date requested by the user, or if you’re able to schedule the transaction immediately. If the user-specified date falls on a banking holiday or on a date when you’d be unable to schedule the transaction, suggest a different date and ask the user for confirmation or use a disambiguation resolution to ask the user to select from two or three alternative dates.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the date range of the payment’s schedule. This parameter must not be `nil`.

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
- [func resolveDueDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolveduedate%28for,with%29.md)
  Resolves the due date of the bill.
- [func resolveTransactionNote(for: INPayBillIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/resolvetransactionscheduleddate(for:with:))*