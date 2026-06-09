# StatusDiskManagementFileVaultEnabled

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports whether FileVault is enabled.

**Availability**:
- macOS 14.0+

## Declaration

```swift
object StatusDiskManagementFileVaultEnabled
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | macOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | macOS |
| Allowed in system scope | macOS |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "diskmanagement": {
        "filevault": {
            "enabled": true
        }
    }
}
```

## Properties

- `diskmanagement.filevault.enabled` (boolean) *(required)*: A Boolean value that specifies the File Vault enabled status on the device.

## See Also

- [object StatusPasscodeCompliance](statuspasscodecompliance.md)
  The status item that reports the device’s passcode compliance.
- [object StatusPasscodeIsPresent](statuspasscodeispresent.md)
  The status item that reports whether the device has a passcode.
- [object StatusSecurityCertificateList](statussecuritycertificatelist.md)
  The status item that lists the device’s managed certificates.
- [object StatusSecurityLockdownMode](statussecuritylockdownmode.md)
  The status item that reports the device’s Lockdown Mode state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusdiskmanagementfilevaultenabled)*