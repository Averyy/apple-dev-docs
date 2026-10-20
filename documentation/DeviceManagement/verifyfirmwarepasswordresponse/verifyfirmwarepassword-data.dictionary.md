# VerifyFirmwarePasswordResponse.VerifyFirmwarePassword

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary containing the results of the command.

**Availability**:
- macOS 10.13+

## Declaration

```
object VerifyFirmwarePasswordResponse.VerifyFirmwarePassword
```

## Properties

- `PasswordVerified` (boolean) *(required)*: If ‘true’, the provided password matched the firmware password set for the device.

## See Also

### Objects
- [object VerifyFirmwarePasswordResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verifyfirmwarepasswordresponse/verifyfirmwarepassword-data.dictionary)*