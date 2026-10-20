# status(forModules:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Returns the status for the list of modules.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func status(forModules modules: [any SpeechModule]) async -> AssetInventory.Status
```

#### Discussion

If the status differs between modules, it returns an applicable status in order from `unsupported`, `downloading`, `supported`, `installed`.

## See Also

### Checking asset status
- [AssetInventory.Status](./status.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinventory/status(formodules:))*