# blockedApplications

**Framework**: ManagedSettings  
**Kind**: property

A description of the setting that controls which apps a user can launch on their device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let blockedApplications: SettingMetadata<Set<Application>>
```

#### Discussion

Use `blockedApplications` to access the metadata for [`blockedApplications`](applicationsettings/blockedapplications-swift.property.md). The default value is an empty set.

## See Also

- [var blockedApplications: Set<Application>?](applicationsettings/blockedapplications-swift.property.md)
  A set of applications for the system to block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationsettings/blockedapplications-swift.type.property)*