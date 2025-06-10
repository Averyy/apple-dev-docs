# ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)

**Framework**: StoreKit  
**Kind**: case

Describes when people chose to continue to view external purchases, and provides the external purchase token.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case continuedWithExternalPurchaseToken(token: String)
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)

#### Discussion

When your app calls [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) and it results in this value: [`ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)`](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md), your app can proceed to present external purchases.

> ❗ **Important**:  Record and use the token to report the customer’s external purchases to Apple. For more information, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

``

## Parameters

- `token`: The external purchase token.

## See Also

- [ExternalPurchase.NoticeResult.cancelled](externalpurchase/noticeresult/cancelled.md)
  Describes when people chose to cancel and not view external purchases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:))*