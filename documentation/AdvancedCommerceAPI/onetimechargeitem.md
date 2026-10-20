# OneTimeChargeItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The details of a one-time charge product, including its display name, price, SKU, and metadata.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object OneTimeChargeItem
```

## Mentions

- [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md)

## Properties

- `description` (description) *(required)*: A description of the product that doesn’t display to customers.

  **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: The product name, suitable for display to customers.

  **Maximum Length**: `30`
- `price` (price) *(required)*: The price, in milliunits of the currency, of the one-time charge product.
- `SKU` (SKU) *(required)*: The product identifier.

  **Maximum Length**: `128`

## See Also

### One-time charge creation in the app
- [object OneTimeChargeCreateRequest](./onetimechargecreaterequest.md)
  The request data your app provides when a customer purchases a one-time-charge product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargeitem)*