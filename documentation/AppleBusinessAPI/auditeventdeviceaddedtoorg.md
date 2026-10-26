# AuditEventDeviceAddedToOrg

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data structure that represents the event data for a device added to organization audit event.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
object AuditEventDeviceAddedToOrg
```

## Properties

- `serialNumber` (string): Serial number of the device, unique to that device.
- `purchaseSourceType` (AuditEventPurchaseSourceType): The way the device was added into Apple Business.
- `purchaseSourceId` (string): The unique id for the purchase source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/auditeventdeviceaddedtoorg)*