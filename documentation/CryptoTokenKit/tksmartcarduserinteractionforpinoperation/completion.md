# TKSmartCardUserInteractionForPINOperation.Completion

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
struct Completion
```

```c
enum TKSmartCardPINCompletion : NSUInteger;
```

## Topics

### Type Properties
- [static var key: TKSmartCardUserInteractionForPINOperation.Completion](./completion/key.md)
- [static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion](./completion/maxlength.md)
- [static var timeout: TKSmartCardUserInteractionForPINOperation.Completion](./completion/timeout.md)
### Initializers
- [init(rawValue: UInt)](./completion/init%28rawvalue%29.md)

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

### Managing Pin Completion
- [var pinCompletion: TKSmartCardUserInteractionForPINOperation.Completion](./pincompletion.md)
  The conditions under which PIN entry should be considered complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion)*