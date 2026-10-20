# init(provisioningCredentialIdentifier:cardConfigurationIdentifier:sharingInstanceIdentifier:passThumbnailImage:ownerDisplayName:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates a shareable pass metadata object.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use initWithProvisioningCredentialIdentifier:sharingInstanceIdentifier:cardConfigurationIdentifier:passPreviewMetadata:

## Declaration

```swift
init?(provisioningCredentialIdentifier credentialIdentifier: String, cardConfigurationIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String)
```

```objc
- (instancetype) initWithProvisioningCredentialIdentifier:(NSString *) credentialIdentifier cardConfigurationIdentifier:(NSString *) cardConfigurationIdentifier sharingInstanceIdentifier:(NSString *) sharingInstanceIdentifier passThumbnailImage:(CGImageRef) passThumbnailImage ownerDisplayName:(NSString *) ownerDisplayName localizedDescription:(NSString *) localizedDescription;
```

## Parameters

- `credentialIdentifier`: A value that represents the user credentials for the pass.
- `cardConfigurationIdentifier`: A value that represents the configuration of the pass.
- `sharingInstanceIdentifier`: A unique value that you use to validate the shared pass.
- `passThumbnailImage`: A thumbnail image for the pass.
- `ownerDisplayName`: The name of the person that receives the shared pass.
- `localizedDescription`: A longer form of the pass description.

## See Also

### Creating a shareable pass metadata object
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String, accountHash: String, templateIdentifier: String, relyingPartyIdentifier: String, requiresUnifiedAccessCapableDevice: Bool)](./init%28provisioningcredentialidentifier,sharinginstanceidentifier,passthumbnailimage,ownerdisplayname,localizeddescription,accounthash,templateidentifier,relyingpartyidentifier,requiresunifiedaccesscapabledevice%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata/init(provisioningcredentialidentifier:cardconfigurationidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:))*