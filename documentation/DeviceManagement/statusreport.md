# StatusReport

**Framework**: Device Management  
**Kind**: dictionary

A status report of the device’s current state.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusReport
```

## Mentions

- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)

#### Discussion

Devices report status incrementally: in effect, the device sends status reports that only contain status items that have changed since the device last sent a successful status report. The device determines a status report has been successfully sent only when it receives an HTTP 200 status code from the server, in response to the status report request. If the response status code indicates an error, the device resends the status items in the next report, along with any others that may have since changed.

When a device activates a status subscription, any status items that the device hasn’t reported to the server, are immediately sent in a status report. This provides the server with initial values for the status items, to assist with processing incremental updates later.

Status items that use an array as their value, are also reported incrementally. Thus items in the array are only included when their value is different from what was successfully sent before. This allows status reporting to efficiently use network bandwidth by not sending every item in the array, even when they’re unchanged. To support this behavior the following applies to the schema for objects used in status item arrays:

- Every status item array value object has an `identifier` whose value is an appropriate unique identifier for the object in the array of objects that forms the status item value. In many cases this is an opaque identifier, such as a UUID, but in others it may be a unique identifier for the underlying object, such as an app bundle id.
- Other keys are present, and are specific to the type of object included in the status report (for example, accounts might contain a key for the server URL, or apps might contain a key for the app name).
- The `removed` key, set to a value of `true`, indicates when a device has removed a previously reported array object. In that case, the device reports only the `identifier` and `removed` keys in the object in the status report.

The server uses the `identifier` value to determine how to update its representation of the device status:

- If the `identifier` value doesn’t match any in the status item array the server already has, and the `removed` key isn’t present, then the reported object is a new array object that the server must add to the representation of the device status.
- If the `identifier` value matches an item in the status item array the server already has, and the `removed` key isn’t present, then the reported object is an update, and the entire object must replace the one with the matching key in the representation of the device status.
- If the `identifier` value matches an item in the status item array the server already has, and only the `removed` key is also present, then the report indicates a removal, and the server must remove the object with the matching key in the representation of the device status.

Applying these rules ensures the server’s state correctly matches that of the device.

## Topics

### Supporting Objects
- [object StatusReport.Error](statusreport/error.md)
  A status report’s error that contains the status item and the reasons for the error.
- [object StatusReport.StatusItems](statusreport/statusitems-data.dictionary.md)
  The status items for a report.

## See Also

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
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  A status report of the device’s operating system supplemental build identifier.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  A status report of the device’s operating system’s rapid security response identifier.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  A status report of the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  A status report of the device’s serial number.
- [object StatusDeviceUDID](statusdeviceudid.md)
  A status report of the device’s UDID.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The enabled status of the File Vault.
- [object StatusManagementClientCapabilities](statusmanagementclientcapabilities.md)
  A status report of the client’s protocol capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusreport)*