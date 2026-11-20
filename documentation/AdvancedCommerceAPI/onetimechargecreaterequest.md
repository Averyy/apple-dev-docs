# OneTimeChargeCreateRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request data your app provides when a customer purchases a one-time-charge product.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object OneTimeChargeCreateRequest
```

## Mentions

- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)
- [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md)
- [Advanced Commerce API changelog](./changelog.md)

### Example

```json
{
    "operation": "CREATE_ONE_TIME_CHARGE",
    "version": "2",                     
    "requestInfo": {
        "requestReferenceId": "f55df048-4cd8-4261-b404-b6f813ff70e5"
    },
    "currency": "USD",
    "taxCode": "C003-00-2", 
    "storefront": "USA",
    "items": [{
        "SKU": "BOOK_SHERLOCK_HOLMES",
        "displayName": "Sherlock Holmes", 
        "description": "The Sherlock Holmes, 5th Edition",
        "price": 4990
    }]
}
```

## Properties

- `currency` (currency) *(required)*: The currency of the price of the product.
- `items` ([OneTimeChargeItem]) *(required)*
- `operation` (string) *(required)*: The constant that represents the operation of this request.

  **Allowed Values**: `CREATE_ONE_TIME_CHARGE`
- `requestInfo` (RequestInfo) *(required)*: The metadata of the request.
- `storefront` (storefront): The storefront for the transaction.
- `taxCode` (taxCode): The tax code for this product.
- `version` (version) *(required)*: The version number of the API.

## See Also

### One-time charge creation in the app
- [object OneTimeChargeItem](./onetimechargeitem.md)
  The details of a one-time charge product, including its display name, price, SKU, and metadata.
- [object OneTimeChargeCreateRequestV1](./onetimechargecreaterequestv1.md)
- [object OneTimeChargeItemV1](./onetimechargeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargecreaterequest)*