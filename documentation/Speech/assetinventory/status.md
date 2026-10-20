# AssetInventory.Status

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Status
```

## Topics

### Asset status
- [AssetInventory.Status.downloading](./status/downloading.md)
  The system is currently downloading the assets, or waiting for conditions to improve and continue downloading later.
- [AssetInventory.Status.installed](./status/installed.md)
  The necessary assets have been downloaded and installed on the device, and the module is ready for use.
- [AssetInventory.Status.supported](./status/supported.md)
  The module can work with its configuration, but the assets will need to be downloaded.
- [AssetInventory.Status.unsupported](./status/unsupported.md)
  The module will not work with its configuration.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Checking asset status
- [static func status(forModules: [any SpeechModule]) async -> AssetInventory.Status](./status%28formodules%29.md)
  Returns the status for the list of modules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/status)*