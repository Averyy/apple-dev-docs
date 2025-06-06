# blockedApplications

**Framework**: ManagedSettings  
**Kind**: property

A set of applications for the system to block.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var blockedApplications: Set<Application>? { get set }
```

#### Discussion

The system hides blocked applications and prevents the user from launching them. The value is `nil` if your app doesn’t specify a set of apps to block. Your app can shield up to 50 applications at once.

## See Also

- [static let blockedApplications: SettingMetadata<Set<Application>>](applicationsettings/blockedapplications-swift.type.property.md)
  A description of the setting that controls which apps a user can launch on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationsettings/blockedapplications-swift.property)*