# Devices

**Framework**: Appstoreconnectapi

Register devices for development and testing.

#### Overview

A `devices` resource represents the iOS, Apple TV, Apple Watch, and Mac devices that you register to use for development and testing. You can register a limited number of new devices and get information about them.

> **Note**:  You can only remove registered devices through the Apple Developer website.

## Topics

### Registering a Device
- [Register a New Device](post-v1-devices.md)
  Register a new device for app development.
### Getting Device Information
- [List Devices](get-v1-devices.md)
  Find and list devices registered to your team.
- [Read Device Information](get-v1-devices-_id_.md)
  Get information for a specific device registered to your team.
### Modifying Device Metadata
- [Modify a Registered Device](patch-v1-devices-_id_.md)
  Update the name or status of a specific device.
### Objects
- [object Device](device.md)
  The data structure that represents a Devices resource.
- [object DevicesWithoutIncludesResponse](deviceswithoutincludesresponse.md)
- [object DeviceCreateRequest](devicecreaterequest.md)
  The request body you use to create a Device.
- [object DeviceUpdateRequest](deviceupdaterequest.md)
  The request body you use to update a Device.
- [object DeviceResponse](deviceresponse.md)
  A response that contains a single Devices resource.
- [object DevicesResponse](devicesresponse.md)
  A response that contains a list of Devices resources.

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI/devices)*