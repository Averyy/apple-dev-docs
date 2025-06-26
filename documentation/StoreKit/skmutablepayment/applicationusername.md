# applicationUsername

**Framework**: StoreKit  
**Kind**: property

A string that associates the transaction with a user account on your service.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var applicationUsername: String? { get set }
```

## Mentions

- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md)
- [Restoring purchased products](restoring-purchased-products.md)
- [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md)

#### Discussion

Consider assigning a UUID to the [`applicationUsername`](skmutablepayment/applicationusername.md) property. When this value is a UUID, the App Store server stores it as an [`appAccountToken`](transaction/appaccounttoken.md). In this scenario, the following happens:

- In the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI), the [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) object returns the [`applicationUsername`](skmutablepayment/applicationusername.md) value in the [`appAccountToken`](https://developer.apple.com/documentation/AppStoreServerAPI/appAccountToken) field.
- In [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications), the [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerNotifications/JWSTransactionDecodedPayload) object returns the [`applicationUsername`](skmutablepayment/applicationusername.md) value in the [`appAccountToken`](https://developer.apple.com/documentation/AppStoreServerNotifications/appAccountToken) field.
- When you call the [`verifyReceipt`](https://developer.apple.com/documentation/appstorereceipts/verifyreceipt) endpoint to verify an App Store receipt, the App Store server returns the [`applicationUsername`](skmutablepayment/applicationusername.md) value in the [`app_account_token`](https://developer.apple.com/documentation/appstorereceipts/app_account_token) field of the [`responseBody.Latest_receipt_info`](https://developer.apple.com/documentation/appstorereceipts/responsebody/latest_receipt_info).

The sample code below shows how to assign a UUID value to [`applicationUsername`](skmutablepayment/applicationusername.md). You may choose to generate the UUID on your server. Assign the value before adding the payment to the payment queue.

If you don’t assign a UUID string value to [`applicationUsername`](skmutablepayment/applicationusername.md), the App Store server doesn’t persist the value. The value won’t appear in the [`app_account_token`](https://developer.apple.com/documentation/appstorereceipts/app_account_token) fields in notifications or receipts.

> ❗ **Important**:  An [`applicationUsername`](skmutablepayment/applicationusername.md) property that isn’t a UUID isn’t guaranteed to persist between the time when you add the payment transaction to the queue and when the queue updates the transaction.

## See Also

- [var productIdentifier: String](skmutablepayment/productidentifier.md)
  A string that identifies a product that can be purchased from within your app.
- [var quantity: Int](skmutablepayment/quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](skmutablepayment/requestdata.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment/applicationusername)*