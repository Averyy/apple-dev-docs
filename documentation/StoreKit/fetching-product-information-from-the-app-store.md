# Fetching product information from the App Store

**Framework**: StoreKit

Retrieve up-to-date information about the products for sale in your app to display to your customers.

#### Overview

To ensure your customers see only products that are available for them to purchase, query the App Store before displaying your app’s store UI. Compare the App Store’s list of product identifiers to your local product identifiers. To retrieve a list of your app’s product identifiers, see [`Loading in-app product identifiers`](loading-in-app-product-identifiers.md).

##### Request Product Information

To query the App Store, create an [`SKProductsRequest`](skproductsrequest.md) and initialize it with a list of your product identifiers. Keep a strong reference to the request object; otherwise, the system might deallocate the request before it can complete.

The products request retrieves information about valid products, along with a list of invalid product identifiers, and then calls its delegate to process the result. The delegate needs to implement the [`SKProductsRequestDelegate`](skproductsrequestdelegate.md) protocol to handle the response from the App Store. Here’s a simple implementation of both pieces of code:

Keep a reference to the array of [`SKProduct`](skproduct.md) objects that the delegate receives. Use these same product objects to create a payment request when a user purchases a product.

If the list of products you sell in your app is subject to change, such as when you add or remove a product from sale, consider creating a custom class that encapsulates a reference to the product object along with other information, such as pictures or descriptions that you fetch from your server. For more information on payment requests, see [`Requesting a payment from the App Store`](requesting-a-payment-from-the-app-store.md).

##### Troubleshoot Invalid Product Ids

Invalid product identifiers in the App Store response to your products request usually indicate an error in your app’s list of product identifiers. Invalid product identifiers may also indicate an incorrectly configured product in App Store Connect. Actionable UI and insightful logging can help you resolve this type of issue, as follows:

- In production builds, display your app’s store UI and omit the invalid product.
- In development builds, display an error to call attention to the issue.
- In both production and development builds, use [`NSLog(_:_:)`](https://developer.apple.com/documentation/Foundation/NSLog(_:_:)) to write a message to the console to record the invalid identifier.
- If your app fetches the list from your server, you can define a logging mechanism to let your app send the list of invalid identifiers back to your server.
- Verify that you have a signed Paid Applications Agreement for your developer account. For more information about this agreement, see [`Sign and update agreements`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/deva001f4a14).

For more information about troubleshooting invalid product identifiers, see [`invalidProductIdentifiers`](skproductsresponse/invalidproductidentifiers.md).

## See Also

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md)
  Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [class SKProductsRequest](skproductsrequest.md)
  An object that can retrieve localized information from the App Store about a specified list of products.
- [class SKProductsResponse](skproductsresponse.md)
  An App Store response to a request for information about a list of products.
- [class SKProduct](skproduct.md)
  Information about a registered product in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/fetching-product-information-from-the-app-store)*