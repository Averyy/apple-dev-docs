# resolvePayer(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the person to receive the payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolvePayer(for intent: INRequestPaymentIntent, with completion: @escaping @Sendable (INRequestPaymentPayerResolutionResult) -> Void)
```

```swift
optional func resolvePayer(for intent: INRequestPaymentIntent) async -> INRequestPaymentPayerResolutionResult
```

```objc
- (void) resolvePayerForRequestPayment:(INRequestPaymentIntent *) intent completion:(void (^)(INRequestPaymentPayerResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to identify the intended recipient of the request. Always strive toward a successful resolution to a specific user, but ask for confirmation of the selected user if there is some uncertainty.

If multiple users match the provided payer information, you can ask for disambiguation of the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users that match the payer information, consider another resolution.

If you identify a user but there is a problem in requesting funds from that user, use the [`unsupported(forReason:)`](../inrequestpaymentpayerresolutionresult/unsupported%28forreason%29.md) method to create a [`INRequestPaymentPayerResolutionResult`](../inrequestpaymentpayerresolutionresult.md) object that indicates the reason why you couldnt use the payer.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPerson`](../inperson.md) object containing detailed information about the user you identified. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INRequestPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-1it85.md)
  Resolves the amount of money requested.
- [func resolveNote(for: INRequestPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the request.
- [func resolvePayer(for: INRequestPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayer%28for,with%29-qp42.md)
  Called when you need to resolve the person who will receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-78c2m.md)
  Called when you need to resolve the amount of money being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling/resolvepayer(for:with:)-4xu87)*