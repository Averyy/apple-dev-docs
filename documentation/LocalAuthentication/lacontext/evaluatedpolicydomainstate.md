# evaluatedPolicyDomainState

**Framework**: Local Authentication  
**Kind**: property

The current state of the evaluated policy domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var evaluatedPolicyDomainState: Data? { get }
```

#### Discussion

The value of this property is non-`nil` when the [`canEvaluatePolicy(_:error:)`](lacontext/canevaluatepolicy(_:error:).md) method succeeds for a biometric policy or the person successfully authenticates using biometrics, following a call to [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md). Otherwise, its value is `nil`.

Compare the values you get from successive calls to this property to determine whether the authorized database changed. However, the value you get doesn’t describe the nature of a change; it only lets you detect if a change happens.

> **Note**:  The value of this property is different in different processes, so you can’t compare the value from one app to the value from another app.

 The value of this property is different in different processes, so you can’t compare the value from one app to the value from another app.

## See Also

- [func evaluatePolicy(LAPolicy, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](lacontext/evaluatepolicy(_:localizedreason:reply:).md)
  Evaluates the specified policy.
- [var maxBiometryFailures: NSNumber?](lacontext/maxbiometryfailures.md)
  The number of biometric authentication failures after which the context falls back to another mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/evaluatedpolicydomainstate)*