# init(provisioningCredentialIdentifier:cardConfigurationIdentifier:sharingInstanceIdentifier:passThumbnailImage:ownerDisplayName:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a shareable pass metadata object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
init?(provisioningCredentialIdentifier credentialIdentifier: String, cardConfigurationIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String)
```

## Parameters

- `credentialIdentifier`: A value that represents the user credentials for the pass.
- `cardConfigurationIdentifier`: A value that represents the configuration of the pass.
- `sharingInstanceIdentifier`: A unique value that you use to validate the shared pass.
- `passThumbnailImage`: A thumbnail image for the pass.
- `ownerDisplayName`: The name of the person that receives the shared pass.
- `localizedDescription`: A longer form of the pass description.

## See Also

- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, passThumbnailImage: CGImage, ownerDisplayName: String, localizedDescription: String, accountHash: String, templateIdentifier: String, relyingPartyIdentifier: String, requiresUnifiedAccessCapableDevice: Bool)](pkshareablepassmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:accounthash:templateidentifier:relyingpartyidentifier:requiresunifiedaccesscapabledevice:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata/init(provisioningcredentialidentifier:cardconfigurationidentifier:sharinginstanceidentifier:passthumbnailimage:ownerdisplayname:localizeddescription:))*