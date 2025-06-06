# showNotice(type:)

**Framework**: StoreKit  
**Kind**: method

Displays the system disclosure notice sheet and asks the customer whether to continue.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult
```

#### Return Value

Returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](externalpurchasecustomlink/noticeresult/continued.md) to indicate the customer chooses to continue, or [`ExternalPurchaseCustomLink.NoticeResult.cancelled`](externalpurchasecustomlink/noticeresult/cancelled.md) to indicate the customer chooses not to continue to view external purchases. This method throws an error if your app isn’t eligible, at runtime, to use this API.

#### Discussion

Use this method if your app configures the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseCustomLinkRegions) property list key.

Call this method to display the system disclosure sheet before your app continues to offer external purchases. Call this method in response to a deliberate customer action, such as tapping a button.

Select the notice type based on how your app presents the custom link to external purchases if the customer chooses to continue:

- Use [`ExternalPurchaseCustomLink.NoticeType.browser`](externalpurchasecustomlink/noticetype/browser.md) if the app goes to the background, and presents external purchases in a destination outside of the app, which can be an alternative app marketplace, another app, or a website on a browser.
- Use [`ExternalPurchaseCustomLink.NoticeType.withinApp`](externalpurchasecustomlink/noticetype/withinapp.md) if the app displays the destination in a web view.

Continue to offer external purchases if [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](externalpurchasecustomlink/noticeresult/continued.md); otherwise don’t continue.

For example code that calls this method, see [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md).

## Parameters

- `type`: An   value that determines the disclosure sheet the system displays.

## See Also

- [ExternalPurchaseCustomLink.NoticeType](externalpurchasecustomlink/noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.
- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/shownotice(type:))*