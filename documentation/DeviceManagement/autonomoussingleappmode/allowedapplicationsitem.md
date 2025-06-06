# AutonomousSingleAppMode.AllowedApplicationsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that specifies an app that can be granted access to the Accessibilty APIs.

**Availability**:
- macOS 10.13.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AutonomousSingleAppMode.AllowedApplicationsItem
```

#### Discussion

> ❗ **Important**:  If two dictionaries contain the same `BundleIdentifier` value but a different `TeamIdentifier` value, an error occurs and the system doesn’t install the profile.

 If two dictionaries contain the same `BundleIdentifier` value but a different `TeamIdentifier` value, an error occurs and the system doesn’t install the profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/autonomoussingleappmode/allowedapplicationsitem)*