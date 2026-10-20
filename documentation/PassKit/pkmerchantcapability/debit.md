# debit

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

Support for debit cards.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var debit: PKMerchantCapability { get }
```

```c
PKMerchantCapabilityDebit
```

## See Also

### Constants
- [static var instantFundsOut: PKMerchantCapability](./instantfundsout.md)
  The value that indicates the merchant supports disbursing funds using Instant Funds Out.
- [static var threeDSecure: PKMerchantCapability](./threedsecure.md)
  Support for the 3-D Secure protocol.
- [static var emv: PKMerchantCapability](./emv.md)
  Support for the EMV protocol.
- [static var credit: PKMerchantCapability](./credit.md)
  Support for credit cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkmerchantcapability/debit)*