# UpdateMerchantMetadataRequest

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

Update the merchant token’s notification metadata.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object UpdateMerchantMetadataRequest
```

## Properties

- `merchantMetadata` (MerchantMetadata) *(required)*: The metadata of the merchant.
- `merchantTokenIdentifier` (string) *(required)*: The unique identifier of the merchant token.

  **Maximum Length**: `64`


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/updatemerchantmetadatarequest)*