# AuditEventDeviceRemovedFromOrg

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents the event data for a device removed from organization audit event.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object AuditEventDeviceRemovedFromOrg
```

## Properties

- `serialNumber` (string): Serial number of the device, unique to that device.
- `releaseEntityId` (string): The unique id of the releasing entity. In the case of releaseEntityType == USER this property is intentionally not populated since it’s already given by SUBJECT_TYPE and SUBJECT_ID.
- `releaseEntityType` (AuditEventReleaseEntityType): The type of entity that conducted the release/disown operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditeventdeviceremovedfromorg)*