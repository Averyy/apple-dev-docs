# PKJapanIndividualNumberCardMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A class that contains metadata indicating the specific product instance to provision.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
class PKJapanIndividualNumberCardMetadata
```

#### Overview

This class is similar to [`PKShareablePassMetadata`](pkshareablepassmetadata.md).

## Topics

### Initializing the digital card metadata
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardConfigurationIdentifier: String, preview: PKAddPassMetadataPreview)](pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardconfigurationidentifier:preview:).md)
  Initializes the user instance for provisioning.
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier: String, preview: PKAddPassMetadataPreview)](pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardtemplateidentifier:preview:).md)
  Creates the product instance to provision.
### Defining configuration
- [var authenticationPassword: String?](pkjapanindividualnumbercardmetadata/authenticationpassword.md)
  A string that specifies the authentication password when provisioning the pass.
- [var preview: PKAddPassMetadataPreview](pkjapanindividualnumbercardmetadata/preview.md)
  An object that contains information representing the pass for provisioning.
- [var signingPassword: String?](pkjapanindividualnumbercardmetadata/signingpassword.md)
  A string that sets the signing password when you provision the pass.

## Relationships

### Inherits From
- [PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md)
  Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Configuring your environment for the Verify with Wallet API](configuring-your-environment-for-the-verify-with-wallet-api.md)
  Set up your environment to use Verify with Wallet.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md)
  Decrypt and verify an in-app presentment request on your server.
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
- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata)*