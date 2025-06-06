# LAPolicy.deviceOwnerAuthenticationWithBiometricsOrWatch

**Framework**: Local Authentication  
**Kind**: case

User authentication with either biometry or Apple Watch.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case deviceOwnerAuthenticationWithBiometricsOrWatch
```

#### Discussion

You use the [`LAPolicy.deviceOwnerAuthenticationWithBiometricsOrWatch`](lapolicy/deviceownerauthenticationwithbiometricsorwatch.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method to authenticate the user with either Apple Watch or biometrics. The authentication mechanisms run in parallel until one or the other succeeds, or until the user cancels the operation.

If the evaluation method can’t find a nearby, paired Apple Watch running watchOS 6 or later, this policy reverts to the behavior of the [`LAPolicy.deviceOwnerAuthenticationWithBiometrics`](lapolicy/deviceownerauthenticationwithbiometrics.md) policy. If biometry is unavailable, the policy behaves like the [`LAPolicy.deviceOwnerAuthenticationWithWatch`](lapolicy/deviceownerauthenticationwithwatch.md) policy.

To allow the user to authenticate with either of these options or a password, use the [`LAPolicy.deviceOwnerAuthentication`](lapolicy/deviceownerauthentication.md) policy instead.

## See Also

- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](lapolicy/deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [LAPolicy.deviceOwnerAuthenticationWithWatch](lapolicy/deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](lapolicy/deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](lapolicy/deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometricsorwatch)*