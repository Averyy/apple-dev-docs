# AppLibrary.App.Installation

**Framework**: MarketplaceKit  
**Kind**: struct

A structure that provides progress information for a specific app installation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Installation
```

#### Overview

The [`installation`](applibrary/app/installation-swift.property.md) property of the[`AppLibrary.App`](applibrary/app.md) class is of this type.

## Topics

### Inspecting installation progress
- [var progress: Progress](applibrary/app/installation-swift.struct/progress.md)
  The progress representing the download & installation of this app. It may be used to pause, resume, or cancel installation depending on the state of this object.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var installation: AppLibrary.App.Installation?](applibrary/app/installation-swift.property.md)
  The progress of the app’s installation.
- [var isInstalled: Bool](applibrary/app/isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](applibrary/app/isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](applibrary/app/isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.
- [var installationError: MarketplaceKitError?](applibrary/app/installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/installation-swift.struct)*