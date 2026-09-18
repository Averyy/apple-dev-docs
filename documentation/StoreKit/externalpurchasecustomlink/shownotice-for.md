# showNotice(for:)

**Framework**: StoreKit  
**Kind**: method

Displays the system disclosure notice sheet for a custom link type and asks the customer whether to continue.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- tvOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
static func showNotice(for externalPurchaseType: ExternalPurchaseCustomLink.ExternalPurchaseType) async throws -> ExternalPurchaseCustomLink.NoticeResult
```

#### Return Value

This method returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](externalpurchasecustomlink/noticeresult/continued.md) to indicate the customer chooses to continue, or [`ExternalPurchaseCustomLink.NoticeResult.cancelled`](externalpurchasecustomlink/noticeresult/cancelled.md) to indicate the customer chooses not to continue to view external purchases. This method throws an error if your app isn’t eligible to use this API at runtime. In case of an error, this method throws a [`StoreKitError`](storekiterror.md).

#### Discussion

Use this method in combination with a specific entitlement entitlement assigned to your app and  Information Property List key depending on the region where you want to offer external purchases, following these guidelines:

- The  [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link) entitlement requires the [`SKExternalPurchaseCustomLinkRegions`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchasecustomlinkregions) Information Property List key.
- The [`com.apple.developer.storekit.external-purchase-link-streaming`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming) entitlement requires the [`SKExternalPurchaseLinkStreamingRegions`](https://developer.apple.com/documentation/bundleresources/information-property-list/skexternalpurchaselinkstreamingregions) Information Property List key.
- The [`StoreKit external purchases or offers entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement is a standalone entitlement and doesn’t require any additional Information Property List key.

An app needs to call this method when a customer taps on a button or scans a QR code to begin a purchase through an alternative payment processor within an app, or to go out of the app to engage with an offer.  If [`isEligible`](externalpurchasecustomlink/iseligible.md) is `false`, this method always fails.

Select the notice type based on how your app communicates the offers if the customer chooses to continue:

- Use [`ExternalPurchaseCustomLink.ExternalPurchaseType.outOfApp(destinationURL:)`](externalpurchasecustomlink/externalpurchasetype/outofapp(destinationurl:).md) if the app goes to the background, and promotes offers in a destination outside of the app.
- Use [`ExternalPurchaseCustomLink.ExternalPurchaseType.withinApp`](externalpurchasecustomlink/externalpurchasetype/withinapp.md) if the app promotes offers in a web view or native experience within the app.

Continue with the offer if [`showNotice(type:)`](externalpurchasecustomlink/shownotice(type:).md) returns [`ExternalPurchaseCustomLink.NoticeResult.continued`](externalpurchasecustomlink/noticeresult/continued.md); otherwise, don’t continue.

> ❗ **Important**: This API only works in countries or regions where the [`StoreKit external purchases or offers entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions) entitlement is available. See the entitlement documentation for additional information.

For example code that calls this method, see [`ExternalPurchaseCustomLink`](externalpurchasecustomlink.md).

##### See Also

- [`ExternalPurchaseCustomLink.NoticeResult`](externalpurchasecustomlink/noticeresult.md)
- [`ExternalPurchaseCustomLink.ExternalPurchaseType`](externalpurchasecustomlink/externalpurchasetype.md)

## Parameters

- `externalPurchaseType`: An [`ExternalPurchaseCustomLink.ExternalPurchaseType`](externalpurchasecustomlink/externalpurchasetype.md) value you select that determines the disclosure sheet the system displays.

## See Also

- [ExternalPurchaseCustomLink.NoticeResult](externalpurchasecustomlink/noticeresult.md)
  The result of showing the disclosure notice.
- [ExternalPurchaseCustomLink.ExternalPurchaseType](externalpurchasecustomlink/externalpurchasetype.md)
  Values that represent the types of external purchase an app can perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/shownotice(for:))*