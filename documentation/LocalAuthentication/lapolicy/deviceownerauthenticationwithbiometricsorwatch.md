# deviceOwnerAuthenticationWithBiometricsOrWatch

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

User authentication with either biometry or Apple Watch.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0 (renamed: LAPolicy.deviceOwnerAuthenticationWithBiometricsOrCompanion)

## Declaration

```swift
static var deviceOwnerAuthenticationWithBiometricsOrWatch: LAPolicy { get }
```

```c
LAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch
```

## Discussion

You use the [`deviceOwnerAuthenticationWithBiometricsOrWatch`](./deviceownerauthenticationwithbiometricsorwatch.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](../lacontext/evaluatepolicy%28_,localizedreason,reply%29.md) method to authenticate the user with either Apple Watch or biometrics. The authentication mechanisms run in parallel until one or the other succeeds, or until the user cancels the operation.

If the evaluation method can’t find a nearby, paired Apple Watch running watchOS 6 or later, this policy reverts to the behavior of the [`LAPolicy.deviceOwnerAuthenticationWithBiometrics`](./deviceownerauthenticationwithbiometrics.md) policy. If biometry is unavailable, the policy behaves like the [`deviceOwnerAuthenticationWithWatch`](./deviceownerauthenticationwithwatch.md) policy.

To allow the user to authenticate with either of these options or a password, use the [`LAPolicy.deviceOwnerAuthentication`](./deviceownerauthentication.md) policy instead.

## See Also

### Policies
- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](./deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [static var deviceOwnerAuthenticationWithWatch: LAPolicy](./deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](./deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](./deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometricsorwatch)*