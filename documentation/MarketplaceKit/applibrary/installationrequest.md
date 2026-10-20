# AppLibrary.InstallationRequest

**Framework**: MarketplaceKit  
**Kind**: struct  
**Role**: Structure

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
- [init(alternativeDistributionPackageURL: URL, account: String, installVerificationToken: String)](./installationrequest/init%28alternativedistributionpackageurl,account,installverificationtoken%29.md)
### Inspecting app installation information
- [var account: String](./installationrequest/account.md)
- [var alternativeDistributionPackageURL: URL](./installationrequest/alternativedistributionpackageurl.md)
- [var appShareURL: URL?](./installationrequest/appshareurl.md)
- [var installVerificationToken: String](./installationrequest/installverificationtoken.md)

## See Also

### Installing apps as a marketplace
- [AppLibrary.App](./app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [var installingApps: Set<AppLibrary.App>](./installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](./requestappinstallation%28_%29.md)
  Requests the installation of the given app distribution package for the given account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/installationrequest)*