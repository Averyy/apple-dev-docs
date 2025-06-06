# Requesting a payment from the App Store

**Framework**: StoreKit

Submit a payment request to the App Store when a customer selects a product to buy.

#### Overview

After you present your app’s store UI, users can make purchases from within your app. When the user chooses a product, your app creates and submits a payment request to the App Store.

Implementing an in-app purchase flow consists of three stages. In the first stage, your app retrieves product information. Then your app requests payment when the user selects a product in your app’s store. Finally, your app delivers the products.

![A flowchart depicting the three stages of the in-app purchase process between your app and the App Store. First, your app makes a request for a product, the App Store provides that product information, and your app displays it. Next, the user selects a product, your app makes a payment request, and the App Store processes the payment. Finally, the App Store calls your app’s transaction queue observer, and your app delivers the purchased product. The second stage, requesting payment, is highlighted.](https://docs-assets.developer.apple.com/published/ea0d3011f324be7c4824026f6efbf13b/media-3315895%402x.png)

##### Create a Payment Request

When the user selects a product to buy, create a payment request using the corresponding [`SKProduct`](skproduct.md) object and set the quantity if needed, as the code below shows. The product object comes from the array of products that your app’s products request returns, as described in [`Fetching product information from the App Store`](fetching-product-information-from-the-app-store.md).

##### Submit a Payment Request

Submit your payment request to the App Store by adding it to the payment queue. If you add a payment object to the queue more than once, the system submits it to the App Store multiple times, charging the user and requiring your app to deliver the product each time.

For each payment request your app submits, it receives a corresponding transaction to process. For more information about transactions and the payment queue, see [`Processing a transaction`](processing-a-transaction.md).

For auto-renewable subscriptions, you may submit a payment request with a subscription offer for users you determine eligible to receive an offer. For more information, see [`Implementing promotional offers in your app`](implementing-promotional-offers-in-your-app.md).

## See Also

- [Processing a transaction](processing-a-transaction.md)
  Register a transaction queue observer to get and handle transaction updates from the App Store.
- [class SKPayment](skpayment.md)
  A request to the App Store to process payment for additional functionality that your app offers.
- [class SKMutablePayment](skmutablepayment.md)
  A mutable request to the App Store to process payment for additional functionality that your app offers.
- [class SKPaymentTransaction](skpaymenttransaction.md)
  An object in the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/requesting-a-payment-from-the-app-store)*