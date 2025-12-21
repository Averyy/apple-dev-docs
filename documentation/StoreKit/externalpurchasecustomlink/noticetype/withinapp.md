# ExternalPurchaseCustomLink.NoticeType.withinApp

**Framework**: StoreKit  
**Kind**: case

A notice type that indicates that you display the destination in a web view or native experience within the app.

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

After displaying a notice with this notice type using [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md), if the customer chooses to continue, the app displays the destination in a web view or native experience within the app.

## See Also

- [ExternalPurchaseCustomLink.NoticeType.browser](externalpurchasecustomlink/noticetype/browser.md)
  A notice type that indicates your app displays external purchases in a destination of your choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype/withinapp)*