# maxBiometryFailures

**Framework**: Local Authentication  
**Kind**: property

The number of biometric authentication failures after which the context falls back to another mechanism.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.10.3+
- visionOS 1.0+

## Declaration

```swift
var maxBiometryFailures: NSNumber? { get set }
```

#### Discussion

Biometry lockout happens after too many wrong attempts, regardless of how you set this property.

## See Also

- [func evaluatePolicy(LAPolicy, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](lacontext/evaluatepolicy(_:localizedreason:reply:).md)
  Evaluates the specified policy.
- [var evaluatedPolicyDomainState: Data?](lacontext/evaluatedpolicydomainstate.md)
  The current state of the evaluated policy domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/maxbiometryfailures)*