# MerchantTokenUsageMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

Metadata about where and how to retrieve the latest usage information.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object MerchantTokenUsageMetadata
```

#### Discussion

The `merchantPublicKey` includes encrypted metadata. When decrypted, you get a `data` JSON object that contains the `webServiceURL` of the merchant server, which hosts the usage information, and an opaque `authenticationToken`. The user’s devices present the `authenticationToken` when retrieving the latest usage information from the merchant server. This allows the merchant server to authenticate these requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagemetadata)*