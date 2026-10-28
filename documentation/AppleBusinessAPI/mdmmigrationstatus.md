# MdmMigrationStatus

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

Strings that represent the state of a device’s device management service migration.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
string MdmMigrationStatus
```

## Possible Values

- `REQUESTED`
- `STARTED`
- `SUCCESS`
- `FAILED`

## Discussion

- Possible Values

  - REQUESTED: The migration has been requested but hasn’t started.
  - STARTED: The device has started the device management service migration.
  - SUCCESS: The device successfully completed the device management service migration.
  - FAILED: The device failed to complete the device management service migration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/mdmmigrationstatus)*