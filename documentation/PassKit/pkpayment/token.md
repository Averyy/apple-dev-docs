# token

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The encrypted payment information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var token: PKPaymentToken { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) PKPaymentToken * token;
```

#### Discussion

For more information about the payment data structure, see [Payment token format reference](../payment-token-format-reference.md).

## See Also

### Working with the payment token
- [class PKPaymentToken](../pkpaymenttoken.md)
  Contains the user’s payment credentials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment/token)*