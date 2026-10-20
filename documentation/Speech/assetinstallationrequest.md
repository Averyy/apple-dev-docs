# AssetInstallationRequest

**Framework**: Speech  
**Kind**: class  
**Role**: Class

An object that describes, downloads, and installs a selection of assets.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@objc
final class AssetInstallationRequest
```

#### Overview

You do not create instances of this type directly; obtain them from [`assetInstallationRequest(supporting:)`](./assetinventory/assetinstallationrequest%28supporting%29.md).

The system consolidates download and installation requests; you may obtain several of these instances and call [`downloadAndInstall()`](./assetinstallationrequest/downloadandinstall%28%29.md) several times without causing redundant downloads.

## Topics

### Performing an installation request
- [func downloadAndInstall() async throws](./assetinstallationrequest/downloadandinstall%28%29.md)
  Downloads and installs assets not already on the device.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [ProgressReporting](../Foundation/progressreporting.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset and resource management
- [enum SpeechModels](./speechmodels.md)
  Namespace for methods related to model management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinstallationrequest)*