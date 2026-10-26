# MdmDeviceDetail.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The attributes for a device management service enrolled device detail resource.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object MdmDeviceDetail.Attributes
```

## Properties

- `bluetoothMacAddress` (string): The Bluetooth MAC address of the device.
- `deviceEraseStatus` (DeviceEraseStatus): The erase status of the device.
- `deviceLockStatus` (DeviceLockStatus): The lock status of the device.
- `deviceModel` (string): The model of the device.
- `deviceName` (string): The name of the device.
- `ethernetMacAddress` (string): The Ethernet MAC address of the device.
- `imei` ([string]): The IMEI numbers of the device.
- `isFileVaultEnabled` (boolean): A Boolean value indicating whether FileVault is enabled on the device.
- `isFirewallEnabled` (boolean): A Boolean value indicating whether the firewall is enabled on the device.
- `lastCheckInDateTime` (date-time): The date and time the device last checked in.
- `lostModeStatus` (LostModeStatus): The lost mode status of the device.
- `meid` ([string]): The Mobile Equipment Identifier numbers of the device.
- `osVersion` (string): The operating system version of the device.
- `platform` (string): The platform of the device.
- `serialNumber` (string): The serial number of the device.
- `storageFreeCapacity` (integer): The free storage capacity of the device, in bytes.
- `storageTotalCapacity` (integer): The total storage capacity of the device, in bytes.
- `wifiMacAddress` (string): The Wi-Fi MAC address of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmdevicedetail/attributes-data.dictionary)*