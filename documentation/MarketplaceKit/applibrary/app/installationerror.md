# installationError

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

An error that occurs during the installation of an app that resides on a marketplace.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
final var installationError: MarketplaceKitError? { get }
```

## See Also

### Inspecting app installation and update status
- [var installation: AppLibrary.App.Installation?](./installation-swift.property.md)
  The progress of the app’s installation.
- [AppLibrary.App.Installation](./installation-swift.struct.md)
  A structure that provides progress information for a specific app installation.
- [var isInstalled: Bool](./isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](./isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](./isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/installationerror)*