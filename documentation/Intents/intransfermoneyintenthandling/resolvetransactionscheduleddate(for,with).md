# resolveTransactionScheduledDate(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the date on which the transfer is to occur.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveTransactionScheduledDate(for intent: INTransferMoneyIntent, with completion: @escaping @Sendable (INDateComponentsRangeResolutionResult) -> Void)
```

```swift
optional func resolveTransactionScheduledDate(for intent: INTransferMoneyIntent) async -> INDateComponentsRangeResolutionResult
```

```objc
- (void) resolveTransactionScheduledDateForTransferMoney:(INTransferMoneyIntent *) intent withCompletion:(void (^)(INDateComponentsRangeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the date on which to transfer money between the user’s accounts. Adjust the date, as needed, to ensure that you can perform the transfer. If the user doesn’t specify a date, assume that the user wants to transfer the money immediately.

Return a successful resolution if you’re able to schedule the transfer on the requested date, or if there’s no date and you can perform the transaction immediately. If the user-specified date falls on a banking holiday or on a date when you’d be unable to schedule the transaction, suggest a different date and ask the user for confirmation or use a disambiguation resolution to ask the user to select from two or three alternative dates.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the date range for the transfer to occur. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveFromAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvefromaccount%28for,with%29.md)
  Resolves the user account that’s the source of the funds.
- [func resolveToAccount(for: INTransferMoneyIntent, with: (INPaymentAccountResolutionResult) -> Void)](./resolvetoaccount%28for,with%29.md)
  Resolves the user account that’s the destination of the funds.
- [func resolveTransactionAmount(for: INTransferMoneyIntent, with: (INPaymentAmountResolutionResult) -> Void)](./resolvetransactionamount%28for,with%29.md)
  Resolves the amount that the user wants to transfer.
- [func resolveTransactionNote(for: INTransferMoneyIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/resolvetransactionscheduleddate(for:with:))*