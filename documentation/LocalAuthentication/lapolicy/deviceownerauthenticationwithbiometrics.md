# LAPolicy.deviceOwnerAuthenticationWithBiometrics

**Framework**: Local Authentication  
**Kind**: case

User authentication with biometry.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- visionOS 1.0+

## Declaration

```swift
case deviceOwnerAuthenticationWithBiometrics
```

#### Discussion

You use the [`LAPolicy.deviceOwnerAuthenticationWithBiometrics`](lapolicy/deviceownerauthenticationwithbiometrics.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method to authenticate the user with biometrics.

Policy evaluation fails if Touch ID or Face ID is unavailable or not enrolled. Evaluation also fails after three failed Touch ID attempts. After two failed Face ID attempts, the system offers a fallback option, but stops trying to authenticate with Face ID. Both Touch ID and Face ID authentication are disabled system-wide after five consecutive unsuccessful attempts, even when the attempts span multiple evaluation calls. When this happens, the system requires the user to enter the device passcode to reenable biometry.

During authentication, the system presents the user with an authentication dialog for every attempt to authenticate with Touch ID, or after any failed Face ID attempt. The dialog contains a cancel button with a title that you can customize by setting the [`localizedCancelTitle`](lacontext/localizedcanceltitle.md) property. If the user taps the cancel button, the policy evaluation fails with the [`userCancel`](laerror-swift.struct/usercancel.md) error.

The authentication dialog also displays a fallback button after the first unsuccessful Touch ID attempt, or after the second unsuccessful Face ID attempt. You can customize the fallback button’s title by setting the [`localizedFallbackTitle`](lacontext/localizedfallbacktitle.md) property. If the user taps the fallback button, the policy evaluation fails with the [`userFallback`](laerror-swift.struct/userfallback.md) error. In this case, your app should provide an alternate mechanism for authenticating the user, like asking for a PIN or a password.

To let the system handle the fallback option by asking for the device passcode (in iOS or watchOS) or the user’s password (in macOS), use the [`LAPolicy.deviceOwnerAuthentication`](lapolicy/deviceownerauthentication.md) policy instead.

## See Also

- [static var deviceOwnerAuthenticationWithWatch: LAPolicy](lapolicy/deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [static var deviceOwnerAuthenticationWithBiometricsOrWatch: LAPolicy](lapolicy/deviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](lapolicy/deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](lapolicy/deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometrics)*