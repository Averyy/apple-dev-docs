# requestAppInstallationFromBrowser(for:referrer:)

**Framework**: MarketplaceKit  
**Kind**: method

Forwards an app installation request from the developer’s webpage.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
nonisolated
final func requestAppInstallationFromBrowser(for url: URL, referrer: URL) async throws
```

## Mentions

- [Enabling alternative distribution app installation in a browser](enabling-alternative-distribution-app-installation-in-a-browser.md)

#### Discussion

Web browsers that render with [`BrowserEngineKit`](https://developer.apple.com/documentation/BrowserEngineKit) rather than [`WebKit`](https://developer.apple.com/documentation/WebKit) call this method to forward the installation of an app from the developer’s webpage. Your browser listens for [`MarketplaceKitURIScheme`](marketplacekiturischeme.md) invocations to field such requests.

For more information, see [`Enabling alternative distribution app installation in a browser`](enabling-alternative-distribution-app-installation-in-a-browser.md).

## Parameters

- `url`: The unparsed   URL that triggers the installation request.
- `referrer`: The origin of the top frame that contains the alternative marketplace installation URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestappinstallationfrombrowser(for:referrer:))*