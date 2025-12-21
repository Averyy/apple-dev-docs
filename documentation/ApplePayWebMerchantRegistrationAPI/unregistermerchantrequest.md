# UnregisterMerchantRequest

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: dictionary

The request body you use to unregister one or more merchant domains.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Declaration

```swift
object UnregisterMerchantRequest
```

#### Overview

The following example shows the format of an `UnregisterMerchant` request.

```json
{
    "domainNames" : ["subdomain-1.example.com"],
    "partnerInternalMerchantIdentifier": "ABC-123456",
    "reason": "merchant has closed their account"
}
```

## See Also

- [Unregister Merchant](unregister-merchant.md)
  Unregister one or more domains associated with a previously registered merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregistermerchantrequest)*