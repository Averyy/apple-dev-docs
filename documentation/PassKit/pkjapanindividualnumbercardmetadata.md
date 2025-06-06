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
  Initializes the product instance to provision.
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

- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata defining the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata)*