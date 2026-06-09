# StatusPasscodeCompliance

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s passcode compliance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object StatusPasscodeCompliance
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
        "is-compliant": true
    }
}
```

## Properties

- `passcode.is-compliant` (boolean) *(required)*: If `true`, the passcode is in compliance with all passcode policies set on the device. If `false`, the passcode isn’t in compliance with one or more passcode policies set on the device. When there are no passcode policies on the device, this value `true`.

## See Also

- [object StatusPasscodeIsPresent](statuspasscodeispresent.md)
  The status item that reports whether the device has a passcode.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The status item that reports whether FileVault is enabled.
- [object StatusSecurityCertificateList](statussecuritycertificatelist.md)
  The status item that lists the device’s managed certificates.
- [object StatusSecurityLockdownMode](statussecuritylockdownmode.md)
  The status item that reports the device’s Lockdown Mode state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statuspasscodecompliance)*