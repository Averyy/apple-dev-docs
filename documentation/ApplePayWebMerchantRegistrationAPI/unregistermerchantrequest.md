# UnregisterMerchantRequest

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: dictionary  
**Role**: Object

The request body you use to unregister one or more merchant domains.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Declaration

```
object UnregisterMerchantRequest
```

#### Overview

The following example shows the format of an `UnregisterMerchant` request.

```json
{
    "domainNames" : [
        "subdomain-1.example.com"
    ],
    "partnerInternalMerchantIdentifier": "ABC-123456",
    "reason": "merchant has closed their account"
}
```

## Properties

- `domainNames` ([string]) *(required)*: A list of fully qualified domain names to unregister. If a merchant has no remaining domain names after this request removes domains, Apple Pay server deletes the merchant’s registration.
- `partnerInternalMerchantIdentifier` (string) *(required)*: A merchant identifier that you create to uniquely identify the registered merchant, and which you use in Apple Pay transactions and in this API.

  **Maximum Length**: `1024`; **Allowed Values**: `/a-zA-Z0-9~-_+&@$!|,.;/`
- `reason` (string) *(required)*: A short, human-readable phrase that describes the cause of unregistration.

  **Maximum Length**: `1024`

## See Also

### Web Merchant Unregistration
- [Unregister Merchant](./unregister-merchant.md)
  Unregister one or more domains associated with a previously registered merchant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregistermerchantrequest)*