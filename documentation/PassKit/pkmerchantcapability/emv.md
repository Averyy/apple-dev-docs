# emv

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Support for the EMV protocol.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var emv: PKMerchantCapability { get }
```

#### Discussion

Include this value only if you support China Union Pay transactions.

## See Also

- [static var instantFundsOut: PKMerchantCapability](pkmerchantcapability/instantfundsout.md)
  The value that indicates the merchant supports disbursing funds using Instant Funds Out.
- [static var threeDSecure: PKMerchantCapability](pkmerchantcapability/threedsecure.md)
  Support for the 3-D Secure protocol.
- [static var credit: PKMerchantCapability](pkmerchantcapability/credit.md)
  Support for credit cards.
- [static var debit: PKMerchantCapability](pkmerchantcapability/debit.md)
  Support for debit cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkmerchantcapability/emv)*