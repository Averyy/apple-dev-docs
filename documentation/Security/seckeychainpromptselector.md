# SecKeychainPromptSelector

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

Bits that define when a keychain should require a passphrase.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainPromptSelector
```

```c
enum SecKeychainPromptSelector : uint16;
```

## Topics

### Constants
- [static var requirePassphase: SecKeychainPromptSelector](./seckeychainpromptselector/requirepassphase.md)
  Indicates that a passphrase should be required for every access.
- [static var unsigned: SecKeychainPromptSelector](./seckeychainpromptselector/unsigned.md)
  Indicates that a passphrase should be required when an unsigned application attempts to use the keychain, overriding the system default.
- [static var unsignedAct: SecKeychainPromptSelector](./seckeychainpromptselector/unsignedact.md)
  Indicates that a passphrase should be required when an unsigned application attempts to use the keychain.
- [static var invalid: SecKeychainPromptSelector](./seckeychainpromptselector/invalid.md)
  Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain, overriding the system default.
- [static var invalidAct: SecKeychainPromptSelector](./seckeychainpromptselector/invalidact.md)
  Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain.
### Initializers
- [init(rawValue: uint16)](./seckeychainpromptselector/init%28rawvalue%29.md)
  Initializes a keychain prompt selector.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainpromptselector)*