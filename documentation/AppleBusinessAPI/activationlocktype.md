# ActivationLockType

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent the type of Activation Lock on a device.

**Availability**:
- Apple Business API 2.7+

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

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/activationlocktype)*