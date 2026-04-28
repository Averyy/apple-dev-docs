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

## Properties

- `BundleIdentifier` (string) *(required)*: The unique bundle identifier. If two dictionaries contain the same `BundleIdentifier` value but a different `TeamIdentifier` value, an error occurs and the profile won’t be installed.
- `TeamIdentifier` (string) *(required)*: The developer’s team identifier that the system used when it signed the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/autonomoussingleappmode/allowedapplicationsitem)*