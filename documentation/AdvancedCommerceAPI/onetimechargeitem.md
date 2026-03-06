# OneTimeChargeItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The details of a one-time charge product, including its display name, price, SKU, and metadata.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object OneTimeChargeItem
```

## Mentions

- [Creating SKUs for your In-App Purchases](creating-your-purchases.md)

## Properties

- `description` (description) *(required)*: A description of the product that doesn’t display to customers.
- `displayName` (displayName) *(required)*: The product name, suitable for display to customers.
- `price` (price) *(required)*: The price, in milliunits of the currency, of the one-time charge product.
- `SKU` (SKU) *(required)*: The product identifier.

## See Also

- [object OneTimeChargeCreateRequest](onetimechargecreaterequest.md)
  The request data your app provides when a customer purchases a one-time-charge product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargeitem)*