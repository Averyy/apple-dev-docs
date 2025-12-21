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

## See Also

- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](applibrary/installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](applibrary/isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](applibrary/requestappinstallation(_:).md)
  Requests the installation of the given app distribution package for the given account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestappinstallationfrombrowser(for:referrer:))*