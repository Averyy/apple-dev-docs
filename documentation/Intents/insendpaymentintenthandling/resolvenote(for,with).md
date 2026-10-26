# resolveNote(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the notes associated with the transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveNote(for intent: INSendPaymentIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveNote(for intent: INSendPaymentIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveNoteForSendPayment:(INSendPaymentIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve any notes associated with the transaction.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is an [`NSString`](../../Foundation/nsstring.md) object containing the note to send with the payment. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayee(for: INSendPaymentIntent, with: (INSendPaymentPayeeResolutionResult) -> Void)](./resolvepayee%28for,with%29-3otmy.md)
  Resolves the recipient for a payment.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INSendPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-75c7o.md)
  Resolves the amount of currency to transfer.
- [func resolvePayee(for: INSendPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayee%28for,with%29-1kh1g.md)
  Called when you need to resolve the recipient of the funds.
- [func resolveCurrencyAmount(for: INSendPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-9vd94.md)
  Called when you need to resolve the currency amount to be transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling/resolvenote(for:with:))*