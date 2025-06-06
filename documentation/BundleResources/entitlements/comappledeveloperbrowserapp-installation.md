# com.apple.developer.browser.app-installation

**Framework**: Bundleresources  
**Kind**: typealias

The entitlement that enables a browser to install alternative-distribution apps from a website.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

#### Discussion

The system requires that your browser app have this entitlement to install alternative marketplace apps from a webpage using [`MarketplaceKit`](https://developer.apple.com/documentation/MarketplaceKit). Browser apps that render with either [`WebKit`](https://developer.apple.com/documentation/WebKit) or [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit) need the entitlement. Apple enables it on your account along with the default browser entitlement ([`com.apple.developer.web-browser`](entitlements/com.apple.developer.web-browser.md)).

> ❗ **Important**:  Request the default browser entitlement by filling out the [`Default browser entitlement request form`](https://developer.apple.comhttps://developer.apple.com/contact/request/default-browser-entitlement/). In that form you can also request this entitlement. If you do that and your request for the default browser entitlement is accepted you get both the default browser entitlement and the app-installation entitlement for your browser app.

Your browser app needs to enforce specific webpage criteria as part of using this entitlement. For more information, see [`Enabling alternative distribution app installation in a browser`](https://developer.apple.com/documentation/appdistribution/enabling-alternative-distribution-app-installation-in-a-browser).

If your account receives this entitlement, provision your app with the entitlement according to: [`Provisioning with managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/).

> **Note**:  This entitlement isn’t available for Enterprise or Developer ID distributed apps.

## See Also

- [com.apple.developer.web-browser](entitlements/com.apple.developer.web-browser.md)
  A Boolean that indicates whether the app can act as the user’s default web browser.
- [com.apple.developer.web-browser.public-key-credential](entitlements/com.apple.developer.web-browser.public-key-credential.md)
  A Boolean value that lets your app make registration and assertion requests for passkeys and security keys for any relying party identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.browser.app-installation)*