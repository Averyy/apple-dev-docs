# storeType

**Framework**: App Store Server API  
**Kind**: typealias

A string that describes the store the customer obtained the app from.

**Availability**:
- App Store Server API 1.22+

## Declaration

```swift
string storeType
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This field appears in the [`JWSAppTransactionDecodedPayload`](jwsapptransactiondecodedpayload.md). The only possible value is `CONSUMER`.

For the full set of values, see [`AppTransaction.StoreType`](https://developer.apple.com/documentation/storekit/apptransaction/storetype-swift.struct) in StoreKit.

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type originalApplicationVersion](originalapplicationversion.md)
  The app version that the customer originally purchased from the App Store.
- [type originalPlatform](originalplatform.md)
  The platform on which a customer originally purchases an app.
- [type preorderDate](preorderdate.md)
  The date a customer places an order for the app before it’s available in the App Store, expressed in UNIX time, in milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/storetype)*