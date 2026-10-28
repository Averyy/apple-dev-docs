# advancedCommerceData

**Framework**: Retention Messaging API  
**Kind**: typealias  
**Role**: Type

A Base64-encoded JSON object which contains a JWS with information describing an offer or switch-plan recommendation.

**Availability**:
- Retention Messaging API 1.2+

## Declaration

```
string advancedCommerceData
```

## Discussion

This property is a part of the [`advancedCommerceInfo`](./advancedcommerceinfo.md). For more information on the Advanced Commerce API (ACA), see [Advanced Commerce API](../AdvancedCommerceAPI/AdvancedCommerceAPI.md).

See [Sending Advanced Commerce API requests from your app](../StoreKit/sending-advanced-commerce-api-requests-from-your-app.md) for how to construct this object. Pass the Base64-encoded advancedCommerceRequestData object as a UTF-8 string as [`advancedCommerceData`](./advancedcommercedata.md). Use [`SubscriptionModifyInAppRequest`](../AdvancedCommerceAPI/subscriptionmodifyinapprequest.md) with a single [`SubscriptionModifyChangeItem`](../AdvancedCommerceAPI/subscriptionmodifychangeitem.md) provided when constructing the advancedCommerceRequestData.

For more information on the structure of JWS objects, see [Generating JWS to sign App Store requests](../StoreKit/generating-jws-to-sign-app-store-requests.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/advancedcommercedata)*