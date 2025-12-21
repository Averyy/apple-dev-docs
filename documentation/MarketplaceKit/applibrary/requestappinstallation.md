# requestAppInstallation(_:)

**Framework**: MarketplaceKit  
**Kind**: method

Requests the installation of the given app distribution package for the given account.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
nonisolated
final func requestAppInstallation(_ request: AppLibrary.InstallationRequest) async throws
```

## See Also

- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](applibrary/installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](applibrary/isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallationFromBrowser(for: URL, referrer: URL) async throws](applibrary/requestappinstallationfrombrowser(for:referrer:).md)
  Forwards an app installation request from the developer’s webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestappinstallation(_:))*