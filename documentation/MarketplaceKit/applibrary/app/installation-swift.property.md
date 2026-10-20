# installation

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

The progress of the app’s installation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final var installation: AppLibrary.App.Installation? { get }
```

## See Also

### Inspecting app installation and update status
- [AppLibrary.App.Installation](./installation-swift.struct.md)
  A structure that provides progress information for a specific app installation.
- [var isInstalled: Bool](./isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](./isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](./isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.
- [var installationError: MarketplaceKitError?](./installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/installation-swift.property)*