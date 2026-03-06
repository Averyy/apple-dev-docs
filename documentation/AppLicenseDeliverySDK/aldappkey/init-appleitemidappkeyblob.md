# init(appleItemID:appKeyBlob:)

**Framework**: App License Delivery SDK  
**Kind**: init

Creates an app key to decrypt a license request.

## Declaration

```swift
init(appleItemID: UInt64, appKeyBlob: [UInt8]) throws
```

## Parameters

- `appleItemID`: A unique identifier for the app. See [`AppleItemID`](https://developer.apple.com/documentation/MarketplaceKit/AppleItemID).
- `appKeyBlob`: A *key blob* for a specific app variant that App Store Connect provides your marketplace server during app ingestion. For more information, see [`Ingesting an alternative distribution package`](https://developer.apple.com/documentation/appdistribution/ingesting-an-alternative-distribution-package).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldappkey/init(appleitemid:appkeyblob:))*