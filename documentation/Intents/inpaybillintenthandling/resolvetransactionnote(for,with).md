# resolveTransactionNote(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves any custom notes associated with the transaction.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionNote(for intent: INPayBillIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveTransactionNote(for intent: INPayBillIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveTransactionNoteForPayBill:(INPayBillIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve whether you can record notes with the transaction. Return a successful resolution if you can record the note with the transaction. If your app doesn’t store notes with transactions, return a resolution indicating that the value isn’t required.

You’re strongly encouraged to record notes with your app’s financial transactions. Notes are optional but are helpful for users to organize their transactions.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the string containing any notes to include with the transaction. This parameter must not be `nil`.

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
- [func resolveTransactionScheduledDate(for: INPayBillIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date for the payment to occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/resolvetransactionnote(for:with:))*