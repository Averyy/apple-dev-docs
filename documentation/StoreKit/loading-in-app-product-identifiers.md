# Loading in-app product identifiers

**Framework**: StoreKit

Load the unique identifiers for your in-app products to retrieve product information from the App Store.

#### Overview

Implementing an in-app purchase flow consists of three stages. In the first stage, your app retrieves product information. Then your app requests payment when the user selects a product in your app’s store. Finally, your app delivers the product.

![A flowchart depicting the three stages of the in-app purchase process between your app and the App Store. First, your app makes a request for a product, the App Store provides that product information, and your app displays it. Next, the user selects a product, your app makes a payment request, and the App Store processes the payment. Finally, the App Store calls your app’s transaction queue observer, and your app delivers the purchased product. The first stage, retrieving product information, is highlighted.](https://docs-assets.developer.apple.com/published/329972bcd64d9cb216994581435db29f/media-3317194%402x.png)

To begin the purchase process, your app needs the product identifiers so it can retrieve information about the products from the App Store and present its store UI to the user. Every product you sell in your app has a unique product identifier. You provide this value in App Store Connect when you create a new in-app purchase product (see [`Create in-app purchases`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devae49fb316) for more information). Your app uses these product identifiers to fetch information about products available for sale in the App Store, such as pricing, and to submit payment requests when users purchase those products.

There are several strategies for storing a list of product identifiers in your app, such as embedding them in the app bundle or storing them on your server. You can then retrieve the product identifiers by reading them locally in the app bundle or fetching them from your server. Choose the method that best serves your app’s needs.

> **Note**:  There’s no runtime mechanism to fetch a list of the configured products in App Store Connect for a particular app. You’re responsible for managing your app’s list of products and providing that information to your app.

 There’s no runtime mechanism to fetch a list of the configured products in App Store Connect for a particular app. You’re responsible for managing your app’s list of products and providing that information to your app.

##### Retrieve Product Ids From the App Bundle

Embed the product identifiers in your app bundle if:

- Your app has a fixed list of in-app purchase products. For example, apps with an in-app purchase to remove ads or unlock functionality can embed the product identifier list in the app bundle.
- You expect users to update the app to see new in-app purchase products.
- The app or product doesn’t require a server.

Include a property list file in your app bundle containing an array of product identifiers, such as the following:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <string>com.example.level1</string>
    <string>com.example.level2</string>
    <string>com.example.rocket_car</string>
</array>
</plist>
```

To get product identifiers from the property list, locate the file in the app bundle and read it.

##### Retrieve Product Ids From Your Server

Store the product identifiers on your server if:

- You update the list of in-app products frequently, without updating your app. For example, games that support additional levels or characters can fetch the product identifiers list from your server.
- The products consist of delivered content.
- Your app or product requires a server.

Host a JSON file on your server with the product identifiers. For example, the following JSON file contains three product IDs:

```xml
[
    "com.example.level1",
    "com.example.level2",
    "com.example.rocket_car"
]
```

To get product identifiers from your server, fetch and read the JSON file.

Consider versioning the JSON file so future versions of your app can change its structure without breaking older versions of your app. For example, you might name the file that uses the old structure `products_v1.json` and the file that uses a new structure `products_v2.json`. This is especially useful if your JSON file is more complex than the simple array in the example.

To ensure that your app remains responsive, use a background thread to download the JSON file and extract the list of product identifiers. To minimize the data that transfers, use standard HTTP caching mechanisms, such as the `Last-Modified` and `If-Modified-Since` headers.

After loading all in-app product identifiers, pass them into the product information request to the App Store. For details on obtaining product information, see [`Fetching product information from the App Store`](fetching-product-information-from-the-app-store.md).

## See Also

- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md)
  Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [class SKProductsRequest](skproductsrequest.md)
  An object that can retrieve localized information from the App Store about a specified list of products.
- [class SKProductsResponse](skproductsresponse.md)
  An App Store response to a request for information about a list of products.
- [class SKProduct](skproduct.md)
  Information about a registered product in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/loading-in-app-product-identifiers)*