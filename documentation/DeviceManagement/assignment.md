# Assignment

**Framework**: Device Management  
**Kind**: dictionary

The asset assignment for a user or device.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Assignment
```

## Mentions

- [Subscribing to Notifications](subscribing-to-notifications.md)

## Properties

- `adamId` (string): The unique identifier for a product in the store.
- `clientUserId` (string): The unique identifier for an active user in your organization.
- `pricingParam` (string): The quality of a product in the store.
- `serialNumber` (string): The unique identifier for a device in your organization.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object RequestUser](requestuser.md)
  The requested user in the organization.
- [object ResponseUser](responseuser.md)
  The user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assignment)*