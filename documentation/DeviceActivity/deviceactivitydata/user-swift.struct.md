# DeviceActivityData.User

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

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
- [var appleID: String?](./user-swift.struct/appleid.md)
  Access the Apple ID of the person.
- [var nameComponents: PersonNameComponents?](./user-swift.struct/namecomponents.md)
  Access the name of the person.
### Defining the account role
- [var role: DeviceActivityData.User.FamilyRole](./user-swift.struct/role.md)
  Access the role of the person.
- [DeviceActivityData.User.FamilyRole](./user-swift.struct/familyrole.md)
  Role of a person in their iCloud family.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing device and user information
- [var user: DeviceActivityData.User](./user-swift.property.md)
  Access the person associated with the activity report.
- [var device: DeviceActivityData.Device](./device-swift.property.md)
  Access the device associated with the activity report.
- [DeviceActivityData.Device](./device-swift.struct.md)
  Device information for activity reporting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct)*