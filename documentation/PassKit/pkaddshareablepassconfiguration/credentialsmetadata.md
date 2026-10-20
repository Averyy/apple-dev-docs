# credentialsMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

Information for a shareable pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var credentialsMetadata: [PKShareablePassMetadata] { get }
```

```objc
@property (nonatomic, strong, readonly) NSArray<PKShareablePassMetadata *> * credentialsMetadata;
```

## See Also

### Creating a pass configuration
- [class func forPassMetaData([PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction, completion: (PKAddShareablePassConfiguration?, (any Error)?) -> Void)](./forpassmetadata%28_,provisioningpolicyidentifier,action,completion%29.md)
  Creates and error checks a new shareable pass-configuration object.
- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](./primaryaction.md)
  The action that the system performs with the shareable pass.
- [var provisioningPolicyIdentifier: String](./provisioningpolicyidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/credentialsmetadata)*