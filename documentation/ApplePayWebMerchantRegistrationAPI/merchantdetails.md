# MerchantDetails

**Framework**: Apple Pay Web Merchant Registration API  
**Kind**: dictionary

Detailed information for a single registered merchant.

**Availability**:
- Apple Pay Web Merchant Registration API 1.0+

## Declaration

```swift
object MerchantDetails
```

#### Discussion

The following example shows the structure of a JSON object that contains the merchant details response.

```json
{
    "domainNames": [
        "subdomain-1.example.com", 
        "subdomain-2.example.com"
    ],
    "partnerMerchantName": "Example Merchant",
    "partnerInternalMerchantIdentifier": "ABC-123456",
    "partnerMerchantValidationURI": "/.well-known/apple-developer-merchantid-domain-association",
    "encryptTo": "DE1EB292B6781EFF977E45ECB42B047BE83DA586C537B4841E29A59065BC122B"
}
```

To compare a payment platform integrator ID or merchant ID with the value that this request returns in the `encryptTo` string, create a SHA-256 hash of the payment platform integrator ID or merchant ID first. In the Terminal app, enter the following command, replacing `com.your.id` with the payment platform integrator ID or merchant ID:

```zsh
echo -n com.your.id | openssl dgst -sha256
```

The result is a hexadecimal value that you can compare with the value that this request returns in the `encryptTo` string.

## Properties

- `domainNames` ([string]): A list of fully qualified domain names for which Apple Pay processes payments for this merchant.
- `encryptTo` (string): A SHA-256 hash of the payment platform integrator ID or merchant ID that you provided for the `encryptTo` value when calling [`Register Merchant`](register-merchant.md).
- `partnerMerchantName` (string): A human-readable name for the merchant.
- `partnerMerchantValidationURI` (string): The URI used by Apple to locate the domain verification file during merchant registration. It is used for tracking and debugging.
- `partnerInternalMerchantIdentifier` (string): The identifier that uniquely identifies the merchant.

## See Also

- [Get Merchant Details](get-merchant.md)
  Retrieve information about a registered merchant’s current state by using the merchant’s internal merchant identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/merchantdetails)*