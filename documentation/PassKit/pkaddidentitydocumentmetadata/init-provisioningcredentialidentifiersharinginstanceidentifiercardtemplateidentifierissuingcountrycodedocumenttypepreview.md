# init(provisioningCredentialIdentifier:sharingInstanceIdentifier:cardTemplateIdentifier:issuingCountryCode:documentType:preview:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates the identity document metadata with parameters that the issuer’s server configures to indicate the specific product instance to provision.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS ?+
- visionOS 26.0+

## Declaration

```swift
init(provisioningCredentialIdentifier credentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier templateIdentifier: String, issuingCountryCode: String, documentType: PKAddIdentityDocumentType, preview: PKAddPassMetadataPreview)
```

## Parameters

- `credentialIdentifier`: Identifies the user’s instance for provisioning.
- `sharingInstanceIdentifier`: A short-lived token to prevent replay ability.
- `templateIdentifier`: A legacy identifier for Apple Pay servers.
- `issuingCountryCode`: Identifies the issuing country of the identity document.
- `documentType`: Identifies the type of the identity document.
- `preview`: An object containing information that represents the pass to provision in Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddidentitydocumentmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardtemplateidentifier:issuingcountrycode:documenttype:preview:))*