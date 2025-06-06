# Sending Advanced Commerce API requests from your app

**Framework**: StoreKit

Send Advanced Commerce API requests from your app that you authorize with a JSON Web Signature (JWS) you generate on your server.

#### Overview

You can make certain [`Advanced Commerce API`](https://developer.apple.com/documentation/AdvancedCommerceAPI) requests through StoreKit in your app, while you make other requests directly from your server.  In both cases, you authorize the calls with signatures you generate on your server.

The following Advanced Commerce API requests are available in your app using StoreKit APIs:

- [`OneTimeChargeCreateRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest)
- [`SubscriptionCreateRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/SubscriptionCreateRequest)
- [`SubscriptionModifyInAppRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/SubscriptionModifyInAppRequest)
- [`SubscriptionReactivateInAppRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/SubscriptionReactivateInAppRequest)

To make Advanced Commerce requests from your app, follow these steps:

1. Collect the request data according to the API you’re invoking.  On your server, create your  by combining the request data into a UTF-8 JSON string and base64-encoding the string.
2. On your server, create a JWS compact serialization that includes your base64-encoded request data in the JWS payload, as described in [`Include custom claims for Advanced Commerce API in-app requests`](generating-jws-to-sign-app-store-requests#Include-custom-claims-for-Advanced-Commerce-API-in-app-requests.md). For more information, see [`Generating JWS to sign App Store requests`](generating-jws-to-sign-app-store-requests.md).
3. Wrap the JWS in a JSON object, and convert it into a `Data` buffer to create the Advanced Commerce request data object, `advancedCommerceRequestData`.
4. In your app, use the `advancedCommerceRequestData` as the value of a purchase option in your product purchase call.

For more information on authorizing server-based calls, see [`Authorizing API requests from your server`](https://developer.apple.com/documentation/AdvancedCommerceAPI/authorizing-server-calls).

#### Create the Base64 Encoded Request Data

Place the Advanced Commerce request data in a UTF-8 JSON string and base64-encode the request.

For example, the following JSON represents a [`OneTimeChargeCreateRequest`](https://developer.apple.com/documentation/AdvancedCommerceAPI/OneTimeChargeCreateRequest) for the purchase of a one-time charge product:

```JSON
{
    "operation": "CREATE_ONE_TIME_CHARGE",
    "version": "1",                     
    "requestInfo": {
        "requestReferenceId": "f55df048-4cd8-4261-b404-b6f813ff70e5"
    },
    "currency": "USD",
    "taxCode": "C003-00-2", 
    "storefront": "USA",
    "item": {
        "SKU": "BOOK_SHERLOCK_HOMLES",
        "displayName": "Sherlock Holmes", 
        "description": "The Sherlock Holmes, 5th Edition",
        "price": 4990
    }
}
```

The result of base64-encoding the example JSON request is:

`ewogICAgIm9wZXJhdGlvbiI6ICJDUkVBVEVfT05FX1RJTUVfQ0hBUkdFIiwKICAgICJ2ZXJzaW9uIjogIjEiLCAgICAgICAgICAgICAgICAgICAgIAogICAgInJlcXVlc3RJbmZvIjogewogICAgICAgICJyZXF1ZXN0UmVmZXJlbmNlSWQiOiAiZjU1ZGYwNDgtNGNkOC00MjYxLWI0MDQtYjZmODEzZmY3MGU1IgogICAgfSwKICAgICJjdXJyZW5jeSI6ICJVU0QiLAogICAgInRheENvZGUiOiAiQzAwMy0wMC0yIiwgCiAgICAic3RvcmVmcm9udCI6ICJVU0EiLAogICAgIml0ZW0iOiB7CiAgICAgICAgIlNLVSI6ICJCT09LX1NIRVJMT0NLX0hPTUxFUyIsCiAgICAgICAgImRpc3BsYXlOYW1lIjogIlNoZXJsb2NrIEhvbG1lcyIsIAogICAgICAgICJkZXNjcmlwdGlvbiI6ICJUaGUgU2hlcmxvY2sgSG9sbWVzLCA1dGggRWRpdGlvbiIsCiAgICAgICAgInByaWNlIjogNDk5MAogICAgfQp9 `

This value, calculated using your own data, is your .

#### Generate the Jws Using Your Request Data

Follow the signing instructions for Advanced Commerce API in-app requests in [`Generating JWS to sign App Store requests`](generating-jws-to-sign-app-store-requests.md). The Advanced Commerce API requires a custom claim, `request`. Provide the base64-encoded request data from the previous step as the value of the `request` claim in the JWS payload.

The result after following the instructions is a .

#### Wrap the Jws and Convert It Into Data

Wrap the JWS to create a `signatureInfo` JSON string that contains a `token` key.  You can complete this step on your server or in your app. Create the `signatureInfo` JSON string as shown below:

```JSON
{
    "signatureInfo": {
        "token": "<your JWS compact serialization>"
    }
}
```

Set the value of the `token` key to your JWS compact serialization.

Next, convert the `signatureInfo` JSON string into a `Data` buffer, as shown below:

```swift
let jsonString ="<# your signatureInfo UTF-8 JSON string>"
let advancedCommerceRequestData = Data(jsonString.utf8)
```

The result is the Advanced Commerce request data object, referred to as `advancedCommerceRequestData` in the code snippets.

Securely send the `advancedCommerceRequestData` to your app.

#### Call the Storekit Purchase Api Using the Signed Request Data

To complete the Advanced Commerce request in the app, call a StoreKit purchase method and provide the signed request, in the Advanced Commerce request data form, as a purchase option.

The following code example sets up the purchase request:

```swift
let purchaseResult = try await product.purchase(
    options: [ 
        Product.PurchaseOption.custom( 
            key: “advancedCommerceData”, 
            value: advancedCommerceRequestData
        )
    ]
)
```

In this example:

- Use the custom key `"advancedCommerceData"` for all Advanced Commerce in-app requests. For more information about the custom purchase option, see [`custom(key:value:)`](product/purchaseoption/custom(key:value:)-80cvh.md).
- For the value attribute, provide your Advanced Commerce request data, which you created using your JWS compact serialization
- For more information about the product purchase method, see [`purchase(options:)`](product/purchase(options:).md).

## See Also

- [struct AdvancedCommerceProduct](advancedcommerceproduct.md)
  A product configured as a generic SKU in App Store Connect for use with the Advanced Commerce API.
- [Generating JWS to sign App Store requests](generating-jws-to-sign-app-store-requests.md)
  Create signed JSON Web Signature (JWS) strings on your server to authorize your API requests in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/sending-advanced-commerce-api-requests-from-your-app)*