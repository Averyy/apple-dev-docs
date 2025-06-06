# environment

**Framework**: App Store Server API  
**Kind**: typealias

The server environment, either sandbox or production.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string environment
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

You receive data from the [`App Store Server API`](AppStoreServerAPI.md) for the sandbox environment when you send test requests to the endpoints using the sandbox base URL:

```javascript
https://api.storekit-sandbox.itunes.apple.com/
```

## See Also

- [type appAppleId](appappleid.md)
  The unique identifier of an app in the App Store.
- [type bundleId](bundleid.md)
  The bundle identifier of an app.
- [type hasMore](hasmore.md)
  A Boolean value indicating whether the App Store has more transaction data.
- [type revision](revision.md)
  A token you use in a query to request the next set of transactions for the customer.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/environment)*