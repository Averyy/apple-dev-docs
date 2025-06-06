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

- [struct JPKIPassContents](jpkipasscontents.md)
  A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [class PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md)
  Configuration to define the identity document.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata defining the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassmetadatapreview)*