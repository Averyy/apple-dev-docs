# deviceOwnerAuthenticationWithBiometricsOrCompanion

**Framework**: Local Authentication  
**Kind**: property

Device owner will be authenticated by biometry or a companion device e.g. Watch, Mac, etc.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
static var deviceOwnerAuthenticationWithBiometricsOrCompanion: LAPolicy { get }
```

#### Discussion

Companion or biometric authentication is required. If no nearby paired companion device can be found, it behaves as LAPolicyDeviceOwnerAuthenticationWithBiometrics. Similarly, if biometry is unavailable it behaves as LAPolicyDeviceOwnerAuthenticationWithCompanion.

```None
        When both mechanisms are available, user is asked to use biometry and companion authentication
        will run in parallel. Users should follow instructions on the companion device to authenticate.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithbiometricsorcompanion)*