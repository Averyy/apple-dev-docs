# forPassMetaData(_:provisioningPolicyIdentifier:action:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Creates and error checks a new shareable pass-configuration object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class func forPassMetaData(_ passMetadata: [PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction) async throws -> PKAddShareablePassConfiguration
```

## Parameters

- `passMetadata`: 
- `provisioningPolicyIdentifier`: 
- `action`: The action that the system performs with the shareable pass.
- `completion`: A completion handler that returns the shareable pass configuration or an error. This handler takes the following parameters: - **`shareableCredentialConfiguration`**: A [`PKAddShareablePassConfiguration`](pkaddshareablepassconfiguration.md) that contains the shareable pass configuration, or `nil` if an error occurred.
- **`error`**: An [`NSError`](https://developer.apple.com/documentation/foundation/nserror) that contains the error, or `nil` if no error occurred.

## See Also

- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](pkaddshareablepassconfiguration/primaryaction.md)
  The action that the system performs with the shareable pass.
- [var credentialsMetadata: [PKShareablePassMetadata]](pkaddshareablepassconfiguration/credentialsmetadata.md)
  Information for a shareable pass.
- [var provisioningPolicyIdentifier: String](pkaddshareablepassconfiguration/provisioningpolicyidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/forpassmetadata(_:provisioningpolicyidentifier:action:completion:))*