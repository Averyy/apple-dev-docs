# status(forModules:)

**Framework**: Speech  
**Kind**: method

Returns the status for the list of modules.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func status(forModules modules: [any SpeechModule]) async -> AssetInventory.Status
```

#### Discussion

If the status differs between modules, it returns the lowest status in order from `unsupported`, `supported`, `downloading`, `installed`.

## See Also

- [AssetInventory.Status](assetinventory/status.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/status(formodules:))*