# PKAddShareablePassConfiguration

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that represents the data and action for a shared copy of pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
class PKAddShareablePassConfiguration
```

```objc
@interface PKAddShareablePassConfiguration : PKAddSecureElementPassConfiguration
```

## Topics

### Creating a pass configuration
- [class func forPassMetaData([PKShareablePassMetadata], provisioningPolicyIdentifier: String, action: PKAddShareablePassConfigurationPrimaryAction, completion: (PKAddShareablePassConfiguration?, (any Error)?) -> Void)](./pkaddshareablepassconfiguration/forpassmetadata%28_,provisioningpolicyidentifier,action,completion%29.md)
  Creates and error checks a new shareable pass-configuration object.
- [var primaryAction: PKAddShareablePassConfigurationPrimaryAction](./pkaddshareablepassconfiguration/primaryaction.md)
  The action that the system performs with the shareable pass.
- [var credentialsMetadata: [PKShareablePassMetadata]](./pkaddshareablepassconfiguration/credentialsmetadata.md)
  Information for a shareable pass.
- [var provisioningPolicyIdentifier: String](./pkaddshareablepassconfiguration/provisioningpolicyidentifier.md)
### Type Methods
- [class func forPassMetadata([PKShareablePassMetadata], action: PKAddShareablePassConfigurationPrimaryAction, completion: (PKAddShareablePassConfiguration?, (any Error)?) -> Void)](./pkaddshareablepassconfiguration/forpassmetadata%28_,action,completion%29.md)

## Relationships

### Inherits From
- [PKAddSecureElementPassConfiguration](./pkaddsecureelementpassconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shareable passes
- [class PKShareablePassMetadata](./pkshareablepassmetadata.md)
  Information that you use to configure the sharing sheet for a pass.
- [enum PKAddShareablePassConfigurationPrimaryAction](./pkaddshareablepassconfigurationprimaryaction.md)
  The kind of add action that the system performs with a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfiguration)*