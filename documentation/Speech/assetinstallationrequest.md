# AssetInstallationRequest

**Framework**: Speech  
**Kind**: class

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

You do not create instances of this type directly; obtain them from [`assetInstallationRequest(supporting:)`](assetinventory/assetinstallationrequest(supporting:).md).

The system consolidates download and installation requests; you may obtain several of these instances and call [`downloadAndInstall()`](assetinstallationrequest/downloadandinstall().md) several times without causing redundant downloads.

## Topics

### Performing an installation request
- [func downloadAndInstall() async throws](assetinstallationrequest/downloadandinstall.md)
  Downloads and installs assets not already on the device.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [ProgressReporting](../foundation/progressreporting.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum SpeechModels](speechmodels.md)
  Namespace for methods related to model management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinstallationrequest)*