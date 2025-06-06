# init(provisioningCredentialIdentifier:sharingInstanceIdentifier:cardConfigurationIdentifier:preview:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Initializes the user instance for provisioning.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
init(provisioningCredentialIdentifier credentialIdentifier: String, sharingInstanceIdentifier: String, cardConfigurationIdentifier templateIdentifier: String, preview: PKAddPassMetadataPreview)
```

## Parameters

- `credentialIdentifier`: An identifier for the user instance to provision.
- `sharingInstanceIdentifier`: A short-lived token to prevent replayability.
- `templateIdentifier`: An identifier for a legacy product on Apple Pay servers.
- `preview`: An object that contains information representing the provisioned pass in UI.

## See Also

- [init(provisioningCredentialIdentifier: String, sharingInstanceIdentifier: String, cardTemplateIdentifier: String, preview: PKAddPassMetadataPreview)](pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardtemplateidentifier:preview:).md)
  Initializes the product instance to provision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkjapanindividualnumbercardmetadata/init(provisioningcredentialidentifier:sharinginstanceidentifier:cardconfigurationidentifier:preview:))*