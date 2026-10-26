# resolveToAccount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user account that’s the destination of the funds.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveToAccount(for intent: INTransferMoneyIntent, with completion: @escaping @Sendable (INPaymentAccountResolutionResult) -> Void)
```

```swift
optional func resolveToAccount(for intent: INTransferMoneyIntent) async -> INPaymentAccountResolutionResult
```

```objc
- (void) resolveToAccountForTransferMoney:(INTransferMoneyIntent *) intent withCompletion:(void (^)(INPaymentAccountResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the user account that’s the destination for the funds. Use this method to verify that the specified account exists and is able to receive the transferred funds. The [`toAccount`](../intransfermoneyintent/toaccount.md) property of the intent object contains any information provided by the user about which account to use.

Return a successful resolution if you’re able to verify the existence of the account. If the user doesn’t have any accounts to facilitate a transfer, return a successful resolution or indicate that the account isn’t required and then use the [`confirm(intent:completion:)`](./confirm%28intent,completion%29.md) method to report an appropriate error. If the user has multiple accounts that match the provided information, either pick one and ask for confirmation or use the [`disambiguation(with:)`](../inpaymentamountresolutionresult/disambiguation%28with%29.md) method to create a resolution that prompts the user to select an account.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPaymentAccount`](../inpaymentaccount.md) object that identifies the user’s account. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveFromAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that’s the source of the funds.
- [func resolveTransactionAmount(for: INTransferMoneyIntent, with: (INPaymentAmountResolutionResult) -> Void)](./resolvetransactionamount%28for,with%29.md)
  Resolves the amount that the user wants to transfer.
- [func resolveTransactionScheduledDate(for: INTransferMoneyIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvetransactionscheduleddate%28for,with%29.md)
  Resolves the date on which the transfer is to occur.
- [func resolveTransactionNote(for: INTransferMoneyIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/resolvetoaccount(for:with:))*