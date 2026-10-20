# requestAppInstallation(_:)

**Framework**: MarketplaceKit  
**Kind**: method  
**Role**: Instance Method

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

### Installing apps as a marketplace
- [AppLibrary.App](./app.md)
  Information about an app that someone installs from a marketplace, including its ID and installation status.
- [AppLibrary.InstallationRequest](./installationrequest.md)
  A request to install an app distribution package for a given account.
- [var installingApps: Set<AppLibrary.App>](./installingapps.md)
  The set of apps that are pending installation completion.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the library is currently loading apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestappinstallation(_:))*