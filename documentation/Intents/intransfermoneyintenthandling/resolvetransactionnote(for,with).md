# resolveTransactionNote(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves any custom notes associated with the transaction.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionNote(for intent: INTransferMoneyIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveTransactionNote(for intent: INTransferMoneyIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveTransactionNoteForTransferMoney:(INTransferMoneyIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
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
- [func resolveFromAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that’s the source of the funds.
- [func resolveToAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvetoaccount%28for,with%29.md)
  Resolves the user account that’s the destination of the funds.
- [func resolveTransactionAmount(for: INTransferMoneyIntent, with: (INPaymentAmountResolutionResult) -> Void)](./resolvetransactionamount%28for,with%29.md)
  Resolves the amount that the user wants to transfer.
- [func resolveTransactionScheduledDate(for: INTransferMoneyIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date on which the transfer is to occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/resolvetransactionnote(for:with:))*