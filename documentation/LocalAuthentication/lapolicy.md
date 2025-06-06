# LAPolicy

**Framework**: Local Authentication  
**Kind**: enum

The set of available local authentication policies.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum LAPolicy
```

## Topics

### Policies
- [LAPolicy.deviceOwnerAuthenticationWithBiometrics](lapolicy/deviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [LAPolicy.deviceOwnerAuthenticationWithWatch](lapolicy/deviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [LAPolicy.deviceOwnerAuthenticationWithBiometricsOrWatch](lapolicy/deviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [LAPolicy.deviceOwnerAuthentication](lapolicy/deviceownerauthentication.md)
  User authentication with biometry, Apple Watch, or the device passcode.
- [LAPolicy.deviceOwnerAuthenticationWithWristDetection](lapolicy/deviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.
### Policy Constants
- [var kLAPolicyDeviceOwnerAuthenticationWithBiometrics: Int32](klapolicydeviceownerauthenticationwithbiometrics.md)
  User authentication with biometry.
- [var kLAPolicyDeviceOwnerAuthenticationWithWatch: Int32](klapolicydeviceownerauthenticationwithwatch.md)
  User authentication with Apple Watch.
- [var kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch: Int32](klapolicydeviceownerauthenticationwithbiometricsorwatch.md)
  User authentication with either biometry or Apple Watch.
- [var kLAPolicyDeviceOwnerAuthentication: Int32](klapolicydeviceownerauthentication.md)
  User authentication with either biometry or the device passcode.
- [var kLAPolicyDeviceOwnerAuthenticationWithWristDetection: Int32](klapolicydeviceownerauthenticationwithwristdetection.md)
  User authentication with wrist detection on watchOS.
### Initializers
- [init?(rawValue: Int)](lapolicy/init(rawvalue:).md)
### Type Properties
- [static var deviceOwnerAuthenticationWithBiometricsOrCompanion: LAPolicy](lapolicy/deviceownerauthenticationwithbiometricsorcompanion.md)
  Device owner will be authenticated by biometry or a companion device e.g. Watch, Mac, etc.
- [static var deviceOwnerAuthenticationWithCompanion: LAPolicy](lapolicy/deviceownerauthenticationwithcompanion.md)
  Device owner will be authenticated by a companion device e.g. Watch, Mac, etc.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func canEvaluatePolicy(LAPolicy, error: NSErrorPointer) -> Bool](lacontext/canevaluatepolicy(_:error:).md)
  Assesses whether authentication can proceed for a given policy.
- [var biometryType: LABiometryType](lacontext/biometrytype.md)
  The type of biometric authentication supported by the device.
- [enum LABiometryType](labiometrytype.md)
  The set of available biometric authentication types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy)*