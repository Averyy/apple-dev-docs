# SecAccessControlCreateFlags

**Framework**: Security  
**Kind**: struct

Access control constants that dictate how a keychain item may be used.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct SecAccessControlCreateFlags
```

## Mentions

- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)
- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md)

#### Overview

Use these flags with the [`SecAccessControlCreateWithFlags(_:_:_:_:)`](secaccesscontrolcreatewithflags(_:_:_:_:).md) function, or as the value associated with the [`kSecAttrAccessControl`](ksecattraccesscontrol.md) key in a keychain item’s attribute dictionary, to control keychain item accessibility.

## Topics

### Constraints
- [static var devicePasscode: SecAccessControlCreateFlags](secaccesscontrolcreateflags/devicepasscode.md)
  Constraint to access an item with a passcode.
- [static var biometryAny: SecAccessControlCreateFlags](secaccesscontrolcreateflags/biometryany.md)
  Constraint to access an item with Touch ID for any enrolled fingers, or Face ID.
- [static var biometryCurrentSet: SecAccessControlCreateFlags](secaccesscontrolcreateflags/biometrycurrentset.md)
  Constraint to access an item with Touch ID for currently enrolled fingers, or from Face ID with the currently enrolled user.
- [static var userPresence: SecAccessControlCreateFlags](secaccesscontrolcreateflags/userpresence.md)
  Constraint to access an item with either biometry or passcode.
- [static var watch: SecAccessControlCreateFlags](secaccesscontrolcreateflags/watch.md)
  Constraint to access an item with a watch.
### Conjunctions
- [static var and: SecAccessControlCreateFlags](secaccesscontrolcreateflags/and.md)
  Indicates that all constraints must be satisfied.
- [static var or: SecAccessControlCreateFlags](secaccesscontrolcreateflags/or.md)
  Indicates that at least one constraint must be satisfied.
### Additional Options
- [static var applicationPassword: SecAccessControlCreateFlags](secaccesscontrolcreateflags/applicationpassword.md)
  Option to use an application-provided password for data encryption key generation.
- [static var privateKeyUsage: SecAccessControlCreateFlags](secaccesscontrolcreateflags/privatekeyusage.md)
  Enable a private key to be used in signing a block of data or verifying a signed block.
### Initializers
- [init(rawValue: CFOptionFlags)](secaccesscontrolcreateflags/init(rawvalue:).md)
  Initialize an access control creation flags object.
### Legacy Constraints
- [static var touchIDAny: SecAccessControlCreateFlags](secaccesscontrolcreateflags/touchidany.md)
  Constraint to access an item with Touch ID for any enrolled fingers.
- [static var touchIDCurrentSet: SecAccessControlCreateFlags](secaccesscontrolcreateflags/touchidcurrentset.md)
  Constraint to access an item with Touch ID for currently enrolled fingers.
### Type Properties
- [static var companion: SecAccessControlCreateFlags](secaccesscontrolcreateflags/companion.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags)*