# AssetInstallationRequest

**Framework**: Speech  
**Kind**: class

An object that describes, downloads, and installs a selection of assets.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@objc
final class AssetInstallationRequest
```

#### Overview

You do not create instances of this type directly; obtain them from [`assetInstallationRequest(supporting:)`](assetinventory/assetinstallationrequest(supporting:).md).

The system consolidates download and installation requests; you may obtain several of these instances and call [`downloadAndInstall()`](assetinstallationrequest/downloadandinstall().md) several times without causing redundant downloads.

## Topics

### Performing an installation request
- [func downloadAndInstall() async throws](assetinstallationrequest/downloadandinstall.md)
  Downloads and installs assets not already on the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum SpeechModels](speechmodels.md)
  Namespace for methods related to model management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinstallationrequest)*