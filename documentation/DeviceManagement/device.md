# Device

**Framework**: Device Management  
**Kind**: dictionary

A device’s properties and their values.

**Availability**:
- Device Assignment Services 5.0+

## Declaration

```swift
object Device
```

## Properties

- `asset_tag` (string): The device’s asset tag.
- `color` (string): The color of the device.
- `description` (string): A description of the device.
- `device_assigned_by` (string): The email of the person who assigned the device.
- `device_assigned_date` (string): A time stamp in ISO 8601 format that indicates when the device was assigned to the MDM server.
- `device_family` (string): The device’s Apple product family: `iPad`, `iPhone`, `iPod`, `Mac`, `AppleTV`, or `Vision`. This key is valid in X-Server-Protocol-Version 2 and later.
- `mdm_migration_deadline` (string): A time stamp in ISO 8601 format that indicates the MDM migration deadline. This key is valid with X-Server-Protocol-Version 8 and later.
- `model` (string): The model name.
- `op_date` (string): A time stamp in ISO 8601 format that indicates when the device was added, updated, or deleted. If the value of `op_type` is added, this is the same as `device_assigned_date`. This field is only applicable with the [`Sync the List of Devices`](sync-devices.md) command.
- `op_type` (string): Indicates whether the device was added (assigned to the MDM server), modified, or deleted. Contains one of the following strings: `added`, `modified`, or `deleted`. This field is only applicable with the `sync the list of devices` command.
- `os` (string): The device’s operating system: `iOS`, `iPadOS`, `OSX`, `tvOS`, or `visionOS`. This key is valid in X-Server-Protocol-Version 2 and later. With X-Server-Protocol-Version 7 and later, iPad product os will return `iPadOS`.
- `profile_assign_time` (string): A time stamp in ISO 8601 format that indicates when a profile was assigned to the device.
- `profile_push_time` (string): A time stamp in ISO 8601 format that indicates when a profile was pushed to the device.
- `profile_status` (string): The status of profile installation—either `empty`, `assigned`, `pushed`, or `removed`.
- `profile_uuid` (string): The unique ID of the assigned profile.
- `serial_number` (string): The device’s serial number.

## See Also

- [object MachineInfo](machineinfo.md)
  A device’s information in response to a MDM enrollment profile request.
- [object Profile](profile.md)
  A profile’s properties and their values.
- [object Limit](limit.md)
  A ranged limit.
- [object Url](url.md)
  A URL object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device)*