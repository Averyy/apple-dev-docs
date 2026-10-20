# Digital Credentials API - Mobile Document Provider

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that represent the types of mobile documents (mdoc) that an identity document provider app can provide during an online web presentment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.developer.identity-document-services.document-provider.mobile-document-types`
- **Type**: array of string 

## Possible Values

- `eu.europa.ec.av.1`: The category for age verification for EU countries.
- `eu.europa.ec.eudi.pid.1`: The category for a personal ID card for EU countries.
- `org.iso.23220.photoid.1`: The category for a photo ID card.
- `org.iso.23220.1.jp.mnc`: The category for a Japan MyNumber card.
- `org.iso.18013.5.1.mDL`: The category for a mobile driver’s license.

#### Discussion

Use this entitlement to define the types of mobile documents that the app provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types)*