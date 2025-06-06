# PKIdentityDocumentMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A set of configured metadata defining the required information to add the corresponding pass to Wallet.

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

Contains the required and optional metadata you need to configure a pass. Similar to [`PKShareablePassMetadata`](pkshareablepassmetadata.md).

## Topics

### Instance Properties
- [var cardConfigurationIdentifier: String](pkidentitydocumentmetadata/cardconfigurationidentifier.md)
- [var cardTemplateIdentifier: String](pkidentitydocumentmetadata/cardtemplateidentifier.md)
- [var credentialIdentifier: String](pkidentitydocumentmetadata/credentialidentifier.md)
- [var serverEnvironmentIdentifier: String](pkidentitydocumentmetadata/serverenvironmentidentifier.md)
- [var sharingInstanceIdentifier: String](pkidentitydocumentmetadata/sharinginstanceidentifier.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
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
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentmetadata)*