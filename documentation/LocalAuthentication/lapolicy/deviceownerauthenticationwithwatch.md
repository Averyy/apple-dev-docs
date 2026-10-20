# deviceOwnerAuthenticationWithWatch

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Type Property

User authentication with Apple Watch.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0 (renamed: LAPolicy.deviceOwnerAuthenticationWithCompanion)

## Declaration

```swift
static var deviceOwnerAuthenticationWithWatch: LAPolicy { get }
```

```c
LAPolicyDeviceOwnerAuthenticationWithWatch
```

#### Discussion

You use the [`deviceOwnerAuthenticationWithWatch`](./deviceownerauthenticationwithwatch.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](../lacontext/evaluatepolicy%28_,localizedreason,reply%29.md) method to authenticate the user with Apple Watch. If the evaluation method can’t find a nearby, paired Apple Watch running watchOS 6 or later, it returns the [`watchNotAvailable`](../laerror-swift.struct/watchnotavailable.md) error.

During authentication, the system presents a dialog that resembles the dialog presented for biometric authentication. The user confirms authentication by double-clicking the watch’s side button.

To allow the user to authenticate either with an Apple Watch or with biometrics, use the [`deviceOwnerAuthenticationWithBiometricsOrWatch`](./deviceownerauthenticationwithbiometricsorwatch.md) policy instead. To allow the user to authenticate with either of these options or a password, use the [`LAPolicy.deviceOwnerAuthentication`](./deviceownerauthentication.md) policy.

## See Also

### Policies
- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](./deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [static var deviceOwnerAuthenticationWithBiometricsOrWatch: LAPolicy](./deviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](./deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](./deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithwatch)*