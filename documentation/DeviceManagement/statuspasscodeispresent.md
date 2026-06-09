# StatusPasscodeIsPresent

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports whether the device has a passcode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusPasscodeIsPresent
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, Shared iPad, visionOS, watchOS |
| Allowed in system scope | iOS, Shared iPad, visionOS, watchOS |
| Allowed in user scope | Shared iPad |

##### Status Item Example

```json
{
    "passcode": {
        "is-present": true
    }
}
```

## Properties

- `passcode.is-present` (boolean) *(required)*: If `true`, a passcode is present on the device. If `false`, a passcode isn’t present on the device. When a passcode is present, the specific attributes of the passcode, such as length or number of complex characters, aren’t reported. Instead, use the `passcode.is-compliant` status item to verify that the passcode complies with all passcode policies set on the device.

## See Also

- [object StatusPasscodeCompliance](statuspasscodecompliance.md)
  The status item that reports the device’s passcode compliance.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The status item that reports whether FileVault is enabled.
- [object StatusSecurityCertificateList](statussecuritycertificatelist.md)
  The status item that lists the device’s managed certificates.
- [object StatusSecurityLockdownMode](statussecuritylockdownmode.md)
  The status item that reports the device’s Lockdown Mode state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspasscodeispresent)*