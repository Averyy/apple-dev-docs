# DeviceActivityData.User

**Framework**: Device Activity  
**Kind**: struct

Information about a person associated with an activity report.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct User
```

## Topics

### Identifying the person
- [var appleID: String?](deviceactivitydata/user-swift.struct/appleid.md)
  Access the Apple ID of the person.
- [var nameComponents: PersonNameComponents?](deviceactivitydata/user-swift.struct/namecomponents.md)
  Access the name of the person.
### Defining the account role
- [var role: DeviceActivityData.User.FamilyRole](deviceactivitydata/user-swift.struct/role.md)
  Access the role of the person.
- [DeviceActivityData.User.FamilyRole](deviceactivitydata/user-swift.struct/familyrole.md)
  Role of a person in their iCloud family.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [var user: DeviceActivityData.User](deviceactivitydata/user-swift.property.md)
  Access the person associated with the activity report.
- [var device: DeviceActivityData.Device](deviceactivitydata/device-swift.property.md)
  Access the device associated with the activity report.
- [DeviceActivityData.Device](deviceactivitydata/device-swift.struct.md)
  Device information for activity reporting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct)*