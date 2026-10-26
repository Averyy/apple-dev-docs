# resolveTransactionAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the amount that the user wants to transfer.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionAmount(for intent: INTransferMoneyIntent, with completion: @escaping @Sendable (INPaymentAmountResolutionResult) -> Void)
```

```swift
optional func resolveTransactionAmount(for intent: INTransferMoneyIntent) async -> INPaymentAmountResolutionResult
```

```objc
- (void) resolveTransactionAmountForTransferMoney:(INTransferMoneyIntent *) intent withCompletion:(void (^)(INPaymentAmountResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the amount of money the user wants to transfer. The [`transactionAmount`](../intransfermoneyintent/transactionamount.md) property of the intent contains information about how much the user wants to transfer. Return a successful resolution if you’re able to transfer the specified amount. If the amount exceeds the maximum or minimum amount allowed by your app, return an adjusted amount and ask for confirmation.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPaymentAmount`](../inpaymentamount.md) object containing the amount to transfer. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveFromAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that’s the source of the funds.
- [func resolveToAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvetoaccount%28for,with%29.md)
  Resolves the user account that’s the destination of the funds.
- [func resolveTransactionScheduledDate(for: INTransferMoneyIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date on which the transfer is to occur.
- [func resolveTransactionNote(for: INTransferMoneyIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/resolvetransactionamount(for:with:))*