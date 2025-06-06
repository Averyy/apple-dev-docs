# Testing promoted In-App Purchases

**Framework**: StoreKit

Test your In-App Purchases before making your app available in the App Store.

#### Overview

Users can buy promoted In-App Purchases from the App Store, but you need to test this flow before making your product publicly available. Apple provides a system URL that triggers your app using the `itms-services://` protocol, so you can test In-App Purchases before they’re available in the App Store.

|  | `itms-services://` |
| --- | --- |
| `action` | `purchaseIntent` |
| `bundleId` | The bundle ID for your app; for example: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `com.example.app` |
| `productIdentifier` | The In-App Purchase product ID you want to test; for example: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `com.example.product` |

The resulting URL looks like this:

`itms-services://?action=purchaseIntent&bundleId=com.example.app&productIdentifier=com.example.product`

Send this URL to yourself in an email or iMessage, and open it from your device. You’ll know the test is running when your app opens automatically. You can then test how your app handles the promoted In-App Purchase.

## See Also

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
  Display promoted In-App Purchases on your product page and handle purchases that users initiate on the App Store.
- [struct PurchaseIntent](purchaseintent.md)
  An instance that emits purchase intents, which indicate that the customer initiated a purchase outside of your app, for your app to complete.
- [Product.PromotionInfo](product/promotioninfo.md)
  Information about a promoted In-App Purchase that customizes its order and visibility on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/testing-promoted-in-app-purchases)*