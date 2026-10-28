# resolveBillPayee(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the entity that originated the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveBillPayee(for intent: INPayBillIntent, with completion: @escaping @Sendable (INBillPayeeResolutionResult) -> Void)
```

```swift
optional func resolveBillPayee(for intent: INPayBillIntent) async -> INBillPayeeResolutionResult
```

```objc
- (void) resolveBillPayeeForPayBill:(INPayBillIntent *) intent withCompletion:(void (^)(INBillPayeeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify the identify of the payee in your app. The payee represents the entity that provided the bill to the user. Siri puts any payee-related information into the [`billPayee`](../inpaybillintent/billpayee.md) property of the intent object. Use that information to match the payee’s nickname or organization to one of the entities that the user registered with your app. (You should also use the information in the [`billType`](../inpaybillintent/billtype.md) property to verify that you’re scheduling payment for the correct bill). Always strive toward a successful resolution of the payee, but feel free to return a different resolution if you can’t locate the payee or you aren’t sure which bill the user intended to pay.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INBillPayee`](../inbillpayee.md) object that identifies the entity to receive the funds. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
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
- [func resolveTransactionNote(for: INPayBillIntent, with: (INStringResolutionResult) -> Void)](./resolvetransactionnote%28for,with%29.md)
  Resolves any custom notes associated with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/resolvebillpayee(for:with:))*