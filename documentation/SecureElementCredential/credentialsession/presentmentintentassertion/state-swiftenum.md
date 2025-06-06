# CredentialSession.PresentmentIntentAssertion.State

**Framework**: SecureElementCredential  
**Kind**: enum

An enumeration of possible states of a presentment intent assertion.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum State
```

## Topics

### Assertion states
- [CredentialSession.PresentmentIntentAssertion.State.active](credentialsession/presentmentintentassertion/state-swift.enum/active.md)
  The presentment intent assertion is active, offering exclusive use of the device’s contactless features.
- [CredentialSession.PresentmentIntentAssertion.State.invalid](credentialsession/presentmentintentassertion/state-swift.enum/invalid.md)
  The presentment intent assertion is invalid, and does not provide exclusive use of contactless features.
### Operators
- [static func == (CredentialSession.PresentmentIntentAssertion.State, CredentialSession.PresentmentIntentAssertion.State) -> Bool](credentialsession/presentmentintentassertion/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](credentialsession/presentmentintentassertion/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](credentialsession/presentmentintentassertion/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](credentialsession/presentmentintentassertion/state-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var state: CredentialSession.PresentmentIntentAssertion.State](credentialsession/presentmentintentassertion/state-swift.property.md)
  The state of a presentment intent assertion, indicating whether it’s currently valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion/state-swift.enum)*