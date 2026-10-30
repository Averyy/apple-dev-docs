# OrgDevice.Attributes

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an organization device resource.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object OrgDevice.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `addedToOrgDateTime` (date-time): The date and time of adding the device to an organization.
- `releasedFromOrgDateTime` (date-time): The date and time the device was released from an organization.  This will be null if the device hasn’t been released.  Currently only querying by a single device is supported.  Batch device queries aren’t currently supported for this property.
- `color` (string): The color of the device.
- `deviceCapacity` (string): The capacity of the device.
- `deviceModel` (string): The model name.
- `eid` (string): The device’s EID (if available).
- `imei` ([string]): The device’s IMEI (if available).
- `meid` ([string]): The device’s MEID (if available).
- `wifiMacAddress` (string): The device’s Wi-Fi MAC address.
- `bluetoothMacAddress` (string): The device’s Bluetooth MAC address.
- `ethernetMacAddress` ([string]): The device’s built-in Ethernet MAC addresses.
- `orderDateTime` (date-time): The date and time of placing the device’s order.
- `orderNumber` (string): The order number of the device.
- `partNumber` (string): The part number of the device.
- `productFamily` (string): The device’s Apple product family: `iPhone`, `iPad`,`Mac`, `AppleTV`, `Watch`, or `Vision`
- `productType` (string): The device’s product type: (examples: `iPhone14,3`, `iPad13,4`,  `MacBookPro14,2`)
- `purchaseSourceType` (string): The device’s purchase source type: `APPLE`, `RESELLER`, or `MANUALLY_ADDED`
- `purchaseSourceId` (string): The unique ID of the purchase source type: Apple Customer Number or Reseller Number
- `serialNumber` (string): The device’s serial number.
- `status` (string): The devices status: ASSIGNED or UNASSIGNED. If ASSIGNED, use a separate API to get the information of the assigned server.
- `updatedDateTime` (date-time): The date and time of the most-recent update for the device.
- `isMdmMigrationCapable` (boolean): Whether the device is eligible for device management service migration.
- `mdmMigrationStatus` (MdmMigrationStatus): The device’s current device management service migration state, if a migration has been requested.
- `mdmMigrationDeadlineDateTime` (date-time): The deadline, in ISO 8601 format, by which the device needs to complete its device management service migration, if a migration has been requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary)*