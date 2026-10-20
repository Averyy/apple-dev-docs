# threeDSecure

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

Support for the 3-D Secure protocol.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static var threeDSecure: PKMerchantCapability { get }
```

```c
PKMerchantCapability3DS
```

## See Also

### Constants
- [static var instantFundsOut: PKMerchantCapability](./instantfundsout.md)
  The value that indicates the merchant supports disbursing funds using Instant Funds Out.
- [static var emv: PKMerchantCapability](./emv.md)
  Support for the EMV protocol.
- [static var credit: PKMerchantCapability](./credit.md)
  Support for credit cards.
- [static var debit: PKMerchantCapability](./debit.md)
  Support for debit cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkmerchantcapability/threedsecure)*