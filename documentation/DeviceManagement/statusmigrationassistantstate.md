# StatusMigrationAssistantState

**Framework**: Device Management  
**Kind**: dictionary

The current migration state of the system.

**Availability**:
- macOS 26.4+ (Beta)

## Declaration

```swift
object StatusMigrationAssistantState
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | macOS |
| Allowed in user scope | NA |

## Properties

- `migration-assistant.state` (string) *(required)*: The current migration state of the system, which has the following possible values: - `none`: Migration has not started yet or no migration has taken place.
- `migrating`: Migration is in progress.
- `completed`: Migration has completed successfully.
- `failed`: Migration has failed.
- `cancelled`: The user cancelled migration.
- `unknown`: Migration status is unknown.

## See Also

- [object StatusReport](statusreport.md)
- [object StatusAppManagedList](statusappmanagedlist.md)
  The device’s declarative managed apps.
- [object StatusDeviceBatteryHealth](statusdevicebatteryhealth.md)
  The device’s battery health.
- [object StatusDeviceModelFamily](statusdevicemodelfamily.md)
  A status report of the device’s hardware family.
- [object StatusDeviceModelIdentifier](statusdevicemodelidentifier.md)
  A status report of the device’s hardware identifier.
- [object StatusDeviceModelMarketingName](statusdevicemodelmarketingname.md)
  A status report of the device’s marketing name.
- [object StatusDeviceModelNumber](statusdevicemodelnumber.md)
  A status report of the device’s hardware number.
- [object StatusDeviceOperatingSystemBuildVersion](statusdeviceoperatingsystembuildversion.md)
  A status report of the device’s software build identifier.
- [object StatusDeviceOperatingSystemFamily](statusdeviceoperatingsystemfamily.md)
  A status report of the device’s operating system family.
- [object StatusDeviceOperatingSystemMarketingName](statusdeviceoperatingsystemmarketingname.md)
  A status report of the device’s operating system marketing name.
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  A status report of the device’s operating system supplemental build identifier.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  A status report of the device’s operating system’s Background Security Improvement identifier.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  A status report of the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  A status report of the device’s serial number.
- [object StatusDeviceUDID](statusdeviceudid.md)
  A status report of the device’s UDID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusmigrationassistantstate)*