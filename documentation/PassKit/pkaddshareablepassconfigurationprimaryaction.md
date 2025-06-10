# PKAddShareablePassConfigurationPrimaryAction

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

The kind of add action that the system performs with a pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
enum PKAddShareablePassConfigurationPrimaryAction
```

## Topics

### Shareable pass configuration actions
- [PKAddShareablePassConfigurationPrimaryAction.add](pkaddshareablepassconfigurationprimaryaction/add.md)
  A constant that indicates the system adds a pass to a device.
- [PKAddShareablePassConfigurationPrimaryAction.share](pkaddshareablepassconfigurationprimaryaction/share.md)
  A constant that indicates the system shares the pass with another user.
### Initializers
- [init?(rawValue: UInt)](pkaddshareablepassconfigurationprimaryaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class PKAddShareablePassConfiguration](pkaddshareablepassconfiguration.md)
  An object that represents the data and action for a shared copy of pass.
- [class PKShareablePassMetadata](pkshareablepassmetadata.md)
  Information that you use to configure the sharing sheet for a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddshareablepassconfigurationprimaryaction)*