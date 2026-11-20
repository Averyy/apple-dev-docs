# BundleItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object BundleItem
```

## Overview

> **Note**: Only the sandbox environment supports bundleItems.

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `appAppleId` (int64)
- `appleProductId` (string)
- `description` (description) *(required)*: **Maximum Length**: `45`
- `displayName` (displayName) *(required)*: **Maximum Length**: `30`
- `previousTransactionId` (transactionId)
- `price` (price) *(required)*
- `taxCode` (taxCode)

## See Also

### Subscription creation in the app
- [object SubscriptionCreateRequest](./subscriptioncreaterequest.md)
  The request data your app provides when a customer purchases an auto-renewable subscription.
- [object SubscriptionCreateItem](./subscriptioncreateitem.md)
  The data that describes a subscription item.
- [object SubscriptionCreateRequestV1](./subscriptioncreaterequestv1.md)
- [object SubscriptionCreateItemV1](./subscriptioncreateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/bundleitem)*