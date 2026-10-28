# showNotice(type:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Displays the system disclosure notice sheet and asks the customer whether to continue.

**Availability**:
- iOS 18.1+ - Deprecated in 27.2
- iPadOS 18.1+ - Deprecated in 27.2
- Mac Catalyst 18.1+ - Deprecated in 27.2
- macOS 15.1+ - Deprecated in 27.2
- tvOS 18.1+ - Deprecated in 27.2
- visionOS 2.1+ - Deprecated in 27.2
- watchOS 11.1+ - Deprecated in 27.2

> **Deprecated**: Use `showNotice(for:)` instead.

## Declaration

```swift
static func showNotice(type: ExternalPurchaseCustomLink.NoticeType) async throws -> ExternalPurchaseCustomLink.NoticeResult
```

## Return Value

Returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](./noticeresult/continued.md) to indicate the customer chooses to continue, or [`ExternalPurchaseCustomLink.NoticeResult.cancelled`](./noticeresult/cancelled.md) to indicate the customer chooses not to continue to view external purchases. This method throws an error if your app isn’t eligible, at runtime, to use this API.

## Discussion

Use this method if your app configures the [`SKExternalPurchaseCustomLinkRegions`](../../BundleResources/information-property-list/skexternalpurchasecustomlinkregions.md) or [`SKExternalPurchaseLinkStreamingRegions`](../../BundleResources/information-property-list/skexternalpurchaselinkstreamingregions.md) property list keys.

Call this method to display the system disclosure sheet before your app continues to communicate and promote offers for purchase in a distribution channel of your choice. Call this method in response to a deliberate customer action, such as tapping a button.

Select the notice type based on how your app communicates the offers if the customer chooses to continue:

- Use [`ExternalPurchaseCustomLink.NoticeType.browser`](./noticetype/browser.md) if the app goes to the background, and promotes offers in a destination outside of the app.
- Use [`ExternalPurchaseCustomLink.NoticeType.withinApp`](./noticetype/withinapp.md) if the app promotes offers in a web view or native experience within the app.

Continue to communicate and promote offers if [`showNotice(type:)`](./shownotice%28type%29.md) returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](./noticeresult/continued.md); otherwise don’t continue.

For example code that calls this method, see [`ExternalPurchaseCustomLink`](../externalpurchasecustomlink.md).

## Parameters

- `type`: An [`ExternalPurchaseCustomLink.NoticeType`](./noticetype.md) value you select that determines the disclosure sheet the system displays.

## See Also

### Deprecated methods and values
- [ExternalPurchaseCustomLink.NoticeType](./noticetype.md)
  The custom link out style that informs the type of disclosure notice to display.
- [static func token(for: String) async throws -> ExternalPurchaseCustomLink.Token?](./token%28for%29-1fyo.md)
  Returns an external purchase token of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/shownotice(type:))*