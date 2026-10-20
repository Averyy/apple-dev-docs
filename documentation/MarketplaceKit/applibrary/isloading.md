# isLoading

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

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

### Installing apps as a marketplace
- [AppLibrary.App](./app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](./installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](./installingapps.md)
  The set of apps that are pending installation completion.
- [func requestAppInstallation(AppLibrary.InstallationRequest) async throws](./requestappinstallation%28_%29.md)
  Requests the installation of the given app distribution package for the given account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/isloading)*