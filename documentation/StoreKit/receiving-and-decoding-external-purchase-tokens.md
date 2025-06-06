# Receiving and decoding external purchase tokens

**Framework**: StoreKit

Receive tokens for external purchases that you use to report transactions to Apple.

#### Overview

An  is a unique string that your app or website receives when your app’s customer chooses to view your external purchase offerings. You receive external purchase tokens in two ways: within your app, or appended to your website URL for link out, as follows:

- In your app, the API returns the token when your app calls [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) and the response is [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md).
- For link out, when your app calls [`open()`](externalpurchaselink/open().md) or [`open(url:)`](externalpurchaselink/open(url:).md), the API appends the token to the current storefront’s destination URL that you configure in the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) or [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list keys, respectively.
- For custom link out, when your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key and calls the [`token(for:)`](externalpurchasecustomlink/token(for:).md) function.

Decode the token to obtain its [`externalPurchaseId`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/externalPurchaseId), which you use to report the tokens and associated transactions to Apple using the [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint of the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Decode External Purchase Tokens

The token your app or website’s server receives is a string that is Base64URL-encoded JSON. Decode the token using Base64URL decoding to read the JSON, which contains the following fields:

- The `appAppleId` and `bundleId`, which uniquely identify the app to which the token applies
- The `tokenCreationDate`, which is the UNIX time, in milliseconds, when the system created the token
- The `externalPurchaseId`, which is a unique value the system created to identify the token

For custom link out, the token is represented by [`ExternalPurchaseCustomLink.Token`](externalpurchasecustomlink/token.md) and has two additional fields:

- A `tokenType`, which has a value of `ACQUISITION` or `SERVICES`
- A `tokenExpirationDate`, which is the UNIX time, in milliseconds, when the token expires, after which you no longer associate the token with new transactions

The `externalPurchaseId` field is required by the [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint when you report tokens and transactions. To get the `externalPurchaseId`, follow these steps:

- Decode the token string using Base64URL decoding. For example, if the token string is:

`ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9`

Then, the token’s value after Base64URL decoding is the following JSON:

```xml
{  
  "appAppleId":1234567890,  
  "bundleId":"com.example",  
  "tokenCreationDate":1706169600000,
  "externalPurchaseId":"00000000-0000-0000-0000-000000000000"
}
```

- Use the value of the `externalPurchaseId` property to identify the token when you call the [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint.

##### Recognize Tokens From the Testing Environment

The [`External Purchase`](external-purchase.md) API returns external purchase tokens that are specific to the app’s environment: production or sandbox. You can recognize a token for the sandbox environment by its `externalPurchaseId` property, which always begins with “`SANDBOX`”.

The following example is an external purchase token that the system created in the sandbox environment. The sandbox token string is:

`ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiU0FOREJPWF8wMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC0wMDAwMDAwMDAwMDAiCn0K`

The token’s JSON content after Base64URL decoding is:

```xml
{
    "appAppleId":1234567890,
    "bundleId":"com.example",
    "tokenCreationDate":1706169600000,
    "externalPurchaseId":"SANDBOX_00000000-0000-0000-0000-000000000000"
}
```

The `externalPurchaseId` includes the “`SANDBOX`” prefix in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/receiving-and-decoding-external-purchase-tokens)*