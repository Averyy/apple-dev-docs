# preprocessAsset(configuration:subprogress:)

**Framework**: Cinematic  
**Kind**: method

Preprocesses the asset by generating a disparity track, writing the result to the URL specified in `configuration`. Required for assets whose `cinematicCapability` is `.needsPreprocessing`; on success the returned `CNAssetInfo` will be `.renderable`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+

## Declaration

```swift
func preprocessAsset(configuration: CNAssetPreprocessConfiguration, subprogress: consuming Subprogress? = nil) async throws -> CNAssetInfo
```

#### Return Value

A `CNAssetInfo` for the preprocessed asset at the destination URL.

#### Discussion

Ensure `resourceStatus` is `.ready` before calling — download resources first if needed.

Cancellation: this method responds to Swift Task cancellation. If the calling task is cancelled, the preprocessing stops; any partially processed destination asset is discarded.

> **Note**: `CNCinematicError` on failure.

## Parameters

- `configuration`: Destination URL and whether to embed or reference source tracks.
- `subprogress`: Optional `Subprogress` for integrating into a `ProgressManager` tree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2/preprocessasset(configuration:subprogress:))*