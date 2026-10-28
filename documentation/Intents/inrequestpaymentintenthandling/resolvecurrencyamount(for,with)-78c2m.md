# resolveCurrencyAmount(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Called when you need to resolve the amount of money being requested.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`resolveCurrencyAmount(for:with:)`](./resolvecurrencyamount%28for,with%29-1it85.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```swift
optional func resolveCurrencyAmount(for intent: INRequestPaymentIntent, with completion: @escaping @Sendable (INCurrencyAmountResolutionResult) -> Void)
```

*Mac Catalyst, visionOS*

```swift
optional func resolveCurrencyAmount(for intent: INRequestPaymentIntent) async -> INCurrencyAmountResolutionResult
```

```objc
- (void) resolveCurrencyAmountForRequestPayment:(INRequestPaymentIntent *) intent withCompletion:(void (^)(INCurrencyAmountResolutionResult *resolutionResult)) completion;
```

## Discussion

Use this method to verify that the request can be made in the intended currency. If the amount is outside of the minimum or maximum transaction amount supported by your app, return a successful result and use your response object to communicate that the amount is below the minimum or above the maximum amount. Do not use this method to validate that the payer’s account contains the necessary funds to complete the transaction.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INCurrencyAmount`](../incurrencyamount.md) object containing the requested amount. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayer(for: INRequestPaymentIntent, with: (INRequestPaymentPayerResolutionResult) -> Void)](./resolvepayer%28for,with%29-4xu87.md)
  Resolves the person to receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INRequestPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-1it85.md)
  Resolves the amount of money requested.
- [func resolveNote(for: INRequestPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the request.
- [func resolvePayer(for: INRequestPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayer%28for,with%29-qp42.md)
  Called when you need to resolve the person who will receive the payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling/resolvecurrencyamount(for:with:)-78c2m)*