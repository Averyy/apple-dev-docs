# ExternalPurchaseCustomLink.NoticeType.withinApp

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A notice type that indicates that you display the destination in a web view or native experience within the app.

**Availability**:
- iOS 18.1+ - Deprecated in 27.2
- iPadOS 18.1+ - Deprecated in 27.2
- Mac Catalyst 18.1+ - Deprecated in 27.2
- macOS 15.1+ - Deprecated in 27.2
- tvOS 18.1+ - Deprecated in 27.2
- visionOS 2.1+ - Deprecated in 27.2
- watchOS 11.1+ - Deprecated in 27.2

> **Deprecated**: Use `ExternalPurchaseType` instead.

## Declaration

```swift
case withinApp
```

## Discussion

After displaying a notice with this notice type using [`showNotice(type:)`](../shownotice%28type%29.md), if the customer chooses to continue, the app displays the destination in a web view or native experience within the app.

## See Also

### Getting notice types
- [ExternalPurchaseCustomLink.NoticeType.browser](./browser.md)
  A notice type that indicates your app displays external purchases in a destination of your choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/noticetype/withinapp)*