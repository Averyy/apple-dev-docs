# resolveCurrencyAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the amount of money requested.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveCurrencyAmount(for intent: INRequestPaymentIntent, with completion: @escaping @Sendable (INRequestPaymentCurrencyAmountResolutionResult) -> Void)
```

```swift
optional func resolveCurrencyAmount(for intent: INRequestPaymentIntent) async -> INRequestPaymentCurrencyAmountResolutionResult
```

```objc
- (void) resolveCurrencyAmountForRequestPayment:(INRequestPaymentIntent *) intent completion:(void (^)(INRequestPaymentCurrencyAmountResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify the requested currency amount. If the amount is outside of the minimum or maximum transaction amount supported by your app, return a successful result and use your response object to communicate that the amount is below the minimum or above the maximum amount. Do not use this method to validate that the payer’s account contains the necessary funds to complete the transaction.

If you identify a currency amount but there is a problem in requesting the funds, use the [`unsupported(forReason:)`](../inrequestpaymentcurrencyamountresolutionresult/unsupported%28forreason%29.md) method to create a [`INRequestPaymentCurrencyAmountResolutionResult`](../inrequestpaymentcurrencyamountresolutionresult.md) object indicating the reason why you can’t request the amount.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INCurrencyAmount`](../incurrencyamount.md) object containing the requested amount. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayer(for: INRequestPaymentIntent, with: (INRequestPaymentPayerResolutionResult) -> Void)](./resolvepayer%28for,with%29-4xu87.md)
  Resolves the person to receive the payment request.
- [func resolveNote(for: INRequestPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the request.
- [func resolvePayer(for: INRequestPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayer%28for,with%29-qp42.md)
  Called when you need to resolve the person who will receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-78c2m.md)
  Called when you need to resolve the amount of money being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling/resolvecurrencyamount(for:with:)-1it85)*