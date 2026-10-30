# ActivationLockStatus.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes for an organization device’s Activation Lock status.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object ActivationLockStatus.Attributes
```

## Overview

> **Note**: When additional attributes are added by Apple, they appear automatically, without requiring a newer version of the API.

## Properties

- `isLocked` (boolean): Whether the device is currently Activation Locked.
- `lockType` (ActivationLockType): The type of Activation Lock on the device, if `isLocked` is `true`. Possible values: `MDM`, `USER`, `NONE`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/activationlockstatus/attributes-data.dictionary)*