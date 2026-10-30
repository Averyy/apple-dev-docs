# OrgDeviceActivityType

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent organization device activities.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
string OrgDeviceActivityType
```

## Possible Values

- `ASSIGN_DEVICES`
- `UNASSIGN_DEVICES`
- `ASSIGN_DEVICES_WITH_MDM_MIGRATION_DEADLINE`
- `UPDATE_MDM_MIGRATION_DEADLINE`
- `CANCEL_MDM_MIGRATION`
- `RELEASE_DEVICES`

## Discussion

- Possible Values

  - ASSIGN_DEVICES: Assign devices to a device management service
  - UNASSIGN_DEVICES: Unassign devices from a device management service
  - ASSIGN_DEVICES_WITH_MDM_MIGRATION_DEADLINE: Assign devices to a device management service and schedule a device management service migration by the given deadline.
  - UPDATE_MDM_MIGRATION_DEADLINE: Update the deadline for an in-progress device management service migration.
  - CANCEL_MDM_MIGRATION: Cancel an in-progress device management service migration.
  - RELEASE_DEVICES: Release devices from an organization

## See Also

### Type Aliases
- [type AppleCareCoveragePaymentType](./applecarecoveragepaymenttype.md)
  Strings that represent AppleCare coverage payment types.
- [type AppleCareCoverageStatus](./applecarecoveragestatus.md)
  Strings that represent AppleCare coverage status.
- [type UserStatus](./userstatus.md)
  Strings that represent user statuses.
- [type UserPhoneNumberType](./userphonenumbertype.md)
  Strings that represent phone number types.
- [type UserGroupStatus](./usergroupstatus.md)
  Strings that represent user group statuses.
- [type UserGroupType](./usergrouptype.md)
  Strings that represent user group types.
- [type SupportedOS](./supportedos.md)
  The supported operating systems for an app.
- [type BlueprintStatus](./blueprintstatus.md)
  The status of a Blueprint.
- [type ConfigurationType](./configurationtype.md)
  The type of Configuration profile.
- [type ConfigurationPlatform](./configurationplatform.md)
  The platform that a Configuration targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/orgdeviceactivitytype)*