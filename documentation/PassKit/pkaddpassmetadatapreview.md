# PKAddPassMetadataPreview

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A preview object that contains information representing the pass you add to Wallet.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
class PKAddPassMetadataPreview
```

#### Overview

Use this class to preview an object with all of the information you need to present a pass during provision.

## Topics

### Creating a preview of the pass
- [init(passThumbnail: CGImage, localizedDescription: String)](pkaddpassmetadatapreview/init(passthumbnail:localizeddescription:).md)
  Provides a preview of an image object that represents the pass you add to Wallet.
- [var localizedDescription: String?](pkaddpassmetadatapreview/localizeddescription.md)
  A localized description of the pass.
- [var passThumbnailImage: CGImage?](pkaddpassmetadatapreview/passthumbnailimage.md)
  A CGImage object representing the card artwork of the pass you use during provisioning.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.class.md)
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
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview)*