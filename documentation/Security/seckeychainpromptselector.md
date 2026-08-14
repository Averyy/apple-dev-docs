# SecKeychainPromptSelector

**Framework**: Security  
**Kind**: struct

Bits that define when a keychain should require a passphrase.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeychainPromptSelector
```

## Topics

### Constants
- [static var requirePassphase: SecKeychainPromptSelector](seckeychainpromptselector/requirepassphase.md)
  Indicates that a passphrase should be required for every access.
- [static var unsigned: SecKeychainPromptSelector](seckeychainpromptselector/unsigned.md)
  Indicates that a passphrase should be required when an unsigned application attempts to use the keychain, overriding the system default.
- [static var unsignedAct: SecKeychainPromptSelector](seckeychainpromptselector/unsignedact.md)
  Indicates that a passphrase should be required when an unsigned application attempts to use the keychain.
- [static var invalid: SecKeychainPromptSelector](seckeychainpromptselector/invalid.md)
  Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain, overriding the system default.
- [static var invalidAct: SecKeychainPromptSelector](seckeychainpromptselector/invalidact.md)
  Indicates that a passphrase should be required when an application with an invalid signature attempts to use the keychain.
### Initializers
- [init(rawValue: uint16)](seckeychainpromptselector/init(rawvalue:).md)
  Initializes a keychain prompt selector.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainpromptselector)*