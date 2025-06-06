# PKAddIdentityDocumentConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Configuration to define the identity document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
class PKAddIdentityDocumentConfiguration
```

#### Overview

Use this class for identity document passes. You provide the underlying metadata that defines the passes.

## Topics

### Setting the metadata
- [var metadata: PKIdentityDocumentMetadata](pkaddidentitydocumentconfiguration/metadata.md)
  A set of configurable metadata that defines the required information to add the corresponding pass to Wallet.
- [class func forMetadata(PKIdentityDocumentMetadata, completion: (PKAddIdentityDocumentConfiguration?, (any Error)?) -> Void)](pkaddidentitydocumentconfiguration/formetadata(_:completion:).md)
  Returns the identity document configuration.

## Relationships

### Inherits From
- [PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md)
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
- [class PKAddPassMetadataPreview](pkaddpassmetadatapreview.md)
  A preview object that contains information representing the pass you add to Wallet.
- [class PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md)
  A set of configured metadata defining the required information to add the corresponding pass to Wallet.
- [class PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md)
  An object for requesting information from a user’s national ID card.
- [class PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md)
  A class that contains metadata indicating the specific product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddidentitydocumentconfiguration)*