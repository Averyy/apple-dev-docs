# ExternalPurchase.NoticeResult.cancelled

**Framework**: StoreKit  
**Kind**: case

Describes when people chose to cancel and not view external purchases.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case cancelled
```

#### Discussion

If your app’s call to [`presentNoticeSheet()`](externalpurchase/presentnoticesheet().md) results in this value, you must not show external purchases.

## See Also

- [ExternalPurchase.NoticeResult.continuedWithExternalPurchaseToken(token:)](externalpurchase/noticeresult/continuedwithexternalpurchasetoken(token:).md)
  Describes when people chose to continue to view external purchases, and provides the external purchase token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchase/noticeresult/cancelled)*