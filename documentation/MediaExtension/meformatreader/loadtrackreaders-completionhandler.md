# loadTrackReaders(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

Loads the array of track readers that represent the tracks in the media asset.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var trackReaders: [any METrackReader] { get async throws }
```

## Parameters

- `completionHandler`: The completion block to execute when the load operation finishes.

## See Also

- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](meformatreader/loadfileinfo(completionhandler:).md)
  Loads the file info object with the properties of the media asset.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](meformatreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset.
- [func parseAdditionalFragments(completionHandler: (MEFormatReaderParseAdditionalFragmentsStatus, (any Error)?) -> Void)](meformatreader/parseadditionalfragments(completionhandler:).md)
  Incorporates additional fragments that the file received after the last time the format reader parsed it.
- [struct MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus.md)
  Informational status flags that the format reader returns after parsing additional fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreader/loadtrackreaders(completionhandler:))*