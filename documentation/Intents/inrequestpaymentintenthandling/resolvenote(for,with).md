# resolveNote(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the notes associated with the request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveNote(for intent: INRequestPaymentIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveNote(for intent: INRequestPaymentIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveNoteForRequestPayment:(INRequestPaymentIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve any problems with the notes for the request.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`NSString`](../../Foundation/nsstring.md) object with the note to send to the request recipient. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePayer(for: INRequestPaymentIntent, with: (INRequestPaymentPayerResolutionResult) -> Void)](./resolvepayer%28for,with%29-4xu87.md)
  Resolves the person to receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INRequestPaymentCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-1it85.md)
  Resolves the amount of money requested.
- [func resolvePayer(for: INRequestPaymentIntent, with: (INPersonResolutionResult) -> Void)](./resolvepayer%28for,with%29-qp42.md)
  Called when you need to resolve the person who will receive the payment request.
- [func resolveCurrencyAmount(for: INRequestPaymentIntent, with: (INCurrencyAmountResolutionResult) -> Void)](./resolvecurrencyamount%28for,with%29-78c2m.md)
  Called when you need to resolve the amount of money being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentintenthandling/resolvenote(for:with:))*