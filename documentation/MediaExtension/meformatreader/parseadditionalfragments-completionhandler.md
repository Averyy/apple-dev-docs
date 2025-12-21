# parseAdditionalFragments(completionHandler:)

**Framework**: MediaExtension  
**Kind**: method

Incorporates additional fragments that the file received after the last time the format reader parsed it.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func parseAdditionalFragments() async throws -> MEFormatReaderParseAdditionalFragmentsStatus
```

#### Discussion

This method additional fragments of the media asset if they exist. Media asset formats that don’t support incremental fragments don’t need implement this method. Create the [`MEFormatReader`](meformatreader.md) object with the [`MEFormatReaderInstantiationOptions`](meformatreaderinstantiationoptions.md) property [`allowIncrementalFragmentParsing`](meformatreaderinstantiationoptions/allowincrementalfragmentparsing.md) set to [`true`](https://developer.apple.com/documentation/Swift/true). This method does nothing if the value for [`MEFileInfo.FragmentsStatus`](mefileinfo/fragmentsstatus-swift.enum.md) is [`MEFileInfo.FragmentsStatus.containsFragments`](mefileinfo/fragmentsstatus-swift.enum/containsfragments.md). Once this method returns an error, additional calls fail.

## Parameters

- `completionHandler`: The completion block to execute when the parse operation finishes.

## See Also

- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](meformatreader/loadfileinfo(completionhandler:).md)
  Loads the file info object with the properties of the media asset.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](meformatreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset.
- [func loadTrackReaders(completionHandler: ([any METrackReader]?, (any Error)?) -> Void)](meformatreader/loadtrackreaders(completionhandler:).md)
  Loads the array of track readers that represent the tracks in the media asset.
- [struct MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus.md)
  Informational status flags that the format reader returns after parsing additional fragments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreader/parseadditionalfragments(completionhandler:))*