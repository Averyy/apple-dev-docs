# AssetInventory.Status.installed

**Framework**: Speech  
**Kind**: case

The necessary assets have been downloaded and installed on the device, and the module is ready for use.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case installed
```

## See Also

- [AssetInventory.Status.downloading](assetinventory/status/downloading.md)
  The system is currently downloading the assets, or waiting for conditions to improve and continue downloading later.
- [AssetInventory.Status.supported](assetinventory/status/supported.md)
  The module can work with its configuration, but the assets will need to be downloaded.
- [AssetInventory.Status.unsupported](assetinventory/status/unsupported.md)
  The module will not work with its configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/status/installed)*