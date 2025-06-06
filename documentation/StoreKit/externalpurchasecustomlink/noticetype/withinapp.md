# ExternalPurchaseCustomLink.NoticeType.withinApp

**Framework**: StoreKit  
**Kind**: case

A notice type that indicates that you display the destination in a web view within the app.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
case withinApp
```

#### Discussion

After displaying a notice with this notice type using [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md), if the customer chooses to continue, the app displays the destination in a web view within the app.

## See Also

- [ExternalPurchaseCustomLink.NoticeType.browser](externalpurchasecustomlink/noticetype/browser.md)
  A notice type that indicates you display external purchases in a destination outside of the app, which can be an alternative marketplace, another app, or a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype/withinapp)*