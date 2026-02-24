# ActivationLockRequest

**Framework**: Device Management  
**Kind**: dictionary

Request enabling activation lock for a device.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ActivationLockRequest
```

## Properties

- `device` (string): Serial number of the device (required).
- `escrow_key` (string): Escrow key (optional). If the escrow key is not provided, the device will be locked to the person who created the MDM server in the portal. For information about creating an escrow key see [`Creating and Using Bypass Codes`](creating-and-using-bypass-codes.md).
- `lost_message` (string): Lost message to be displayed on the device (optional).

## See Also

- [object ActivationLockStatusResponse](activationlockstatusresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/activationlockrequest)*