# ExternalLinkAccount

**Framework**: StoreKit  
**Kind**: enum

Enables qualifying apps to link to an external website for account creation or management.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.4+

## Declaration

```swift
enum ExternalLinkAccount
```

#### Overview

This functionality is only available to apps with the [`com.apple.developer.storekit.external-link.account`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.storekit.external-link.account) entitlement. For more information, see [`Distributing “reader” apps with a link to your website`](https://developer.apple.comhttps://developer.apple.com/support/reader-apps/).

## Topics

### Linking to external accounts
- [static var canOpen: Bool](externallinkaccount/canopen.md)
  A Boolean value that indicates whether the app can open the external link account.
- [static func open() async throws](externallinkaccount/open.md)
  Presents a continuation sheet that enables people to choose whether to open your app’s link to an external website for account creation or management.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [com.apple.developer.storekit.external-link.account](../BundleResources/Entitlements/com.apple.developer.storekit.external-link.account.md)
  A Boolean value that indicates whether your app can link to an external website for account creation or management.
- [SKExternalLinkAccount](../BundleResources/Information-Property-List/SKExternalLinkAccount.md)
  A dictionary that contains localized URLs to an external website for account creation or management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/externallinkaccount)*