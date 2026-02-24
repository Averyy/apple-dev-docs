# ResponseAsset

**Framework**: Device Management  
**Kind**: dictionary

The asset that the organization owns.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ResponseAsset
```

## Mentions

- [Managing Assets](managing-assets.md)

## Properties

- `adamId` (string): The unique identifier for the product in the store.
- `assignedCount` (int32): The assigned amount of the asset.
- `availableCount` (int32): The available amount of the asset.
- `deviceAssignable` (boolean): The flag denoting whether the asset is device-assignable.
- `pricingParam` (string): The quality of the product in the store.
- `productType` (string): The asset product type.
- `retiredCount` (int32): The retired amount of the asset.
- `revocable` (boolean): The flag denoting whether the asset is revocable.
- `totalCount` (int32): The total amount of the asset.
- `supportedPlatforms` ([string]): The platforms that the asset supports.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
- [object RequestUser](requestuser.md)
  The requested user in the organization.
- [object ResponseUser](responseuser.md)
  The user in the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/responseasset)*