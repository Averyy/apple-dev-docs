# init(provisioningCredentialIdentifier:sharingInstanceIdentifier:passThumbnailImage:ownerDisplayName:localizedDescription:accountHash:templateIdentifier:relyingPartyIdentifier:requiresUnifiedAccessCapableDevice:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use initWithProvisioningCredentialIdentifier:sharingInstanceIdentifier:cardTemplateIdentifier:passPreviewMetadata:

## Declaration

```swift
init(provisioningCredentialIdentifier credentialIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String, accountHash: String, templateIdentifier: String, relyingPartyIdentifier: String, requiresUnifiedAccessCapableDevice: Bool)
```

```objc
- (instancetype) initWithProvisioningCredentialIdentifier:(NSString *) credentialIdentifier sharingInstanceIdentifier:(NSString *) sharingInstanceIdentifier passThumbnailImage:(CGImageRef) passThumbnailImage ownerDisplayName:(NSString *) ownerDisplayName localizedDescription:(NSString *) localizedDescription accountHash:(NSString *) accountHash templateIdentifier:(NSString *) templateIdentifier relyingPartyIdentifier:(NSString *) relyingPartyIdentifier requiresUnifiedAccessCapableDevice:(BOOL) requiresUnifiedAccessCapableDevice;
```

## See Also

### Creating a shareable pass metadata object
- [init?(provisioningCredentialIdentifier: String, cardConfigurationIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String)](./init%28provisioningcredentialidentifier,cardconfigurationidentifier,sharinginstanceidentifier,passthumbnailimage,ownerdisplayname,localizeddescription%29.md)
  Creates a shareable pass metadata object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:accounthash:templateidentifier:relyingpartyidentifier:requiresunifiedaccesscapabledevice:))*