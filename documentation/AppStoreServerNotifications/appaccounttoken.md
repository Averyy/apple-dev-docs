# appAccountToken

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

A UUID that associates the transaction with a customer on your service.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
uuid appAccountToken
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

#### Discussion

When a customer initiates an in-app purchase, your app may create an [`appAccountToken(_:)`](../StoreKit/product/purchaseoption/appaccounttoken%28_%29.md) and send it to the App Store. The App Store returns the same value in [`appAccountToken`](./appaccounttoken.md) in the transaction information after the customer completes the purchase.

If you’re using the [Original API for Apple In-App Purchase](../StoreKit/original-api-for-in-app-purchase.md) and provide a UUID in the [`applicationUsername`](../StoreKit/skmutablepayment/applicationusername.md) property, then the [`appAccountToken`](./appaccounttoken.md) field contains that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/appaccounttoken)*