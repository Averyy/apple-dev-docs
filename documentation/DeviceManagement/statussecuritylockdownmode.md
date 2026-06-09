# StatusSecurityLockdownMode

**Framework**: Device Management  
**Kind**: dictionary

The status item that reports the device’s Lockdown Mode state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
object StatusSecurityLockdownMode
```

#### Discussion

##### Status Item Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, watchOS |
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, macOS, watchOS |
| Allowed in user scope | N/A |

##### Status Item Example

```json
{
    "security": {
        "lockdown-mode": false
    }
}
```

## Properties

- `security.lockdown-mode` (boolean) *(required)*: If `true`, indicates that Lockdown Mode is enabled.

## See Also

- [object StatusPasscodeCompliance](statuspasscodecompliance.md)
  The status item that reports the device’s passcode compliance.
- [object StatusPasscodeIsPresent](statuspasscodeispresent.md)
  The status item that reports whether the device has a passcode.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The status item that reports whether FileVault is enabled.
- [object StatusSecurityCertificateList](statussecuritycertificatelist.md)
  The status item that lists the device’s managed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statussecuritylockdownmode)*