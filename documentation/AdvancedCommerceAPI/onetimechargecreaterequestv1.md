# OneTimeChargeCreateRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object OneTimeChargeCreateRequestV1
```

## Properties

- `currency` (currency) *(required)*
- `item` (OneTimeChargeItemV1) *(required)*
- `operation` (string) *(required)*: **Allowed Values**: `CREATE_ONE_TIME_CHARGE`
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode) *(required)*
- `version` (versionV1) *(required)*

## See Also

### One-time charge creation in the app
- [object OneTimeChargeCreateRequest](./onetimechargecreaterequest.md)
  The request data your app provides when a customer purchases a one-time-charge product.
- [object OneTimeChargeItem](./onetimechargeitem.md)
  The details of a one-time charge product, including its display name, price, SKU, and metadata.
- [object OneTimeChargeItemV1](./onetimechargeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargecreaterequestv1)*