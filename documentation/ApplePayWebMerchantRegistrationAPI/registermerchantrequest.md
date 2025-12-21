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
    "domainNames" : ["subdomain-1.example.com", "subdomain-2.example.com"],
    "partnerMerchantName" : "Example Merchant",
    "partnerInternalMerchantIdentifier": "ABC-123456",
    "encryptTo" : "platformintegrator.com.example",
    "merchantUrl": "https://example.com"
}
```

## See Also

- [Preparing merchant domains for verification](preparing-merchant-domains-for-verification.md)
  Host a domain verification file on each domain before requesting registration.
- [Register Merchant](register-merchant.md)
  Register a merchant and its corresponding set of fully qualified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registermerchantrequest)*