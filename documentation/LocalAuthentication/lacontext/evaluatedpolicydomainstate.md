# evaluatedPolicyDomainState

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

The current state of the evaluated policy domain.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
var evaluatedPolicyDomainState: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * evaluatedPolicyDomainState;
```

## Discussion

The value of this property is non-`nil` when the [`canEvaluatePolicy(_:error:)`](./canevaluatepolicy%28_,error%29.md) method succeeds for a biometric policy or the person successfully authenticates using biometrics, following a call to [`evaluatePolicy(_:localizedReason:reply:)`](./evaluatepolicy%28_,localizedreason,reply%29.md). Otherwise, its value is `nil`.

Compare the values you get from successive calls to this property to determine whether the authorized database changed. However, the value you get doesn’t describe the nature of a change; it only lets you detect if a change happens.

> **Note**:  The value of this property is different in different processes, so you can’t compare the value from one app to the value from another app.

## See Also

### Evaluating authentication policies
- [func evaluatePolicy(LAPolicy, localizedReason: String, reply: (Bool, (any Error)?) -> Void)](./evaluatepolicy%28_,localizedreason,reply%29.md)
  Evaluates the specified policy.
- [var maxBiometryFailures: NSNumber?](./maxbiometryfailures.md)
  The number of biometric authentication failures after which the context falls back to another mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/evaluatedpolicydomainstate)*