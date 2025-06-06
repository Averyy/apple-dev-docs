# credentialsMetadata

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Information for a shareable pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var credentialsMetadata: [PKShareablePassMetadata] { get }
```

## See Also

- [class func forPassMetaData([PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction, completion: (PKAddShareablePassConfiguration?, (any Error)?) -> Void)](pkaddshareablepassconfiguration/forpassmetadata(_:provisioningpolicyidentifier:action:completion:).md)
  Creates and error checks a new shareable pass-configuration object.
- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](pkaddshareablepassconfiguration/primaryaction.md)
  The action that the system performs with the shareable pass.
- [var provisioningPolicyIdentifier: String](pkaddshareablepassconfiguration/provisioningpolicyidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration/credentialsmetadata)*