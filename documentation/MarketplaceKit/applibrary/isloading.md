# isLoading

**Framework**: MarketplaceKit  
**Kind**: property

A Boolean value that indicates whether the library is currently loading apps.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final var isLoading: Bool { get }
```

## See Also

- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](applibrary/installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
  The set of apps that are pending installation completion.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](applibrary/requestappinstallation(_:).md)
  Requests the installation of the given app distribution package for the given account.
- [func requestAppInstallationFromBrowser(for: URL, referrer: URL) async throws](applibrary/requestappinstallationfrombrowser(for:referrer:).md)
  Forwards an app installation request from the developer’s webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/isloading)*