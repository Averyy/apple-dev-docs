# DeviceActivityData.User.FamilyRole

**Framework**: Device Activity  
**Kind**: enum  
**Role**: Enumeration

Role of a person in their iCloud family.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum FamilyRole
```

#### Overview

If the person is not signed into an iCloud account or in an iCloud family, they are an individual.

## Topics

### Defining family roles
- [DeviceActivityData.User.FamilyRole.individual](./familyrole/individual.md)
  A person who has authorized your app.
- [DeviceActivityData.User.FamilyRole.child](./familyrole/child.md)
  A child being managed by a parent or guardian in their iCloud family.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)

## See Also

### Defining the account role
- [var role: DeviceActivityData.User.FamilyRole](./role.md)
  Access the role of the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/user-swift.struct/familyrole)*