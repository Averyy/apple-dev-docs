# LAPolicy.deviceOwnerAuthenticationWithCompanion

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

Device owner will be authenticated by a companion device e.g. Watch, Mac, etc.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
case deviceOwnerAuthenticationWithCompanion
```

```c
LAPolicyDeviceOwnerAuthenticationWithCompanion
```

#### Discussion

Companion authentication is required. If no nearby paired companion device can be found, LAErrorCompanionNotAvailable is returned.

```
        Users should follow instructions on the companion device to authenticate.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/lapolicy/deviceownerauthenticationwithcompanion)*