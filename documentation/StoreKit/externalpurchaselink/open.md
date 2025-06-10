# open()

**Framework**: StoreKit  
**Kind**: method

Presents a continuation sheet that enables people to choose whether your app shows its link for external purchases.

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
static func open() async throws
```

## Mentions

- [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md)

#### Discussion

Use this method if your app configures the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) property list key.

Call this asynchronous method to have the system attempt to open the external purchase link, as shown below:

```swift
try await ExternalPurchaseLink.open()
```

To use this method, follow these steps:

1. Call [`canOpen`](externalpurchaselink/canopen.md) to determine whether to display a button or other user-interface controls that enable you to call [`open()`](externalpurchaselink/open().md). If it returns `true`, your app can display the user-interface controls to enable deliberate user interaction.
2. In response to deliberate user interaction, such as tapping a button, call [`open()`](externalpurchaselink/open().md). The system displays the continuation sheet that enables the user to choose whether to continue to view your app’s external purchase URL. This asynchronous method returns before the system presents the continuation sheet, and throws an error if [`canOpen`](externalpurchaselink/canopen.md) is `false`.

If the person chooses to continue, this method opens the current storefront’s destination URL that you configure in the [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink) property list key and appends an external purchase token and the app’s bundleID to the URL. For example, StoreKit opens the following URL on the default browser if your destination URL is `https://site.example.com`:

```http
https://site.example.com?externalPurchaseToken=ewoJImFwcEFwcGxlSWQiOjEyMzQ1Njc4OTAsCgkiYnVuZGxlSWQiOiJjb20uZXhhbXBsZSIsCgkidG9rZW5DcmVhdGlvbkRhdGUiOjE3MDYxNjk2MDAwMDAsCgkiZXh0ZXJuYWxQdXJjaGFzZUlkIjoiMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAwIgp9&bundleId=com.example

```

> ❗ **Important**:  Record and use the external purchase token to report the customer’s external purchases to Apple. For more information, see [`External Purchase Server API`](https://developer.apple.com/documentation/ExternalPurchaseServerAPI).

##### Handle Errors

This method throws a [`StoreKitError`](storekiterror.md) if any of the following are true:

- Your app doesn’t have the [`com.apple.developer.storekit.external-purchase-link`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-purchase-link) entitlement.
- You haven’t configured external purchases for the current App Store storefront in [`SKExternalPurchaseLink`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKExternalPurchaseLink).
- The current App Store storefront doesn’t support external purchases.
- The person is ineligible to make external purchases.
- A network or system error occurs.

For more information about App Store storefronts, see [`Storefront`](storefront.md).

## See Also

- [SKExternalPurchaseLink](../BundleResources/Information-Property-List/SKExternalPurchaseLink.md)
  A dictionary that contains URLs to websites where people using your app can make external purchases for supported regions.
- [static var canOpen: Bool](externalpurchaselink/canopen.md)
  A Boolean value that indicates whether the app can successfully open the configured external purchase link in the current App Store storefront.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externalpurchaselink/open())*