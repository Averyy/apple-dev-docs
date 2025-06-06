# open(url:)

**Framework**: StoreKit  
**Kind**: method

Presents a continuation sheet that enables people to choose whether your app shows the indicated URL link for external purchases.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
static func open(url: URL) async throws
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)

#### Discussion

Call this method if your app configures the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key to attempt to open the eligible external purchase link, `url`. Call this asynchronous method as shown below:

```swift
if let eligibleURLs = await ExternalPurchaseLink.eligibleURLs {
    let url = chooseTheUrl(eligibleURLs) // Supply a function to choose one of the eligible URLs.
    try await ExternalPurchaseLink.open(url: url)
  }
```

To use this method, follow these steps:

1. Check the [`eligibleURLs`](externalpurchaselink/eligibleurls.md) array. If the array contains one or more links, your app can display the user-interface controls to enable deliberate user interaction before offering an external purchase link.
2. Select one of the eligible links.
3. In response to deliberate user interaction, such as tapping a button, call [`open(url:)`](externalpurchaselink/open(url:).md) with the link you select.

The system displays the continuation sheet that enables the user to choose whether to continue to view the external purchase link. This asynchronous method returns before the system presents the continuation sheet, and can throw an error.

If the person chooses to continue, this method opens the link that you provide in the `url` parameter, and appends an external purchase token and the app’s bundleID to the URL. For example, StoreKit opens the following link on the default browser if your destination URL is `https://site.example.com`:

```http
https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example
```

> ❗ **Important**:  Record and use the external purchase token to report the customer’s external purchases to Apple. For more information, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

 Record and use the external purchase token to report the customer’s external purchases to Apple. For more information, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Handle Errors

This method throws a [`StoreKitError`](storekiterror.md) if any of the following are true:

- Your app doesn’t have the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement.
- You haven’t configured external purchase links for the current App Store storefront in the [`SKExternalPurchaseMultiLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseMultiLink) property list key.
- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- A network or system error occurs.

For more information about App Store storefronts, see [`Storefront`](storefront.md).

## Parameters

- `url`: An eligible external purchase link that you select from the   array.

## See Also

- [SKExternalPurchaseMultiLink](../BundleResources/Information-Property-List/SKExternalPurchaseMultiLink.md)
  A dictionary that contains an array of URLs to websites where people using your app can make external purchases.
- [static var eligibleURLs: [URL]?](externalpurchaselink/eligibleurls.md)
  An array of external purchase links for the current storefront that the app configured and from which it chooses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchaselink/open(url:))*