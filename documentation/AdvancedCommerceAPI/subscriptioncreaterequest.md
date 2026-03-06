# SubscriptionCreateRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The request data your app provides when a customer purchases an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object SubscriptionCreateRequest
```

## Mentions

- [Creating SKUs for your In-App Purchases](creating-your-purchases.md)
- [Creating SKUs for the Mini Apps Partner Program](creating-skus-for-the-mini-app-partner-program.md)

##### Example Subscription with a Single Item

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "1", 
    "requestInfo": {
        "requestReferenceId": "74ad2401-488d-4e1a-9c9d-80cdf0efed67"
    },
    "currency": "USD", 
    "taxCode": "C003-00-1", 
    "descriptors": {
        "displayName": "Anne's Game Stream",
        "description": "Streaming Service for Anne's Game"
    },
    "period": "P1M",
    "storefront": "USA",
    "items": [ 
        {
            "SKU": "ANNES_GOLD_TIER_1M",
            "displayName": "Gold Tier",                        
            "description": "Access to Anne's Game Stream",
            "price": 7990
        }
    ]
}
```

##### Example Subscription with Multiple Items and an Offer

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "1", 
    "requestInfo": {
        "requestReferenceId": "74ad2401-488d-4e1a-9c9d-80cdf0efed67"
    },
    "currency": "USD", 
    "taxCode": "C003-00-1", 
    "descriptors": {
        "displayName": "Streaming Pass",
        "description": "Streaming pass with multiple items"
    },
    "period": "P1M",
    "storefront": "USA",
    "items": [ 
        {
            "SKU": "LIVE_SPORTS",
            "displayName": "Live Sports",                        
            "description": "Streaming for sports events",
            "price": 40000
        },
        {
            "SKU": "SATURDAY_MORNING_CARTOONS",
            "displayName": "Saturday Morning Cartoons",
            "description": "Streaming for animated series",
            "price": 11000,
            "offer": {
                "price": 2990, 
                "period": "P1M",
                "periodCount": 3,
                "reason": "ACQUISITION"
            }
        }
    ]
}
```

## Properties

- `currency` (currency) *(required)*
- `descriptors` (Descriptors) *(required)*
- `items` ([SubscriptionCreateItem]) *(required)*
- `operation` (string) *(required)*
- `period` (period) *(required)*
- `previousTransactionId` (transactionId)
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode) *(required)*
- `version` (version) *(required)*

## See Also

- [object SubscriptionCreateItem](subscriptioncreateitem.md)
  The data that describes a subscription item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreaterequest)*