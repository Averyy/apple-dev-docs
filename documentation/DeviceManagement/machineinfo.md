# MachineInfo

**Framework**: Device Management  
**Kind**: dictionary

A device’s information in response to a MDM enrollment profile request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object MachineInfo
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)

#### Discussion

This dictionary is CMS-signed with the device identity certificate. The system includes the device’s certificate and all necessary intermediate certificates. The certificate chain should validate against the Apple Root CA.

## See Also

- [object Device](device.md)
  A device’s properties and their values.
- [object Profile](profile.md)
  A profile’s properties and their values.
- [object Limit](limit.md)
  A ranged limit.
- [object Url](url.md)
  A URL object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/machineinfo)*