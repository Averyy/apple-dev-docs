# EducationConfiguration.GroupsItem

**Framework**: Device Management  
**Kind**: dictionary

An array of dictionaries defining groups.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.14+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EducationConfiguration.GroupsItem
```

## Properties

- `BeaconID` (integer) *(required)*: An unsigned 16 bit integer specifying this group’s unique beacon ID.
- `ConfigurationSource` (string): The source that provided this group, such as SIS, or MDM.
- `Description` (string): The description of the group.
- `DeviceGroupIdentifiers` ([string]): The identifiers that refer to entries in the `DeviceGroups` array to which the instructor can assign users from this class. Has no effect on the configuration of the Shared iPad login screen.
- `ImageURL` (string): Deprecated in iOS 9.3.1 and later. The URL of an image for the group.
- `LeaderIdentifiers` ([string]): The user identifiers that are leaders of this group.
- `MemberIdentifiers` ([string]) *(required)*: The entries in the Users array that are members of the group.
- `Name` (string) *(required)*: The display name of the group.

## See Also

- [object EducationConfiguration.DepartmentsItem](educationconfiguration/departmentsitem.md)
  A department in the organization.
- [object EducationConfiguration.DeviceGroupsItem](educationconfiguration/devicegroupsitem.md)
  A device group in the organization.
- [object EducationConfiguration.UsersItem](educationconfiguration/usersitem.md)
  A user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/educationconfiguration/groupsitem)*