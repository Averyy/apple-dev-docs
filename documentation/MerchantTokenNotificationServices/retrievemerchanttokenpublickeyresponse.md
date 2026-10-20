# RetrieveMerchantTokenPublicKeyResponse

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

Get the merchant token public key response.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object RetrieveMerchantTokenPublicKeyResponse
```

## Properties

- `merchantTokenPublicKey` (string) *(required)*: The X9.63-encoded public key, Base64-encoded.

  **Maximum Length**: `256`
- `statusCode` (integer) *(required)*: The HTTP status code.
- `supportedCiphersuite` (string) *(required)*: The Apple-supported ciphersuite for HPKE in authorization mode. Supported: HPKE_AUTH_P384_SHA384_AES_GCM_256.

  **Maximum Length**: `64`


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/retrievemerchanttokenpublickeyresponse)*