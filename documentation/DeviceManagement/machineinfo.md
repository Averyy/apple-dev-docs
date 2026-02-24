# MachineInfo

**Framework**: Device Management  
**Kind**: dictionary

A device’s information in response to a MDM enrollment profile request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object MachineInfo
```

## Mentions

- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)

#### Discussion

This dictionary is CMS-signed with the device identity certificate. The system includes the device’s certificate and all necessary intermediate certificates. The certificate chain should validate against the Apple Root CA.

## Properties

- `IMEI` (string): The device’s IMEI (if available).
- `LANGUAGE` (string): The user’s currently-selected language, for example, `en`.
- `MANDATORY_SOFTWARE_UPDATE_REQUIRED` (boolean): If `true`, indicates that the device requires a mandatory software update during Setup Assistant. The MDM server can return a 403 with a [`ErrorCodeSoftwareUpdateRequired`](errorcodesoftwareupdaterequired.md) error to force the device to update to a specific version instead of the device choosing a version. Available on macOS 26.1 and later.
- `MDM_CAN_REQUEST_PSSO_CONFIG` (boolean): If `true`, indicates that the server can trigger the device to do a required Platform SSO authentication before enrolling. Available on macOS 26 and later.
- `MDM_CAN_REQUEST_SOFTWARE_UPDATE` (boolean): If `true`, indicates that the server can trigger the device to do a required software update. Available on iOS 17 and later, and macOS 14 and later.
- `MEID` (string): The device’s MEID (if available).
- `OS_VERSION` (string) *(required)*: The OS version installed on the device, for example, 17.0. Available on iOS 17 and later, macOS 14 and later, tvOS 17 and later, and watchOS 10 and later.
- `PAIRING_TOKEN` (data): The pairing token to validate when a watch is enrolling. Available on watchOS 10 and later.
- `PRODUCT` (string) *(required)*: The device’s product type, for example, `iPhone5,1`.
- `SERIAL` (string) *(required)*: The device’s serial number.
- `SOFTWARE_UPDATE_DEVICE_ID` (string): The device model identifier used to lookup available OS updates through https://gdmf.apple.com/v2/pmv. Available on iOS 17.4 and later, macOS 14.4 and later, and visionOS 1.1 and later.
- `SUPPLEMENTAL_BUILD_VERSION` (string): The device’s operating system supplemental build version (if available). Available on iOS 17 and later, macOS 14 and later, tvOS 17 and later, and watchOS 10 and later.
- `SUPPLEMENTAL_OS_VERSION_EXTRA` (string): The device’s operating system supplemental OS version extra (if available). Available on iOS 17 and later, macOS 14 and later, tvOS 17 and later, and watchOS 10 and later.
- `UDID` (string) *(required)*: The device’s UDID.
- `VERSION` (string) *(required)*: The build version installed on the device, for example, `7A182`.

## See Also

- [object Device](device.md)
  A device’s properties and their values.
- [object Profile](profile.md)
  A profile’s properties and their values.
- [object Limit](limit.md)
  A ranged limit.
- [object Url](url.md)
  A URL object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/machineinfo)*