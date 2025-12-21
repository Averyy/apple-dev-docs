# Receiving and decoding external purchase tokens

**Framework**: StoreKit

Receive tokens for external purchases that you use to report transactions to Apple.

#### Overview

An  is a unique string that your app or website receives when your customer chooses to view your external purchase offerings. You receive external purchase tokens within your app or appended to your website URL, depending on the API you call.

- When you call [`token(for:)`](externalpurchasecustomlink/token(for:).md) and your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key, you receive an external purchase token for custom links (also called a ) . For more information about these tokens, see the following section, [`Receive custom link tokens`](receiving-and-decoding-external-purchase-tokens#Receive-custom-link-tokens.md).
- When you call [`token(for:)`](externalpurchasecustomlink/token(for:).md), and your app configures the [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions) property list key, you receive custom link tokens for a music streaming service.
- When you call [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) and the response is [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md), you receive an external purchase token in your app.
- When you call [`open()`](externalpurchaselink/open().md) or [`open(url:)`](externalpurchaselink/open(url:).md), you receive an external purchase token appended to the current storefront’s destination URL. You configure the URLs in the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) or [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list keys, respectively.

In all cases, decode the token to obtain its [`externalPurchaseId`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/externalPurchaseId). Use the `externalPurchaseId` to report the token and its associated transactions to Apple using the [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint of the [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

The External Purchase API returns tokens that are specific to the app’s environment, either production or sandbox. Tokens in the sandbox environment have an `externalPurchaseId` value that begins with `SANDBOX`.

##### Receive Custom Link Tokens

The system automatically generates custom link tokens for your customer if your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) or [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLinkStreamingRegions) property list keys. Your app calls the [`token(for:)`](externalpurchasecustomlink/token(for:).md) method to receive the tokens. These tokens have two possible token types: `ACQUISITION` and `SERVICES`.

The system automatically generates new custom link tokens when the following qualifying events occur:

| Qualifying event | Custom link tokens |
| --- | --- |
| Customer installs an app for the first time across all of their devices | The system generates both the `ACQUISITION` and `SERVICES` tokens. |
| Customer updates or redownloads an app on any of their devices | If there’s no active `SERVICES` token, the system generates a new `SERVICES` token. |

Custom link tokens have expiration dates. A token is considered  during the time between its creation date and expiration date.

Apps can request custom link tokens at any time, for example, when the app launches, or before displaying a store. If there’s an active token period, the system returns the token that corresponds to that active period. The returned token can be identical to the original token, or it can be a  token. A refreshed token has the same creation and expiration dates as the original token, but a different [`externalPurchaseId`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/externalPurchaseId).

Use either the original token or a refreshed token to report transactions that occur during the active token period.

> **Note**: To report transactions for custom link tokens, you can use any token associated with the customer that is active (not expired) at the time of the transaction.

After a customer’s `ACQUISITION` token expires, the system doesn’t generate another. The `ACQUISITION` token type has only one active token period. After a customer’s `SERVICES` token expires, the system generates a new `SERVICES` token only if a qualifying event occurs, as listed in the table above.

Custom link tokens are available only on devices running iOS 18.1 and later, iPadOS 18.1 and later, macOS 15.1 and later, tvOS 18.1 and later, visionOS 2.1 and later, and watchOS 11.1 and later.

##### Decode External Purchase Tokens

The token your app or website’s server receives is a string that is Base64URL-encoded JSON. Decode the token using Base64URL decoding to read the JSON, which contains the following fields:

The following additional fields apply only to custom link tokens:

The [`Send External Purchase Report`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) endpoint requires the [`externalPurchaseId`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/externalPurchaseId) field to report tokens and transactions. To get the `externalPurchaseId`, decode the token string using Base64URL decoding.

The following example shows an external purchase token. For a token string that is:

```None
ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9
```

The token’s value after Base64URL decoding is the following JSON:

```json
{  
  "appAppleId":1234567890,  
  "bundleId":"com.example",  
  "tokenCreationDate":1706169600000,
  "externalPurchaseId":"00000000-0000-0000-0000-000000000000"
}
```

The following example shows a custom link token with a `SERVICES` token type. The token string is:

```None
eyJhcHBBcHBsZUlkIjoxMjM0NTY3ODkwLCJidW5kbGVJZCI6ImNvbS5leGFtcGxlIiwidG9rZW5DcmVhdGlvbkRhdGUiOjE3NTA4OTYwMDAwMDAsImV4dGVybmFsUHVyY2hhc2VJZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsInRva2VuVHlwZSI6IlNFUlZJQ0VTIiwidG9rZW5FeHBpcmF0aW9uRGF0ZSI6MTc4MjQzMjAwMDAwMH0K
```

The custom link token’s value after Base64URL decoding is the following JSON:

```json
{
  "appAppleId": 1234567890,
  "bundleId": "com.example",
  "tokenCreationDate": 1750896000000,
  "externalPurchaseId": "00000000-0000-0000-0000-000000000000",
  "tokenType": "SERVICES", // Present only in custom link tokens
  "tokenExpirationDate": 1782432000000 // Present only in custom link tokens
}
```

##### Recognize Tokens From the Testing Environment

The [`External Purchase`](external-purchase.md) API returns external purchase tokens that are specific to the app’s environment: production or sandbox. You can recognize a token for the sandbox environment by its `externalPurchaseId` property, which always begins with `SANDBOX`.

The following example is an external purchase token that the system created in the sandbox environment. The sandbox token string is:

```None
eyJhcHBBcHBsZUlkIjoxMjM0NTY3ODkwLCJidW5kbGVJZCI6ImNvbS5leGFtcGxlIiwidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsImV4dGVybmFsUHVyY2hhc2VJZCI6IlNBTkRCT1hfMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwidG9rZW5UeXBlIjoiU0VSVklDRVMiLCJ0b2tlbkV4cGlyYXRpb25EYXRlIjoxNzA2MTczMjAwMDAwfQo=
```

The token’s JSON content after Base64URL decoding is:

```json
{
    "appAppleId":1234567890,
    "bundleId":"com.example",
    "tokenCreationDate":1706169600000,
    "externalPurchaseId":"SANDBOX_00000000-0000-0000-0000-000000000000"
}
```

The following example is a custom link token with a `SERVICES` token type, that the system created in the sandbox environment. The sandbox token string is:

```None
eyJhcHBBcHBsZUlkIjoxMjM0NTY3ODkwLCJidW5kbGVJZCI6ImNvbS5leGFtcGxlIiwidG9rZW5DcmVhdGlvbkRhdGUiOjE3MzA0NDg3MjAwMDAsImV4dGVybmFsUHVyY2hhc2VJZCI6IlNBTkRCT1hfMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIiwidG9rZW5UeXBlIjoiU0VSVklDRVMiLCJ0b2tlbkV4cGlyYXRpb25EYXRlIjoxNzMwNDUyMzIwMDAwfQ==
```

The custom link token’s JSON content after Base64URL decoding is:

```json
{
  "appAppleId": 1234567890,
  "bundleId": "com.example",
  "tokenCreationDate": 1706169600000,
  "externalPurchaseId": "SANDBOX_00000000-0000-0000-0000-000000000000",
  "tokenType": "SERVICES", // Present only in custom link tokens
  "tokenExpirationDate": 1706173200000 // Present only in custom link tokens
}
```

Notice that the custom link token has both a creation date and an expiration date. In the sandbox environment, the expiration date is one hour after the creation date. An `ACQUISITION` token has the same format, with a `tokenType` value of `ACQUISITION`.

For more information about testing and receiving custom link tokens in the sandbox environment, see [`Testing transactions that use custom link tokens`](testing-transactions-that-use-custom-link-tokens.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/receiving-and-decoding-external-purchase-tokens)*