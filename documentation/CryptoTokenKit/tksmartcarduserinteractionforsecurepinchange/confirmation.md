# TKSmartCardUserInteractionForSecurePINChange.Confirmation

**Framework**: CryptoTokenKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct Confirmation
```

```c
enum TKSmartCardPINConfirmation : NSUInteger;
```

## Topics

### Type Properties
- [static var current: TKSmartCardUserInteractionForSecurePINChange.Confirmation](./confirmation/current.md)
- [static var new: TKSmartCardUserInteractionForSecurePINChange.Confirmation](./confirmation/new.md)
- [TKSmartCardPINConfirmationNone](../tksmartcardpinconfirmation/tksmartcardpinconfirmationnone.md)
### Initializers
- [init(rawValue: UInt)](./confirmation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring User Interaction
- [var pinConfirmation: TKSmartCardUserInteractionForSecurePINChange.Confirmation](./pinconfirmation.md)
  The way PIN confirmation is requested. `TKSmartCardPINConfirmationNone` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation)*