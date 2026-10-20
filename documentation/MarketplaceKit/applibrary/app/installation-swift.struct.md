# AppLibrary.App.Installation

**Framework**: MarketplaceKit  
**Kind**: struct  
**Role**: Structure

A structure that provides progress information for a specific app installation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Installation
```

#### Overview

The [`installation`](./installation-swift.property.md) property of the[`AppLibrary.App`](../app.md) class is of this type.

## Topics

### Inspecting installation progress
- [var progress: Progress](./installation-swift.struct/progress.md)
  The progress representing the download & installation of this app. It may be used to pause, resume, or cancel installation depending on the state of this object.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting app installation and update status
- [var installation: AppLibrary.App.Installation?](./installation-swift.property.md)
  The progress of the app’s installation.
- [var isInstalled: Bool](./isinstalled.md)
  A Boolean value that indicates whether the app’s installation is complete.
- [var isInstalling: Bool](./isinstalling.md)
  A Boolean value that indicates whether the app’s installation is in progress.
- [var isUpdating: Bool](./isupdating.md)
  A Boolean value that indicates whether an app’s update is in progress.
- [var installationError: MarketplaceKitError?](./installationerror.md)
  An error that occurs during the installation of an app that resides on a marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/app/installation-swift.struct)*