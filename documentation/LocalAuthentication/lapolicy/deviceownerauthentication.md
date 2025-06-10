# LAPolicy.deviceOwnerAuthentication

**Framework**: Local Authentication  
**Kind**: case

User authentication with biometry, Apple Watch, or the device passcode.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case deviceOwnerAuthentication
```

#### Discussion

You use the [`LAPolicy.deviceOwnerAuthentication`](lapolicy/deviceownerauthentication.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method to authenticate a user in iOS with either biometrics or a passcode, in watchOS with a passcode, or in macOS with Touch ID, Apple Watch, or the user’s password.

If biometry is available, enrolled, and not disabled, the system uses that first. In macOS, the system simultaneously looks for a nearby, paired Apple Watch running watchOS 6 or later, and tries to use that in parallel. When these options aren’t available, the system prompts the user for the device passcode or user’s password.

In iOS, policy evaluation fails with the error [`passcodeNotSet`](laerror-swift.struct/passcodenotset.md) if the device passcode isn’t enabled. The system disables passcode authentication after 6 unsuccessful attempts, with progressively increasing delays between attempts.

The authentication dialog contains a cancel button with a default title that you can customize using the [`localizedCancelTitle`](lacontext/localizedcanceltitle.md) property, as well as a fallback button that you can customize using [`localizedFallbackTitle`](lacontext/localizedfallbacktitle.md) property. When the user taps the fallback button, the system reverts to asking for the device passcode or user’s password. When the user taps the cancel button, the evaluation fails with the [`userCancel`](laerror-swift.struct/usercancel.md) error.

## See Also

- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](lapolicy/deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [static var deviceOwnerAuthenticationWithWatch: LAPolicy](lapolicy/deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [static var deviceOwnerAuthenticationWithBiometricsOrWatch: LAPolicy](lapolicy/deviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](lapolicy/deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthentication)*