# resolvePayee(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the recipient for a payment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolvePayee(for intent: INSendPaymentIntent, with completion: @escaping @Sendable (INSendPaymentPayeeResolutionResult) -> Void)
```

```swift
optional func resolvePayee(for intent: INSendPaymentIntent) async -> INSendPaymentPayeeResolutionResult
```

```objc
- (void) resolvePayeeForSendPayment:(INSendPaymentIntent *) intent completion:(void (^)(INSendPaymentPayeeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to determine whether you can send funds to the designated recipient. Use the provided payee information in the intent object to locate the corresponding user in your app. Always strive toward a successful resolution to a specific user, but always ask for confirmation of the selected user if there is some uncertainty.

If multiple users match the provided payee information, you might ask for disambiguation of the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider a different resolution.

If you identify a user but there is a problem in sending funds to that user, use the [`unsupported(forReason:)`](../insendpaymentpayeeresolutionresult/unsupported%28forreason%29.md) method to create a [`INSendPaymentPayeeResolutionResult`](../insendpaymentpayeeresolutionresult.md) object that indicates you can’t the payee.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INPerson`](../inperson.md) object containing detailed information about the user you identified. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INSendPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-75c7o.md)
  Resolves the amount of currency to transfer.
- [func resolveNote(for: INSendPaymentIntent, with: (INStringResolutionResult) -> Void)](./resolvenote%28for,with%29.md)
  Resolves the notes associated with the transaction.
- [func resolvePayee(for: INSendPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayee%28for,with%29-1kh1g.md)
  Called when you need to resolve the recipient of the funds.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-9vd94.md)
  Called when you need to resolve the currency amount to be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling/resolvepayee(for:with:)-3otmy)*