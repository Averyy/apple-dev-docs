# OneTimeChargeItemV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object OneTimeChargeItemV1
```

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `partners` ([Partner])
- `price` (price) *(required)*

## See Also

### One-time charge creation in the app
- [object OneTimeChargeCreateRequest](./onetimechargecreaterequest.md)
  The request data your app provides when a customer purchases a one-time-charge product.
- [object OneTimeChargeItem](./onetimechargeitem.md)
  The details of a one-time charge product, including its display name, price, SKU, and metadata.
- [object OneTimeChargeCreateRequestV1](./onetimechargecreaterequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargeitemv1)*