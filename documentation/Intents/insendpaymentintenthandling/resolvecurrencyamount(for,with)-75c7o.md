# resolveCurrencyAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the amount of currency to transfer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveCurrencyAmount(for intent: INSendPaymentIntent, with completion: @escaping @Sendable (INSendPaymentCurrencyAmountResolutionResult) -> Void)
```

```swift
optional func resolveCurrencyAmount(for intent: INSendPaymentIntent) async -> INSendPaymentCurrencyAmountResolutionResult
```

```objc
- (void) resolveCurrencyAmountForSendPayment:(INSendPaymentIntent *) intent completion:(void (^)(INSendPaymentCurrencyAmountResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify that you can transfer money in the intended currency. If the amount is outside of the minimum or maximum transaction amount supported by your app, return a successful result and use your response object to communicate that the amount is below the minimum or above the maximum amount. Do not use this method to validate that the user’s account contains the specified amount.

If you identify a currency amount but there is a problem in sending the funds, use the [`unsupported(forReason:)`](../insendpaymentcurrencyamountresolutionresult/unsupported%28forreason%29.md) method to create a [`INSendPaymentCurrencyAmountResolutionResult`](../insendpaymentcurrencyamountresolutionresult.md) object that indicates the reason you couldn’t send the amount.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INCurrencyAmount`](../incurrencyamount.md) object containing the amount you plan to transfer. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayee(for: INSendPaymentIntent, with: (INSendPaymentPayeeResolutionResult) -> Void)](./resolvepayee%28for,with%29-3otmy.md)
  Resolves the recipient for a payment.
- [func resolveNote(for: INSendPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the transaction.
- [func resolvePayee(for: INSendPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayee%28for,with%29-1kh1g.md)
  Called when you need to resolve the recipient of the funds.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-9vd94.md)
  Called when you need to resolve the currency amount to be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling/resolvecurrencyamount(for:with:)-75c7o)*