# PKShareablePassMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Information that you use to configure the sharing sheet for a pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKShareablePassMetadata
```

## Topics

### Creating a shareable pass metadata object
- [init?(provisioningCredentialIdentifier: String, cardConfigurationIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String)](pkshareablepassmetadata/init(provisioningcredentialidentifier:cardconfigurationidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:).md)
  Creates a shareable pass metadata object.
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String, accountHash: String, templateIdentifier: String, relyingPartyIdentifier: String, requiresUnifiedAccessCapableDevice: Bool)](pkshareablepassmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:accounthash:templateidentifier:relyingpartyidentifier:requiresunifiedaccesscapabledevice:).md)
### Displaying information on the share sheet
- [var ownerDisplayName: String](pkshareablepassmetadata/ownerdisplayname.md)
  The name of the person that receives a shared pass.
- [var passThumbnailImage: CGImage](pkshareablepassmetadata/passthumbnailimage.md)
  A thumbnail image of a pass that the system displays on the sharing sheet.
- [var localizedDescription: String](pkshareablepassmetadata/localizeddescription.md)
  A longer form of the pass description that the system displays on the sharing sheet.
### Reading notification properties
- [var accountHash: String](pkshareablepassmetadata/accounthash.md)
  An Apple Push Notification push token.
- [var relyingPartyIdentifier: String](pkshareablepassmetadata/relyingpartyidentifier.md)
  An identifier used in push notifications.
- [var templateIdentifier: String](pkshareablepassmetadata/templateidentifier.md)
  An identifier used in push notifications.
- [var cardTemplateIdentifier: String](pkshareablepassmetadata/cardtemplateidentifier.md)
### Requiring a unified access capable device
- [var requiresUnifiedAccessCapableDevice: Bool](pkshareablepassmetadata/requiresunifiedaccesscapabledevice.md)
### Initializers
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardConfigurationIdentifier: String, preview: PKShareablePassMetadata.Preview)](pkshareablepassmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardconfigurationidentifier:preview:).md)
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier: String, preview: PKShareablePassMetadata.Preview)](pkshareablepassmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardtemplateidentifier:preview:).md)
### Instance Properties
- [var cardConfigurationIdentifier: String](pkshareablepassmetadata/cardconfigurationidentifier.md)
  A developer-defined value that represents the configuration of a pass.
- [var credentialIdentifier: String](pkshareablepassmetadata/credentialidentifier.md)
  A developer-defined value that represents the user credentials of a pass.
- [var preview: PKShareablePassMetadata.Preview](pkshareablepassmetadata/preview-swift.property.md)
- [var serverEnvironmentIdentifier: String](pkshareablepassmetadata/serverenvironmentidentifier.md)
- [var sharingInstanceIdentifier: String](pkshareablepassmetadata/sharinginstanceidentifier.md)
  A developer-defined unique value that you use to validate a shared pass.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKAddShareablePassConfiguration](pkaddshareablepassconfiguration.md)
  An object that represents the data and action for a shared copy of pass.
- [enum PKAddShareablePassConfigurationPrimaryAction](pkaddshareablepassconfigurationprimaryaction.md)
  The kind of add action that the system performs with a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata)*