# MEFormatReaderParseAdditionalFragmentsStatus

**Framework**: MediaExtension  
**Kind**: struct

Informational status flags that the format reader returns after parsing additional fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MEFormatReaderParseAdditionalFragmentsStatus
```

## Topics

### Creating informational status flags
- [init(rawValue: UInt)](meformatreaderparseadditionalfragmentsstatus/init(rawvalue:).md)
  Create a new information status flag for parsing additional fragments.
### Evaluating a fragment parsing operation
- [static var sizeIncreased: MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus/sizeincreased.md)
  Indicates that the format reader file size increased.
- [static var fragmentAdded: MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus/fragmentadded.md)
  Indicates that the format reader received one or more fragments.
- [static var fragmentsComplete: MEFormatReaderParseAdditionalFragmentsStatus](meformatreaderparseadditionalfragmentsstatus/fragmentscomplete.md)
  Indicates that the format reader can’t receive any more fragments.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](meformatreader/loadfileinfo(completionhandler:).md)
  Loads the file info object with the properties of the media asset.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](meformatreader/loadmetadata(completionhandler:).md)
  Loads the array of metadata items from the media asset.
- [func loadTrackReaders(completionHandler: ([any METrackReader]?, (any Error)?) -> Void)](meformatreader/loadtrackreaders(completionhandler:).md)
  Loads the array of track readers that represent the tracks in the media asset.
- [func parseAdditionalFragments(completionHandler: (MEFormatReaderParseAdditionalFragmentsStatus, (any Error)?) -> Void)](meformatreader/parseadditionalfragments(completionhandler:).md)
  Incorporates additional fragments that the file received after the last time the format reader parsed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderparseadditionalfragmentsstatus)*