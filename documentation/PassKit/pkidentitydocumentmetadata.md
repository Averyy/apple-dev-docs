# PKIdentityDocumentMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A set of configured metadata that defines the required information to add the corresponding pass to Wallet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
class PKIdentityDocumentMetadata
```

#### Overview

This class contains the required and optional metadata you need to configure a pass. It’s similar to [`PKShareablePassMetadata`](PKShareablePassMetadata.md).

## Topics

### Instance Properties
- [var cardConfigurationIdentifier: String](PKIdentityDocumentMetadata/cardConfigurationIdentifier.md)
- [var cardTemplateIdentifier: String](PKIdentityDocumentMetadata/cardTemplateIdentifier.md)
- [var credentialIdentifier: String](PKIdentityDocumentMetadata/credentialIdentifier.md)
- [var serverEnvironmentIdentifier: String](PKIdentityDocumentMetadata/serverEnvironmentIdentifier.md)
  An identifier that references the target server environment Apple Pay servers need to connect with to provision the pass.
- [var sharingInstanceIdentifier: String](PKIdentityDocumentMetadata/sharingInstanceIdentifier.md)
  A unique identifier that refers to an instance of sharing credentials to a person’s device that another user, device, or the web initiates.
- [var documentType: PKAddIdentityDocumentType](PKIdentityDocumentMetadata/documentType.md)
  Identifies the type of the identity document.
- [var issuingCountryCode: String](PKIdentityDocumentMetadata/issuingCountryCode.md)
  Identifies the issuing country of the identity document.
- [var cardConfigurationIdentifier: String](pkidentitydocumentmetadata/cardconfigurationidentifier.md)
- [var cardTemplateIdentifier: String](pkidentitydocumentmetadata/cardtemplateidentifier.md)
- [var credentialIdentifier: String](pkidentitydocumentmetadata/credentialidentifier.md)
- [var documentType: PKAddIdentityDocumentType](pkidentitydocumentmetadata/documenttype.md)
  Identifies the type of the identity document.
- [var issuingCountryCode: String](pkidentitydocumentmetadata/issuingcountrycode.md)
  Identifies the issuing country of the identity document.
- [var serverEnvironmentIdentifier: String](pkidentitydocumentmetadata/serverenvironmentidentifier.md)
  An identifier that references the target server environment Apple Pay servers need to connect with to provision the pass.
- [var sharingInstanceIdentifier: String](pkidentitydocumentmetadata/sharinginstanceidentifier.md)
  A unique identifier that refers to an instance of sharing credentials to a person’s device that another user, device, or the web initiates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md)
- [PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
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
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentmetadata)*