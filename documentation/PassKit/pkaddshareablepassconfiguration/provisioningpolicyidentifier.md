# provisioningPolicyIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 14.0+ - Deprecated in 16.0
- iPadOS 14.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0
- macOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: provisioningPolicyIdentifier has been deprecated. You can stop setting this property in the init with no repercussions.

## Declaration

```swift
var provisioningPolicyIdentifier: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * provisioningPolicyIdentifier;
```

## See Also

### Creating a pass configuration
- [class func forPassMetaData([PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction, completion: (PKAddShareablePassConfiguration?, (any Error)?) -> Void)](./forpassmetadata%28_,provisioningpolicyidentifier,action,completion%29.md)
  Creates and error checks a new shareable pass-configuration object.
- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](./primaryaction.md)
  The action that the system performs with the shareable pass.
- [var credentialsMetadata: [PKShareablePassMetadata]](./credentialsmetadata.md)
  Information for a shareable pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/provisioningpolicyidentifier)*