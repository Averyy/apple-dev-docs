# installingApps

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

The set of apps that are pending installation completion.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final var installingApps: Set<AppLibrary.App> { get set }
```

## See Also

### Installing apps as a marketplace
- [AppLibrary.App](./app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](./installationrequest.md)
  A request to install an app distribution package for a given account.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](./requestappinstallation%28_%29.md)
  Requests the installation of the given app distribution package for the given account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/installingapps)*