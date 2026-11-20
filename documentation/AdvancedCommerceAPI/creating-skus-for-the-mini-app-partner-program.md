# Creating SKUs for the Mini Apps Partner Program

**Framework**: Advanced Commerce API  
**Role**: Article

Define display names and SKUs for one-time charges and subscriptions in the Mini Apps Partner Program.

## Overview

If your app supports the Mini Apps Partner Program, use the Advanced Commerce APIs when a customer initiates a one-time purchase ([`OneTimeChargeCreateRequest`](./onetimechargecreaterequest.md)), or purchases a subscription ([`SubscriptionCreateRequest`](./subscriptioncreaterequest.md)).

The Mini Apps Partner Program has specific requirements for defining the SKUs and the product display names, so they fully identify each mini app product. Follow these guidelines to create display names and SKUs for products you offer through the Mini Apps Partner Program and describe the format for one-time purchases and subscriptions. See [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md) for additional guidance.

## Describe the mini app and mini apps partner with metadata

The following table lists the identifiers that make up mini app display names and SKUs.

| Identifier | Description | Example |
| --- | --- | --- |
| `[Mini App Name]` | The name of the mini app | `Anne’s Game` |
| `[Mini App Product Name]` | The name of the product associated with the mini app | `Boost Pack` or `Pro Monthly` |
| `[Mini App Partner Name]` | The name of the mini app partner | `Apple_Seed` |
| `[Mini App Partner ID]` | The unique identifier you set for the mini app partner | `WC123` |
| `[Mini App SKU Identifier]` | The unique identifier you set for the Mini App Product | `boost_pack_id, pro_monthly_id` |

> ❗ **Important**: V1 and V2 endpoints in Advanced Commerce API support the [`Partner`](./partner.md) object.

To learn more about eligibility and apply for access to the Advanced Commerce API, see [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/). For more about eligibility and to apply for access to the Mini Apps Partner Program, see [Mini Apps Partner Program](https://developer.apple.com/programs/mini-apps-partner/).

## Initiate a one-time charge purchase

To initiate a one-time charge for a mini app product, use the [`OneTimeChargeCreateRequest`](./onetimechargecreaterequest.md).

Create the mini app display name using the format `[Mini App Name] - [Mini App Product Name]`. Using the sample values from the table above, `item.displayName` would look like the following example:

```
items.displayName = "Anne’s Game - Boost Pack"
```

- The display name can use a maximum of 30 characters.

Create the `items.SKU` using the `[Mini App SKU Identifier]` value.

Using the sample values from the table above, the `items.SKU` would look like the following example:

```
items.SKU = "boost_pack_id"
```

- The SKU value needs to be unique within your app and can use a maximum of 128 characters.

Provide `[Mini App Partner Name]` and `[Mini App Partner ID]` for the purchase associated with the Mini App.

```
partners.id = "WC123"
```

```
partners.name = "Apple Seed"
```

### Example: Create a one-time charge

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
    "items":[{
        "SKU": "boost_pack_id",
        "displayName": "Anne’s Game - Boost Pack",
        "description": "Boost Pack for Anne's Game",
        "price": 4990,
        "partners": [
            {
                "id": "WC123",
                "name": "Apple Seed"
            }
        ]
    }]
}
```

## Initiate a subscription purchase

To initiate a subscription purchase, use the [`SubscriptionCreateRequest`](./subscriptioncreaterequest.md) API.

Create the display name and SKU in [`SubscriptionCreateItem`](./subscriptioncreateitem.md) to include the specified details and ensure it conforms to the indicated formatting and length limitations.

The mini app’s display name can use a maximum of 30 characters, and follows this format: `descriptors.displayName` = `[Mini App Name]`, for example

```
descriptors.displayName = "Anne's Game"
```

The product display name can use a maximum of 30 characters and follow this format: `items.displayName` = `[Mini App Product Name]`, for example

```
items.displayName = "Pro Monthly"
```

The SKU value needs to be unique within your app, can use a maximum of 128 characters, and follows this format: `items.SKU` = `[Mini App SKU Identifier]`; for example:

```
items.SKU = "pro_monthly_id"
```

Provide `[Mini App Partner Name]` and `[Mini App Partner ID]` for the purchase associated with the Mini App.

```
partners.id = "WC123"
```

```
partners.name = "Apple Seed"
```

### Example: Request a subscription purchase

```json
{
    "operation": "CREATE_SUBSCRIPTION", 
    "version": "2",
    "requestInfo": {
        "requestReferenceId": "f55df048-4cd8-4261-b404-b6f813ff70e5"
    },
    "storefront": "USA",
    "currency": "USD",
    "taxCode": "C003-00-1",
    "displayName": "Anne's Game",
    "period": "P1M",
    "items": [
        {
            "SKU": "pro_monthly_id",
            "displayName": "Pro Monthly",
            "description": "Subscription for Anne's Game",
            "price": 6990,
            "partners": [{
                "id": "WC123",
                "name": "Apple Seed"
            }]
        }
    ]
}
```

## See Also

### Generic product IDs and SKUs
- [Setting up generic product identifiers](./setting-up-generic-product-identifiers.md)
  Configure the generic product IDs in App Store Connect that the Advanced Commerce API requires.
- [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md)
  Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
  Sell subscriptions that a customer buys for a group through Group Purchases, with per-seat or volume discount pricing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/creating-skus-for-the-mini-app-partner-program)*