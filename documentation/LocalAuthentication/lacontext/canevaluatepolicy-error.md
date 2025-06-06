# canEvaluatePolicy(_:error:)

**Framework**: Local Authentication  
**Kind**: method

Assesses whether authentication can proceed for a given policy.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func canEvaluatePolicy(_ policy: LAPolicy, error: NSErrorPointer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the policy can be evaluated, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Some policies impose requirements that must be met before authentication can proceed. For example, a policy that requires biometrics can’t authenticate if Touch ID or Face ID is disabled. This method tests all the prerequisites for a given policy.

Don’t store the return value from this method because it might change as a result of changes in the system. For example, a user might disable Touch ID after you call this method.

> ❗ **Important**:  Don’t call this method in the reply block of the [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method because that might lead to deadlock.

 Don’t call this method in the reply block of the [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method because that might lead to deadlock.

## Parameters

- `policy`: The policy to evaluate. For possible values, see  .
- `error`: Specify   for this parameter to ignore any errors.

## See Also

- [enum LAPolicy](lapolicy.md)
  The set of available local authentication policies.
- [var biometryType: LABiometryType](lacontext/biometrytype.md)
  The type of biometric authentication supported by the device.
- [enum LABiometryType](labiometrytype.md)
  The set of available biometric authentication types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lacontext/canevaluatepolicy(_:error:))*