# init(merchantIdentifier:currency:region:supportedNetworks:merchantCapabilities:summaryItems:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a disbursement request with the parameters you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
convenience init(merchantIdentifier: String, currency: Locale.Currency, region: Locale.Region, supportedNetworks: [PKPaymentNetwork], merchantCapabilities: PKMerchantCapability, summaryItems: [PKPaymentSummaryItem])
```

## Parameters

- `merchantIdentifier`: A string that identifies the merchant.
- `currency`: The   that represents the  , which represents the value of this disbursement.
- `region`: The   that represents the merchant’s  .
- `supportedNetworks`: An array of   networks the merchant supports.
- `merchantCapabilities`: An array of   structures that describe the capabilities the merchant supports.
- `summaryItems`: An array of   objects that describe the disbursement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/init(merchantidentifier:currency:region:supportednetworks:merchantcapabilities:summaryitems:))*