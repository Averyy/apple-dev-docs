# VppAssignment

**Framework**: Device Management  
**Kind**: dictionary

An assignment’s properties and their values.

**Availability**:
- VPP License Management 1.1+

## Declaration

```swift
object VppAssignment
```

## Properties

- `adamIdStr` (string): The unique identifier for a product in the iTunes Store.
- `clientUserIdStr` (string): The client user ID of the user that the device is currently assigned to.
- `pricingParam` (string): The quality of a product in the iTunes Store. Possible values are: - `STDQ`: Standard quality
- `PLUS`: High quality
- `serialNumber` (string): The device’s serial number that the license is currently assigned to.

## See Also

- [object VppAsset](vppasset.md)
  A particular asset in the purchase program.
- [object VppLicense](vpplicense.md)
  A license for a product in the purchase program.
- [object VppAssociation](vppassociation.md)
  An association between a license and a user or device.
- [object VppUser](vppuser.md)
  A user within the purchase program.
- [object VppLocation](vpplocation.md)
  A location used for managing purchases.
- [object VppErrorCode](vpperrorcode.md)
  An error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppassignment)*