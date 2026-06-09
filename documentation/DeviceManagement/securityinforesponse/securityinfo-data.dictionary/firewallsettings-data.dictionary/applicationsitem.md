# SecurityInfoResponse.SecurityInfo.FirewallSettings.ApplicationsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes the allowed apps.

**Availability**:
- macOS 10.12+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.FirewallSettings.ApplicationsItem
```

## Properties

- `Allowed` (boolean): If `true`, the app is an allowed app.
- `BundleID` (string): The app’s bundle identifier.
- `Name` (string): The app’s display name if it’s determinable from the `BundleID`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/firewallsettings-data.dictionary/applicationsitem)*