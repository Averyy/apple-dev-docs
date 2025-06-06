# appAccountToken

**Framework**: App Store Server Notifications  
**Kind**: typealias

A UUID that associates the transaction with a customer on your service.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```swift
uuid appAccountToken
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

When a customer initiates an in-app purchase, your app may create an [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) and send it to the App Store. The App Store returns the same value in [`appAccountToken`](appaccounttoken.md) in the transaction information after the customer completes the purchase.

If you’re using the [`Original API for In-App Purchase`](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase) and provide a UUID in the [`applicationUsername`](https://developer.apple.com/documentation/StoreKit/SKMutablePayment/applicationUsername) property, then the [`appAccountToken`](appaccounttoken.md) field contains that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/appaccounttoken)*