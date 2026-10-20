# applicationUsername

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that associates the transaction with a user account on your service.

**Availability**:
- iOS 7.0+ - Deprecated in 18.0
- iPadOS 7.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.9+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.appAccountToken to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
var applicationUsername: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * applicationUsername;
```

## Mentions

- [Implementing promotional offers in your app](../implementing-promotional-offers-in-your-app.md)
- [Generating a signature for promotional offers](../generating-a-signature-for-promotional-offers.md)
- [Restoring purchased products](../restoring-purchased-products.md)

#### Discussion

Consider assigning a UUID to the [`applicationUsername`](./applicationusername.md) property. When this value is a UUID, the App Store server stores it as an [`appAccountToken`](../transaction/appaccounttoken.md). In this scenario, the following happens:

- In the [App Store Server API](../../AppStoreServerAPI/AppStoreServerAPI.md), the [`JWSTransactionDecodedPayload`](../../AppStoreServerAPI/jwstransactiondecodedpayload.md) object returns the [`applicationUsername`](./applicationusername.md) value in the [`appAccountToken`](../../AppStoreServerAPI/appaccounttoken.md) field.
- In [App Store Server Notifications](../../AppStoreServerNotifications/AppStoreServerNotifications.md), the [`JWSTransactionDecodedPayload`](../../AppStoreServerNotifications/jwstransactiondecodedpayload.md) object returns the [`applicationUsername`](./applicationusername.md) value in the [`appAccountToken`](../../AppStoreServerNotifications/appaccounttoken.md) field.
- When you call the [`verifyReceipt`](../../AppStoreReceipts/verify-receipt.md) endpoint to verify an App Store receipt, the App Store server returns the [`applicationUsername`](./applicationusername.md) value in the [`app_account_token`](../../AppStoreReceipts/app_account_token.md) field of the [`responseBody.Latest_receipt_info`](../../AppStoreReceipts/responsebody/latest_receipt_info-data.dictionary.md).

The sample code below shows how to assign a UUID value to [`applicationUsername`](./applicationusername.md). You may choose to generate the UUID on your server. Assign the value before adding the payment to the payment queue.

**Swift**:

```swift
let payment = SKMutablePayment(product: product)
payment.applicationUsername = uuidString

SKPaymentQueue.default().add(payment)
```

**Objective-C**:

```objc
SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:product];
payment.applicationUsername = uuidString;

[[SKPaymentQueue defaultQueue] addPayment:payment];
```

If you don’t assign a UUID string value to [`applicationUsername`](./applicationusername.md), the App Store server doesn’t persist the value. The value won’t appear in the [`app_account_token`](../../AppStoreReceipts/app_account_token.md) fields in notifications or receipts.

> ❗ **Important**:  An [`applicationUsername`](./applicationusername.md) property that isn’t a UUID isn’t guaranteed to persist between the time when you add the payment transaction to the queue and when the queue updates the transaction.

## See Also

### Getting and Setting Attributes
- [var productIdentifier: String](./productidentifier.md)
  A string that identifies a product that can be purchased from within your app.
- [var quantity: Int](./quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](./requestdata.md)
  Reserved for future use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment/applicationusername)*