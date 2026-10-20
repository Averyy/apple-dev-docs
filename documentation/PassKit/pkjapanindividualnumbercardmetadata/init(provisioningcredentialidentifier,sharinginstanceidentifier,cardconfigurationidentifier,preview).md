# init(provisioningCredentialIdentifier:sharingInstanceIdentifier:cardConfigurationIdentifier:preview:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Initializes the user instance for provisioning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
init(provisioningCredentialIdentifier credentialIdentifier: String, sharingInstanceIdentifier: String, cardConfigurationIdentifier: String, preview: PKAddPassMetadataPreview)
```

```objc
- (instancetype) initWithProvisioningCredentialIdentifier:(NSString *) credentialIdentifier sharingInstanceIdentifier:(NSString *) sharingInstanceIdentifier cardConfigurationIdentifier:(NSString *) cardConfigurationIdentifier preview:(PKAddPassMetadataPreview *) preview;
```

## Parameters

- `credentialIdentifier`: An identifier for the user instance to provision.
- `sharingInstanceIdentifier`: A short-lived token to prevent replayability.
- `preview`: An object that contains information representing the provisioned pass in UI.

## See Also

### Initializing the digital card metadata
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier: String, preview: PKAddPassMetadataPreview)](./init%28provisioningcredentialidentifier,sharinginstanceidentifier,cardtemplateidentifier,preview%29.md)
  Creates the product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardconfigurationidentifier:preview:))*