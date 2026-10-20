# CredentialSession.PresentmentIntentAssertion.State

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

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
- [CredentialSession.PresentmentIntentAssertion.State.active](./state-swift.enum/active.md)
  The presentment intent assertion is active, offering exclusive use of the device’s contactless features.
- [CredentialSession.PresentmentIntentAssertion.State.invalid](./state-swift.enum/invalid.md)
  The presentment intent assertion is invalid, and doesn’t provide exclusive use of contactless features.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Inspecting assertion state
- [var state: CredentialSession.PresentmentIntentAssertion.State](./state-swift.property.md)
  The state of a presentment intent assertion, indicating whether it’s currently valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion/state-swift.enum)*