# maxBiometryFailures

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

The number of biometric authentication failures after which the context falls back to another mechanism.

**Availability**:
- iOS 8.3+ - Deprecated in 9.0
- iPadOS 8.3+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10.3+ - Deprecated in 10.11
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This property is deprecated and setting it has no effect.

## Declaration

```swift
var maxBiometryFailures: NSNumber? { get set }
```

```objc
@property (nonatomic, nullable) NSNumber * maxBiometryFailures;
```

#### Discussion

Biometry lockout happens after too many wrong attempts, regardless of how you set this property.

## See Also

### Evaluating authentication policies
- [func evaluatePolicy(LAPolicy, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](./evaluatepolicy%28_,localizedreason,reply%29.md)
  Evaluates the specified policy.
- [var evaluatedPolicyDomainState: Data?](./evaluatedpolicydomainstate.md)
  The current state of the evaluated policy domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/maxbiometryfailures)*