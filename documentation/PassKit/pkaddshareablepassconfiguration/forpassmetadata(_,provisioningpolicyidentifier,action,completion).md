# forPassMetaData(_:provisioningPolicyIdentifier:action:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Creates and error checks a new shareable pass-configuration object.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use configurationForPassMetadata:primaryAction:completion:

## Declaration

```swift
class func forPassMetaData(_ passMetadata: [PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction, completion: @escaping @Sendable (PKAddShareablePassConfiguration?, (any Error)?) -> Void)
```

```swift
class func forPassMetaData(_ passMetadata: [PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction) async throws -> PKAddShareablePassConfiguration
```

```objc
+ (void) configurationForPassMetadata:(NSArray<PKShareablePassMetadata *> *) passMetadata provisioningPolicyIdentifier:(NSString *) provisioningPolicyIdentifier primaryAction:(PKAddShareablePassConfigurationPrimaryAction) action completion:(void (^)(PKAddShareablePassConfiguration *shareableCredentialConfiguration, NSError *error)) completion;
```

## Parameters

- `passMetadata`: 
- `provisioningPolicyIdentifier`: 
- `action`: The action that the system performs with the shareable pass.
- `completion`: A completion handler that returns the shareable pass configuration or an error. This handler takes the following parameters:

  - **`shareableCredentialConfiguration`**: A [`PKAddShareablePassConfiguration`](../pkaddshareablepassconfiguration.md) that contains the shareable pass configuration, or `nil` if an error occurred.
  - **`error`**: An [`NSError`](../../Foundation/nserror.md) that contains the error, or `nil` if no error occurred.

## See Also

### Creating a pass configuration
- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](./primaryaction.md)
  The action that the system performs with the shareable pass.
- [var credentialsMetadata: [PKShareablePassMetadata]](./credentialsmetadata.md)
  Information for a shareable pass.
- [var provisioningPolicyIdentifier: String](./provisioningpolicyidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/forpassmetadata(_:provisioningpolicyidentifier:action:completion:))*