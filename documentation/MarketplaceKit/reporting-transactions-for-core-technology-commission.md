# Reporting transactions for the Core Technology Commission

**Framework**: MarketplaceKit  
**Role**: Article

Track any eligible purchases that you offer a person that relate to your app and report them to Apple using a token.

## Overview

When a person installs your app from your website or from an alternative app marketplace, track any eligible purchases that you offer to a person that relate to your app and report them to Apple. To report the potential purchases, request a token from MarketplaceKit and send it to Apple using the External Purchase Server API. For more information, see [`Send External Purchase Report`](../ExternalPurchaseServerAPI/send-external-purchase-report.md). Retrieve a token for each purchase that you offer and send the token to Apple even if a person doesn’t complete a transaction for the offered purchase.

> ❗ **Important**: To determine which purchase offerings require reporting, see [Reporting tokens and transactions to Apple](http://developer.apple.com/help/app-store-connect/making-payments-to-apple/reporting-tokens-and-transactions) in App Store Connect Help.

To receive reminders to report your tokens and transactions, sign up for App Store Server notifications. The App Store’s commerce server periodically sends the endpoint that you configure in App Store Connect information regarding the tokens you generate. Compare the information with your own records, and if you fail to report a token, you can catch it and fix the issue. Notifications also help during development by validating your token-transmission code in the sandbox environment.

## Add the required target property

As a one-time setup task, add the [`MKSellsDigitalGoods`](../BundleResources/information-property-list/mksellsdigitalgoods.md) property to your app’s target configuration in Xcode. Assign the property a value of `YES` to indicate that your app offers the purchase of digital goods or services. If your app doesn’t sell digital goods or services, you still need to add the [`MKSellsDigitalGoods`](../BundleResources/information-property-list/mksellsdigitalgoods.md) property to your app’s target configuration with a value of `NO`.

## Request a Core Technology token

For the potential transactions that are eligible for reporting, request a token from MarketplaceKit using the [`TransactionReporting`](./transactionreporting.md) enumerations’s [`token(for:)`](./transactionreporting/token%28for%29.md) method, passing in a token of type [`coreTechnology`](./transactionreporting/tokentype/coretechnology.md). For example:

```swift
import MarketplaceKit
do {
    // Retrieve a token for a possible purchase.
    let token = try TransactionReporting.token(for: .coreTechnology)    
} catch let error as MarketplaceKitError {
    print("MarketplaceKit error: \(error.localizedDescription)")
    // Handle based on error.errorDescription or error type.    
} catch { print("Unexpected error: \(error)") }
```

An example token follows, which is a Base64URL-encoded string:

```
eyAgCiAgImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsICAKICAiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsICAKICAidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCiAgImV4dGVybmFsUHVyY2hhc2VJZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsCiAgInRva2VuVHlwZSI6IkNPUkVfVEVDSE5PTE9HWSIKfQ==
```

Decode the token using Base64URL decoding to reveal the token’s JSON data. A decoded token follows:

```json
{  
  "appAppleId":1234567890,  
  "bundleId":"com.example",  
  "tokenCreationDate":1706169600000,
  "externalPurchaseId":"00000000-0000-0000-0000-000000000000",
  "tokenType":"CORE_TECHNOLOGY"
}
```

For more information on decoding tokens, see [Receiving and decoding external purchase tokens](../StoreKit/receiving-and-decoding-external-purchase-tokens.md).

## Report tokens and their transactions

In the decoded JSON, use the [`externalPurchaseId`](../ExternalPurchaseServerAPI/externalpurchaseid.md) value to report the token to Apple. Report the token by using the [`Send External Purchase Report`](../ExternalPurchaseServerAPI/send-external-purchase-report.md) endpoint of the [External Purchase Server API](../ExternalPurchaseServerAPI/ExternalPurchaseServerAPI.md).

Report each token you retrieve regardless of whether the token corresponds to a completed transaction. The endpoint allows you to specify which tokens result in a transaction. You can also send the same token with updated information. For example, when a transaction completes after you initially report a token you can update the token with the transaction information. For more information, see [Reporting tokens with transactions](../ExternalPurchaseServerAPI/reportwithtransactions.md).

## Receive notifications

To receive reminders to report your tokens and transactions, sign up for [App Store Server Notifications](../AppStoreServerNotifications/AppStoreServerNotifications.md). Implement an endpoint on your webserver ([`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md)), to receive notifications of type `EXTERNAL_PURCHASE_TOKEN` for each token that you generate. For more information, see [`notificationType`](../AppStoreServerNotifications/notificationtype.md).

In production, you can send a token again; for example, if Apple fails to receive a particular token you identify in your records as sent. Notifications in the sandbox environment are also helpful during development. For more information, see “Receive notifications for unreported tokens” in [External Purchase Server API](../ExternalPurchaseServerAPI/ExternalPurchaseServerAPI.md).

## See Also

### Token and transaction reporting
- [enum TransactionReporting](./transactionreporting.md)
  An enumeration that provides token services for transaction reporting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/reporting-transactions-for-core-technology-commission)*