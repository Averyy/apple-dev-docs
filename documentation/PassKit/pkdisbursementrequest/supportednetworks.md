# supportedNetworks

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An array of payment networks the merchant supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var supportedNetworks: [PKPaymentNetwork] { get set }
```

#### Discussion

This property constrains the selectable payment passes to those the array includes — for example, [`visa`](pkpaymentnetwork/visa.md) or [`masterCard`](pkpaymentnetwork/mastercard.md).

## See Also

- [var merchantIdentifier: String](pkdisbursementrequest/merchantidentifier.md)
  A string that identifies the merchant.
- [var merchantCapabilities: PKMerchantCapability](pkdisbursementrequest/merchantcapabilities.md)
  A value that represents the payment-processing capabilities of the merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/supportednetworks)*