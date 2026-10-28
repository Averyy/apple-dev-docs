# ActivationLockType

**Framework**: AppleSchoolManagerAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent the type of Activation Lock on a device.

**Availability**:
- Apple School Manager API 1.7+

## Declaration

```
string ActivationLockType
```

## Possible Values

- `MDM`
- `USER`
- `NONE`

## Discussion

- Possible Values

  - MDM: The device is Activation Locked by its device management service.
  - USER: The device is Activation Locked to a personal Apple Account.
  - NONE: The device isn’t Activation Locked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/activationlocktype)*