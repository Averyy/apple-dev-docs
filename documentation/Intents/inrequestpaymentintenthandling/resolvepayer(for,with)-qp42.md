# resolvePayer(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Called when you need to resolve the person who will receive the payment request.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 4.0

> **Deprecated**: Use [`resolvePayer(for:with:)`](./resolvepayer%28for,with%29-4xu87.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```swift
optional func resolvePayer(for intent: INRequestPaymentIntent, with completion: @escaping @Sendable (INPersonResolutionResult) -> Void)
```

*Mac Catalyst, visionOS*

```swift
optional func resolvePayer(for intent: INRequestPaymentIntent) async -> INPersonResolutionResult
```

```objc
- (void) resolvePayerForRequestPayment:(INRequestPaymentIntent *) intent withCompletion:(void (^)(INPersonResolutionResult *resolutionResult)) completion;
```

#### Discussion

Use the `intent` object to identify intended recipient of the request. Always strive toward a successful resolution to a specific user, but feel free to ask for confirmation of the selected user if there is some uncertainty.

If multiple users match the provided payer information, you can ask for disambiguation of the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users that match the payer information, consider another resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPerson`](../inperson.md) object containing detailed information about the user you identified. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayer(for: INRequestPaymentIntent, with: (INRequestPaymentPayerResolutionResult) -> Void)](./resolvepayer%28for,with%29-4xu87.md)
  Resolves the person to receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INRequestPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-1it85.md)
  Resolves the amount of money requested.
- [func resolveNote(for: INRequestPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-78c2m.md)
  Called when you need to resolve the amount of money being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling/resolvepayer(for:with:)-qp42)*