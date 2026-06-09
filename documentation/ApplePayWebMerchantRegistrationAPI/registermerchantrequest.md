# RegisterMerchantRequest

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: dictionary

The request body you use to register merchants.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Declaration

```swift
object RegisterMerchantRequest
```

#### Discussion

The following example shows the structure of a JSON object with information on how to register merchant requests.

```json
{
    "domainNames" : [
        "subdomain-1.example.com",
        "subdomain-2.example.com"
    ],
    "partnerMerchantName" : "Example Merchant",
    "partnerInternalMerchantIdentifier": "ABC-123456",
    "encryptTo" : "platformintegrator.com.example",
    "merchantUrl": "https://example.com"
}
```

## Properties

- `domainNames` ([string]) *(required)*: A list of fully qualified domain names for which Apple Pay processes payments for this merchant. Items must be unique within the scope of each `partnerInternalMerchantIdentifier`. The API is limited to 99 domain names per `partnerInternalMerchantIdentifier`.
- `encryptTo` (string) *(required)*: The payment platform integrator ID or merchant ID associated with the payment processing certificate Apple Pay will use to encrypt payment data on behalf of the merchant you’re registering. Typically, use the payment platform integrator ID of the calling e-commerce platform. If a party other than the e-commerce platform decrypts the Apple Pay data, use their payment platform integrator ID or merchant ID.
- `merchantUrl` (string): An optional field in which you provide the merchant website’s top-level domain. Supply this value when registering merchants using a shared payment page hosted on the payment platform’s domain. This URL doesn’t have to be affiliated with the payment transaction nor is it verified.
- `partnerInternalMerchantIdentifier` (string) *(required)*: A unique identifier that you create for the merchant you’re registering. Each merchant your e-commerce platform serves must have a unique identifier. This is the same identifier that you pass as the `merchantIdentifier` field into [`canMakePaymentsWithActiveCard`](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePaySession/canMakePaymentsWithActiveCard) and when requesting and Apple Pay payment session. For more information, see [`Requesting an Apple Pay payment session`](https://developer.apple.com/documentation/ApplePayontheWeb/requesting-an-apple-pay-payment-session). The `partnerInternalMerchantIdentifier` value must use allowed characters only: `a-zA-Z0-9~-_+&@$!|,.;`
- `partnerMerchantName` (string) *(required)*: A human-readable name for the merchant; the API does not parse this name programmatically.

## See Also

- [Preparing merchant domains for verification](preparing-merchant-domains-for-verification.md)
  Host a domain verification file on each domain before requesting registration.
- [Register Merchant](register-merchant.md)
  Register a merchant and its corresponding set of fully qualified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registermerchantrequest)*