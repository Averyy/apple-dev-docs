# EducationConfiguration.DeviceGroupsItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A device group in the organization.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 9.3+
- macOS 10.14+

## Declaration

```
object EducationConfiguration.DeviceGroupsItem
```

## Properties

- `Identifier` (string) *(required)*: The unique identifier for the device group in the organization.
- `Name` (string) *(required)*: The name of the device group, which must be unique in the organization.
- `SerialNumbers` ([string]) *(required)*: The serial numbers of the devices in the group.

## See Also

### Objects
- [object EducationConfiguration.DepartmentsItem](./departmentsitem.md)
  A department in the organization.
- [object EducationConfiguration.GroupsItem](./groupsitem.md)
  An array of dictionaries defining groups.
- [object EducationConfiguration.UsersItem](./usersitem.md)
  A user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/educationconfiguration/devicegroupsitem)*