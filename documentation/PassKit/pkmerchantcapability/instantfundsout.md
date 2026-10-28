# instantFundsOut

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The value that indicates the merchant supports disbursing funds using Instant Funds Out.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var instantFundsOut: PKMerchantCapability { get }
```

```c
PKMerchantCapabilityInstantFundsOut
```

## Discussion

This capability indicates the merchant supports disbursing funds using Instant Funds Out (IFO), which means the recipient receives funds in minutes rather than days. Passing `PKMerchantCapabilityInstantFundsOut` into the [`init(merchantIdentifier:currency:region:supportedNetworks:merchantCapabilities:summaryItems:)`](../pkdisbursementrequest/init%28merchantidentifier,currency,region,supportednetworks,merchantcapabilities,summaryitems%29.md) indicates that the merchant is going to use IFO to facilitate the disbursement once the individual authenticates it.

## See Also

### Constants
- [static var threeDSecure: PKMerchantCapability](./threedsecure.md)
  Support for the 3-D Secure protocol.
- [static var emv: PKMerchantCapability](./emv.md)
  Support for the EMV protocol.
- [static var credit: PKMerchantCapability](./credit.md)
  Support for credit cards.
- [static var debit: PKMerchantCapability](./debit.md)
  Support for debit cards.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkmerchantcapability/instantfundsout)*