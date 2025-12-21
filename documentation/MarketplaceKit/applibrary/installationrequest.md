# AppLibrary.InstallationRequest

**Framework**: MarketplaceKit  
**Kind**: struct

A request to install an app distribution package for a given account.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct InstallationRequest
```

## Topics

### Initializing an app installation request
- [init(alternativeDistributionPackageURL: URL, account: String, installVerificationToken: String)](applibrary/installationrequest/init(alternativedistributionpackageurl:account:installverificationtoken:).md)
### Inspecting app installation information
- [var account: String](applibrary/installationrequest/account.md)
- [var alternativeDistributionPackageURL: URL](applibrary/installationrequest/alternativedistributionpackageurl.md)
- [var appShareURL: URL?](applibrary/installationrequest/appshareurl.md)
- [var installVerificationToken: String](applibrary/installationrequest/installverificationtoken.md)

## See Also

- [AppLibrary.App](applibrary/app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [var installingApps: Set<AppLibrary.App>](applibrary/installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](applibrary/isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](applibrary/requestappinstallation(_:).md)
  Requests the installation of the given app distribution package for the given account.
- [func requestAppInstallationFromBrowser(for: URL, referrer: URL) async throws](applibrary/requestappinstallationfrombrowser(for:referrer:).md)
  Forwards an app installation request from the developer’s webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/installationrequest)*