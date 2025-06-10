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
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainpromptselector)*