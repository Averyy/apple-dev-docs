# LAPolicy.deviceOwnerAuthenticationWithWristDetection

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

User authentication with wrist detection on watchOS.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
case deviceOwnerAuthenticationWithWristDetection
```

```c
LAPolicyDeviceOwnerAuthenticationWithWristDetection
```

## Discussion

You use the [`LAPolicy.deviceOwnerAuthenticationWithWristDetection`](./deviceownerauthenticationwithwristdetection.md) policy when calling the [`evaluatePolicy(_:localizedReason:reply:)`](../lacontext/evaluatepolicy%28_,localizedreason,reply%29.md) method to authenticate a user on watchOS.

Policy evaluation fails if the user hasn’t set or entered the passcode on their watch or if the watch previously detected its removal from the user’s wrist.

The following shows a policy evaluation that uses wrist detection on watchOS 9 and later:

```swift
var error: NSError?
let context = LAContext()
guard #available(watchOS 9.0, *), context.canEvaluatePolicy(.deviceOwnerWithWristDetection, error: &error) else {
    // Can't evaluate the policy, either it's unsupported or a passcode isn't set.
    // See `error` for details and fall back to legacy authentication.
}

do {
    try await context.evaluatePolicy(.deviceOwnerWithWristDetection, localizedReason: "Approve a sensitive operation")
    // The user's watch is on their wrist and they entered the correct passcode.
    
} catch {
    // Watch isn't on the wrist or the user hasn't entered the correct passcode.
    // See `error` for details and fall back to legacy authentication.
}
```

## See Also

### Policies
- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](./deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [static var deviceOwnerAuthenticationWithWatch: LAPolicy](./deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [static var deviceOwnerAuthenticationWithBiometricsOrWatch: LAPolicy](./deviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](./deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithwristdetection)*