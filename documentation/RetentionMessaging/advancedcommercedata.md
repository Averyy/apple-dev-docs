# advancedCommerceData

**Framework**: Retention Messaging API  
**Kind**: typealias

A Base64-encoded JSON object which contains a JWS with information describing an offer or switch-plan recommendation.

**Availability**:
- Retention Messaging 1.2+

## Declaration

```swift
string advancedCommerceData
```

#### Discussion

This property is a part of the [`advancedCommerceInfo`](advancedcommerceinfo.md). For more information on the Advanced Commerce API (ACA), see [`Advanced Commerce API`](https://developer.apple.com/documentation/AdvancedCommerceAPI).

See [`Sending Advanced Commerce API requests from your app`](https://developer.apple.com/documentation/StoreKit/sending-advanced-commerce-api-requests-from-your-app) for how to construct this object. Pass the Base64-encoded advancedCommerceRequestData object as a UTF-8 string as [`advancedCommerceData`](advancedcommercedata.md). Use [`SubscriptionModifyInAppRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest) with a single [`SubscriptionModifyChangeItem`](https://developer.apple.com/documentation/AdvancedCommerceAPI/SubscriptionModifyChangeItem) provided when constructing the advancedCommerceRequestData.

For more information on the structure of JWS objects, see [`Generating JWS to sign App Store requests`](https://developer.apple.com/documentation/StoreKit/generating-jws-to-sign-app-store-requests).


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/advancedcommercedata)*