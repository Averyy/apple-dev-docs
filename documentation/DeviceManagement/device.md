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
- `bluetooth_mac_address` (string): The device’s Bluetooth MAC address. This key is valid in X-Server-Protocol-Version 10 and later.
- `color` (string): The color of the device.
- `description` (string): A description of the device.
- `device_assigned_by` (string): The email of the person who assigned the device.
- `device_assigned_date` (string): A time stamp in ISO 8601 format that indicates when the device was assigned to the MDM server.
- `device_family` (string): The device’s Apple product family: `iPad`, `iPhone`, `iPod`, `Mac`, `AppleTV`, or `Vision`. This key is valid in X-Server-Protocol-Version 2 and later.
- `eid` (string): The Embedded Identity Document (EID), sometimes known as the CSN, that uniquely identifies the eSIM chip built into the device. This key is valid in X-Server-Protocol-Version 10 and later.
- `ethernet_mac_address` (string): The device’s Ethernet MAC address. This key is valid in X-Server-Protocol-Version 10 and later.
- `imei` ([string]): An array of strings containing the International Mobile Equipment Identity (IMEI) numbers that identify the device. This key is valid in X-Server-Protocol-Version 10 and later.
- `is_replacement_device` (boolean): If `true`, the device is a replacement for another device. Use [`Get Replacement Details`](get-replacement-details.md) to retrieve information about the device it replaced. This key is valid in X-Server-Protocol-Version 10 and later.
- `mdm_migration_deadline` (string): A time stamp in ISO 8601 format that indicates the MDM migration deadline. This key is valid with X-Server-Protocol-Version 8 and later.
- `meid` ([string]): An array of strings containing the Mobile Equipment Identifier (MEID) numbers that identify CDMA-based mobile devices. This key is valid in X-Server-Protocol-Version 10 and later.
- `model` (string): The model name.
- `op_date` (string): A time stamp in ISO 8601 format that indicates when the device was added, updated, or deleted. If the value of `op_type` is added, this is the same as `device_assigned_date`. This field is only applicable with the [`Sync the List of Devices`](sync-devices.md) command.
- `op_type` (string): Indicates whether the device was added (assigned to the MDM server), modified, or deleted. Contains one of the following strings: `added`, `modified`, or `deleted`. This field is only applicable with the `sync the list of devices` command.
- `os` (string): The device’s operating system: `iOS`, `iPadOS`, `OSX`, `tvOS`, or `visionOS`. This key is valid in X-Server-Protocol-Version 2 and later. With X-Server-Protocol-Version 7 and later, iPad product os will return `iPadOS`.
- `profile_assign_time` (string): A time stamp in ISO 8601 format that indicates when a profile was assigned to the device.
- `profile_push_time` (string): A time stamp in ISO 8601 format that indicates when a profile was pushed to the device.
- `profile_status` (string): The status of profile installation—either `empty`, `assigned`, `pushed`, or `removed`.
- `profile_uuid` (string): The unique ID of the assigned profile.
- `released_by_replacement` (boolean): If `true`, the device was released from the MDM server because it was replaced by another device. This key is only present with [`Sync the List of Devices`](sync-devices.md) when `op_type` is `deleted`. This key is valid in X-Server-Protocol-Version 10 and later.
- `serial_number` (string): The device’s serial number.
- `wifi_mac_address` (string): The device’s Wi-Fi MAC address. This key is valid in X-Server-Protocol-Version 10 and later.

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