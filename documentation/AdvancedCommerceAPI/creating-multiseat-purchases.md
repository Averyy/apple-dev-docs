# Creating multiseat purchases

**Framework**: Advanced Commerce API  
**Role**: Article

Sell subscriptions that a customer buys for a group through Group Purchases, with per-seat or volume discount pricing.

## Overview

A multiseat purchase is an auto-renewable subscription that a customer buys in a quantity greater than one. Each unit of quantity is a *seat*, and each seat gives one person access to your subscription. The customer who buys the seats, the *group purchaser*, holds the first seat and invites other people to join the group. The group purchaser pays for every seat; the people they invite don’t pay.

With the Advanced Commerce API, you sell multiseat subscriptions through Group Purchases on the App Store. You set the number of seats and their prices in the request that your app sends for the purchase, using the same generic product ID that you use for other subscriptions. For the customer experience, the invitation models, and how to grant access to the members of a group, see [Supporting multiseat purchases in your app](../StoreKit/supporting-multiseat-purchases-in-your-app.md).

Multiseat purchases require version 2 of the in-app requests and server endpoints. Set the `version` of each in-app request to `2`. A version 1 request for a multiseat subscription fails with [`SubsForGroupsRequiresLatestVersionError`](./subsforgroupsrequireslatestversionerror.md).

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

## Turn on multiseat purchasing

Before you offer group subscriptions, turn on multiseat purchasing for your generic product ID for subscriptions in App Store Connect. For more information, see [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions).

In your app, check [`supportsMultiSeatPurchase`](../StoreKit/advancedcommerceproduct/supportsmultiseatpurchase.md) before you offer a group subscription.

## Choose a pricing model

You set the price per seat in tiers, with one to five [`SeatPriceTier`](./seatpricetier.md) objects in the item’s `seatPriceTiers` array. The number of tiers determines the pricing model:

- **Per-seat pricing**: Provide a single tier with no `maximumSeatQuantity`. Every seat has the same price.
- **Volume discount pricing**: Provide two to five tiers. The price per seat decreases as the number of seats increases.

Follow these rules when you create the tiers:

- List the tiers in order, from the most expensive price per seat to the least expensive.
- Make the price of each tier lower than the price of the tier before it.
- Provide a `maximumSeatQuantity` for every tier except the last. The last tier has no upper limit, so omit it.

The `maximumSeatQuantity` value is the number of seats in a tier, not the position of the tier’s last seat. Seats fill the tiers in order, starting with the most expensive tier. For example, with tiers of 5 seats at 9.99 USD, 5 seats at 7.99 USD, and any further seats at 5.99 USD, a group of 8 seats includes 5 seats at 9.99 USD and 3 seats at 7.99 USD, for a total of 73.92 USD.

A multiseat subscription contains a single item, which can’t be a bundle or a suite. Provide either a `price` or `seatPriceTiers` for an item, not both.

## Create a group subscription

When the group purchaser buys a group subscription, send a [`SubscriptionCreateRequest`](./subscriptioncreaterequest.md) with a single [`SubscriptionCreateItem`](./subscriptioncreateitem.md). In the item, provide the following values instead of a `price`:

- **`seatPriceTiers`**: The complete set of tiers.
- **[`finalQuantity`](./finalquantity.md)**: The number of seats the group purchaser is buying.

Also provide the item’s `SKU`, and the `displayName` and `description` that the App Store shows to the customer. Your app signs the request and sends it with StoreKit; for more information, see [Sending Advanced Commerce API requests from your app](../StoreKit/sending-advanced-commerce-api-requests-from-your-app.md). For an example with per-seat pricing, see [`SubscriptionCreateRequest`](./subscriptioncreaterequest.md).

The seats and their tiers travel in the request that you sign for the purchase. The App Store calculates the total price from the tiers and the number of seats, and shows it on the payment sheet. A group holds up to 100 people, including the group purchaser. Before the group purchaser buys, show them in your app how the price per seat applies to the number of seats they choose.

After the purchase, the transaction’s `quantity` reports the number of seats, and its `price` is the average price per seat. The transaction’s [`TransactionMultiSeatInfo`](../AppStoreServerAPI/transactionmultiseatinfo.md) lists the seats bought at each price, and its `advancedCommerceInfo` items include the `seatPriceTiers` you provided. The group purchaser then invites people to fill the remaining seats, through invitations that Apple or your app hosts, depending on your setting in App Store Connect. For more information, see [`invitationManagement`](../AppStoreServerAPI/invitationmanagement.md).

### Example: Create a group subscription

In the following request and response:

- The group purchaser buys 8 seats of a group subscription with volume discount pricing. The first two tiers each cover 5 seats, and the last tier covers every seat after the tenth.
- The purchase includes 5 seats at the first tier’s price and 3 seats at the second tier’s price. The request still includes the last tier.
- In the decoded signed transaction, `quantity` is `8`, `multiSeatInfo.priceTiers` lists the seats at each price, and `price` is the average price per seat.
- The example doesn’t include optional fields in `requestInfo` or the tax fields in `advancedCommerceInfo`.

**Request**:

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "2",
    "requestInfo": {
        "requestReferenceId": "9a4d7e2b-1c3f-4e8a-b5d6-0f2e7c9a1b34"
    },
    "currency": "USD",
    "taxCode": "C003-00-1",
    "storefront": "USA",
    "items": [
        {
            "SKU": "GROUP_PRO_1M",
            "displayName": "Group Pro",
            "description": "Shared access for your group",
            "period": "P1M",
            "seatPriceTiers": [
                { "maximumSeatQuantity": 5, "price": 9990 },
                { "maximumSeatQuantity": 5, "price": 7990 },
                { "price": 5990 }
            ],
            "finalQuantity": 8
        }
    ]
}
```

**Decoded signed transaction**:

```json
{
    "transactionId": "12345",
    "originalTransactionId": "12345",
    "webOrderLineItemId": "23456",
    "bundleId": "com.example",
    "productId": "com.example.base",
    "subscriptionGroupIdentifier": "34567",
    "purchaseDate": 1735718400000,
    "originalPurchaseDate": 1735718400000,
    "expiresDate": 1738396800000,
    "quantity": 8,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1735718400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 9240,
    "currency": "USD",
    "appTransactionId": "45678",
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 7990, "quantity": 3 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "price": 9240,
                "seatPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "9a4d7e2b-1c3f-4e8a-b5d6-0f2e7c9a1b34",
        "period": "P1M"
    }
}
```

## Add seats

To add seats in your app, send a [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) that meets these conditions:

- The request’s [`effective`](./effective.md) value is `IMMEDIATELY`.
- Its single [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md) identifies the item by its `currentSKU`, omits `SKU`, and re-declares the item’s current values, including its `seatPriceTiers` and `period`.
- The change item’s [`finalQuantity`](./finalquantity.md) contains the total number of seats after the addition, not the number of seats to add. For example, to add 4 seats to a group that has 8, provide `12`.

Make adding seats the only change in the request, and submit other changes, such as a new SKU or period, in a separate request.

The App Store charges a prorated amount for the added seats for the rest of the current period, and the subscription renews with the new number of seats on its existing renewal date. Adding seats creates an additional transaction for the added seats in the same period, and every transaction in the period reports an `additionalTransactionReason` of `SEAT_ADDITION`. Your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `INCREASE_QUANTITY`. For more information, see [Managing the life cycle of multiseat subscriptions](../StoreKit/managing-the-life-cycle-of-multiseat-subscriptions.md).

### Example: Add seats to a group subscription

In the following request and response:

- On January 16, the group purchaser adds 4 seats to a group subscription that has 8 seats and renews on February 1.
- The change item identifies the item by its `currentSKU`, omits `SKU`, and re-declares the item’s current `seatPriceTiers` and `period`. The `finalQuantity` is `12`.
- The decoded signed transaction is the additional transaction for the 4 added seats. Its `quantity` is `4`, and its `additionalTransactionReason` is `SEAT_ADDITION`. Its `multiSeatInfo.priceTiers` lists the full per-seat prices of the tiers the added seats fall in, 2 seats at the second tier’s price and 2 at the last tier’s price. The App Store prorates its `price` for the rest of the period, so it’s lower than those prices.
- The original transaction for the first 8 seats stays valid and also reports an `additionalTransactionReason` of `SEAT_ADDITION`. The example doesn’t show it.
- The decoded signed renewal information shows the 12 seats that renew on February 1, and the tiers that apply to them.
- The example doesn’t include optional fields in `requestInfo` or the tax fields in `advancedCommerceInfo`.

**Request**:

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "2",
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36"
    },
    "currency": "USD",
    "storefront": "USA",
    "effective": "IMMEDIATELY",
    "changeItems": [
        {
            "currentSKU": "GROUP_PRO_1M",
            "displayName": "Group Pro",
            "description": "Shared access for your group",
            "period": "P1M",
            "seatPriceTiers": [
                { "maximumSeatQuantity": 5, "price": 9990 },
                { "maximumSeatQuantity": 5, "price": 7990 },
                { "price": 5990 }
            ],
            "finalQuantity": 12,
            "transactionId": "12345",
            "taxCode": "C003-00-1"
        }
    ]
}
```

**Decoded signed transaction**:

```json
{
    "transactionId": "12346",
    "originalTransactionId": "12345",
    "bundleId": "com.example",
    "productId": "com.example.base",
    "subscriptionGroupIdentifier": "34567",
    "purchaseDate": 1737014400000,
    "originalPurchaseDate": 1735718400000,
    "expiresDate": 1738396800000,
    "quantity": 4,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1737014400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "additionalTransactionReason": "SEAT_ADDITION",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 3610,
    "currency": "USD",
    "appTransactionId": "45678",
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 7990, "quantity": 2 },
            { "price": 5990, "quantity": 2 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "price": 3610,
                "seatPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "period": "P1M"
    }
}
```

**Decoded signed renewal information**:

```json
{
    "originalTransactionId": "12345",
    "autoRenewProductId": "com.example.base",
    "productId": "com.example.base",
    "autoRenewStatus": 1,
    "signedDate": 1737014400000,
    "environment": "Production",
    "recentSubscriptionStartDate": 1735718400000,
    "renewalDate": 1738396800000,
    "currency": "USD",
    "renewalPrice": 8490,
    "renewalQuantity": 12,
    "multiSeatInfo": {
        "renewalPriceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 7990, "quantity": 5 },
            { "price": 5990, "quantity": 2 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "seatRenewalPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "consistencyToken": "1.12345.c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "period": "P1M"
    },
    "appTransactionId": "45678"
}
```

## Reduce seats

You can’t reduce the number of seats with a modify request; a `finalQuantity` lower than the current number of seats fails with [`SeatDecreaseNotAllowedError`](./seatdecreasenotallowederror.md). The group purchaser reduces the number of seats in their subscription settings, and the change takes effect at the next renewal date. Your server receives a `DID_CHANGE_RENEWAL_PREF` notification with a subtype of `DECREASE_QUANTITY`.

To revoke unclaimed seats and refund them, call the [`Revoke Subscription`](./revoke-subscription.md) endpoint with a [`revokeSeatQuantity`](./revokeseatquantity.md). You can revoke only unclaimed seats, which are seats that no member occupies, and the App Store revokes them from the least expensive tier first. The subscription’s transaction remains valid for its remaining seats, its automatic renewal status doesn’t change, and your server receives a `REFUND` notification with a subtype of `SEATS`. Omit `revokeSeatQuantity` to revoke the entire subscription, including claimed seats.

## Change the subscription or its price

To upgrade, downgrade, or crossgrade a group subscription, send a [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) with the new `SKU`, the complete `seatPriceTiers`, and a `finalQuantity` equal to the current number of seats. A multiseat subscription keeps its tiers; a change item can’t replace them with a `price`. Change the SKU and the number of seats in separate requests.

To change the price per seat, call the [`Change Subscription Price`](./change-subscription-price.md) endpoint with the complete set of new `seatPriceTiers` instead of a `price`. The new tiers replace the existing tiers at the next renewal. Whether the change is a price increase depends on the change to the total price of the group purchaser’s seats. For more information, see [Handling subscription price changes](./handling-subscription-price-changes.md).

## Handle refunds and members’ transactions

When you call the [`Request Transaction Refund`](./request-transaction-refund.md) endpoint for a multiseat subscription, you can’t combine a `CUSTOM` refund type with a revocation. Use a refund type of `FULL` or `PRORATED` instead.

With Apple-hosted invitations, each member receives a transaction with an [`inAppOwnershipType`](../AppStoreServerAPI/inappownershiptype.md) of `ASSIGNED`. A member’s transaction carries a `requestReferenceId` of all zeros rather than the reference of your request, so don’t use it to match members’ transactions to your requests. The [`Migrate a Subscription to Advanced Commerce API`](./migrate-subscription-to-advanced-commerce-api.md) endpoint doesn’t accept a member’s transaction.

To test multiseat purchases, use the sandbox environment. For more information, see [Testing multiseat subscriptions](../StoreKit/testing-multiseat-subscriptions.md).

## See Also

### Related Documentation
- [Supporting multiseat purchases in your app](../StoreKit/supporting-multiseat-purchases-in-your-app.md)
  Configure, merchandise, and sell subscriptions that people buy for a group or that organizations buy in volume, and grant access to every seat.
- [Managing the life cycle of multiseat subscriptions](../StoreKit/managing-the-life-cycle-of-multiseat-subscriptions.md)
  Handle added and removed seats, member changes, plan changes, cancellations, billing issues, refunds, and price changes for multiseat subscriptions.
- [Hosting group invitations in your app](../StoreKit/hosting-group-invitations-in-your-app.md)
  Run your own invitation flow for group subscriptions, and keep the App Store informed of which seats your members hold.
### Generic product IDs and SKUs
- [Setting up generic product identifiers](./setting-up-generic-product-identifiers.md)
  Configure the generic product IDs in App Store Connect that the Advanced Commerce API requires.
- [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md)
  Define and manage one-time charges, subscriptions, and bundled subscriptions within your app.
- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)
  Define display names and SKUs for one-time charges and subscriptions in the Mini Apps Partner Program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/creating-multiseat-purchases)*