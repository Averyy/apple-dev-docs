# OrgDeviceActivityType

**Framework**: AppleSchoolManagerAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent organization device activities.

**Availability**:
- Apple School Manager API 1.8+

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

## Discussion

- Possible Values

  - ASSIGN_DEVICES:
  - UNASSIGN_DEVICES:
  - ASSIGN_DEVICES_WITH_MDM_MIGRATION_DEADLINE: Assign devices to a device management service and schedule a device management service migration by the given deadline.
  - UPDATE_MDM_MIGRATION_DEADLINE: Update the deadline for an in-progress device management service migration.
  - CANCEL_MDM_MIGRATION: Cancel an in-progress device management service migration.

## See Also

### Type Aliases
- [type AppleCareCoveragePaymentType](./applecarecoveragepaymenttype.md)
  Strings that represent AppleCare coverage payment types.
- [type AppleCareCoverageStatus](./applecarecoveragestatus.md)
  Strings that represent AppleCare coverage status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/orgdeviceactivitytype)*