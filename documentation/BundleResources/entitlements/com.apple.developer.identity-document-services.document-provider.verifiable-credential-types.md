# Digital Credentials API - Verifiable Credential Provider

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that represent the types of verifiable credentials that an identity document provider app can provide during an online web presentment.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)

## Details

- **Name**: `com.apple.developer.identity-document-services.document-provider.verifiable-credential-types`
- **Type**: array of string 

## Possible Values

- `urn:eudi:pid:1`

## Discussion

`urn:eudi:pid:1` is the category for a personal ID card for EU countries. Use this entitlement to enable your app to provide verifiable credentials during an identity document presentment to the web.

## See Also

### IdentityDocumentServices
- [Digital Credentials API - Mobile Document Provider](./com.apple.developer.identity-document-services.document-provider.mobile-document-types.md)
  An array of strings that represent the types of mobile documents (mdoc) that an identity document provider app can provide during an online web presentment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.identity-document-services.document-provider.verifiable-credential-types)*