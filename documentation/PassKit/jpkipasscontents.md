# JPKIPassContents

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct JPKIPassContents
```

#### Overview

Supports access to installed digital identities associated with the pass. You can use these actions to perform all operations to view, modify, and act on the credientials the applet contains.

## Topics

### Initializing the digital identity
- [init(PKPass) async throws](jpkipasscontents/init(_:).md)
  Initializes with the digital identity state of the provided pass.
### Defining access to the identity passes
- [JPKIPassContents.UserIdentity](jpkipasscontents/useridentity-swift.struct.md)
  The functionality for the type of user identification.
- [JPKIPassContents.SigningIdentity](jpkipasscontents/signingidentity-swift.struct.md)
  The authentication for signing user identification.
- [JPKIPassContents.Signature](jpkipasscontents/signature.md)
  The resulting signed data and certificate you use to sign the pass.
- [JPKIPassContents.Certificate](jpkipasscontents/certificate.md)
  The certificate data associated with an identity document.
- [JPKIPassContents.AuthenticationRequest](jpkipasscontents/authenticationrequest.md)
  The user authentification request based on the generics type.
- [JPKIPassContents.Identity](jpkipasscontents/identity.md)
  Defines the common functionality that JPKI digital identities support.
### Error cases
- [JPKIPassContents.Error](jpkipasscontents/error.md)
  Defines a set of possible errors.
### Instance Properties
- [let signingIdentity: JPKIPassContents.SigningIdentity?](jpkipasscontents/signingidentity-swift.property.md)
  Allows access to the signing identity, if present in the JPKI applet.
- [let userIdentity: JPKIPassContents.UserIdentity?](jpkipasscontents/useridentity-swift.property.md)
  Allows for access to the user identity, if present in the JPKI applet.

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [class PKIdentityPhotoIDDescriptor](pkidentityphotoiddescriptor.md)
  An object you use to request information from a user’s photo ID or equivalent document.
- [class PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md)
  An object you use to request information from multiple identity documents.
- [class PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md)
  An object for requesting information from a user’s driver’s license or equivalent document.
- [class PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md)
  The object for specifying the metadata necessary to provision identity documents.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents)*