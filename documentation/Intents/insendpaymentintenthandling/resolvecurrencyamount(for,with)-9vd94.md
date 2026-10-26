# resolveCurrencyAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Called when you need to resolve the currency amount to be transferred.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`resolveCurrencyAmount(for:with:)`](./resolvecurrencyamount%28for,with%29-75c7o.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```swift
optional func resolveCurrencyAmount(for intent: INSendPaymentIntent, with completion: @escaping @Sendable (INCurrencyAmountResolutionResult) -> Void)
```

*Mac Catalyst, visionOS*

```swift
optional func resolveCurrencyAmount(for intent: INSendPaymentIntent) async -> INCurrencyAmountResolutionResult
```

```objc
- (void) resolveCurrencyAmountForSendPayment:(INSendPaymentIntent *) intent withCompletion:(void (^)(INCurrencyAmountResolutionResult *resolutionResult)) completion;
```

#### Discussion

Use this method to verify that you can transfer money in the intended currency. If the amount is outside of the minimum or maximum transaction amount supported by your app, return a successful result and use your response object to communicate that the amount is below the minimum or above the maximum amount. Do not use this method to validate that the user’s account contains the specified amount.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INCurrencyAmount`](../incurrencyamount.md) object containing the amount you plan to transfer. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayee(for: INSendPaymentIntent, with: (INSendPaymentPayeeResolutionResult) -> Void)](./resolvepayee%28for,with%29-3otmy.md)
  Resolves the recipient for a payment.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INSendPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-75c7o.md)
  Resolves the amount of currency to transfer.
- [func resolveNote(for: INSendPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the transaction.
- [func resolvePayee(for: INSendPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayee%28for,with%29-1kh1g.md)
  Called when you need to resolve the recipient of the funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling/resolvecurrencyamount(for:with:)-9vd94)*