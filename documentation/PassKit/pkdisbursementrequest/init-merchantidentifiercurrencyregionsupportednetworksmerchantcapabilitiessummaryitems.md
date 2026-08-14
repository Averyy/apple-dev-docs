# init(merchantIdentifier:currency:region:supportedNetworks:merchantCapabilities:summaryItems:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a disbursement request with the parameters you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS ?+

## Declaration

```swift
convenience init(merchantIdentifier: String, currency: Locale.Currency, region: Locale.Region, supportedNetworks: [PKPaymentNetwork], merchantCapabilities: PKMerchantCapability, summaryItems: [PKPaymentSummaryItem])
```

## Parameters

- `merchantIdentifier`: A string that identifies the merchant.
- `currency`: The [`Locale.Currency`](https://developer.apple.com/documentation/foundation/locale/currency-swift.struct) that represents the [`ISO 4127 currency code`](https://developer.apple.comhttps://www.iso.org/iso-4217-currency-codes.html), which represents the value of this disbursement.
- `region`: The [`Locale.Region`](https://developer.apple.com/documentation/foundation/locale/region-swift.struct) that represents the merchant’s [`ISO 3166 region code`](https://developer.apple.comhttps://www.iso.org/iso-3166-country-codes.html).
- `supportedNetworks`: An array of [`PKPaymentNetwork`](pkpaymentnetwork.md) networks the merchant supports.
- `merchantCapabilities`: An array of [`PKMerchantCapability`](pkmerchantcapability.md) structures that describe the capabilities the merchant supports.
- `summaryItems`: An array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that describe the disbursement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/init(merchantidentifier:currency:region:supportednetworks:merchantcapabilities:summaryitems:))*