# state

**Framework**: SecureElementCredential  
**Kind**: property  
**Role**: Instance Property

The state of a presentment intent assertion, indicating whether it’s currently valid.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
final var state: CredentialSession.PresentmentIntentAssertion.State { get async }
```

#### Discussion

Be sure to check if the state of the acquired intent assertion is stale before attempting to present over the contactess interface.

## See Also

### Inspecting assertion state
- [CredentialSession.PresentmentIntentAssertion.State](./state-swift.enum.md)
  An enumeration of possible states of a presentment intent assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion/state-swift.property)*