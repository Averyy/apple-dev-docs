# SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity

**Framework**: Device Management  
**Kind**: dictionary

Reports which security features the user disables in `recoveryOS`. This property is only present for a Mac with Apple silicon when `SecureBootLevel` is `medium`.

**Availability**:
- macOS 11.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SecurityInfoResponse.SecurityInfo.SecureBoot.ReducedSecurity
```

#### Discussion

Available in iOS 11 and later.

## Properties

- `AllowsAnyAppleSignedOS` (string): If ‘true’, allows any signed version of trusted system software from Apple to run.
- `AllowsMDM` (string): If ‘true’, the MDM server controls kernel extensions and software updates.
- `AllowsUserKextApproval` (string): If ‘true’, the user has control over kernel extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/securityinforesponse/securityinfo-data.dictionary/secureboot-data.dictionary/reducedsecurity-data.dictionary)*