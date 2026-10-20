# init(provisioningCredentialIdentifier:sharingInstanceIdentifier:cardTemplateIdentifier:preview:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init  
**Role**: Initializer

Creates the product instance to provision.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+

## Declaration

```swift
init(provisioningCredentialIdentifier credentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier templateIdentifier: String, preview: PKAddPassMetadataPreview)
```

```objc
- (instancetype) initWithProvisioningCredentialIdentifier:(NSString *) credentialIdentifier sharingInstanceIdentifier:(NSString *) sharingInstanceIdentifier cardTemplateIdentifier:(NSString *) templateIdentifier preview:(PKAddPassMetadataPreview *) preview;
```

## See Also

### Initializing the digital card metadata
- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardConfigurationIdentifier: String, preview: PKAddPassMetadataPreview)](./init%28provisioningcredentialidentifier,sharinginstanceidentifier,cardconfigurationidentifier,preview%29.md)
  Initializes the user instance for provisioning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardtemplateidentifier:preview:))*