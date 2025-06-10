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
### Default Implementations
- [Equatable Implementations](meformatreaderparseadditionalfragmentsstatus/equatable-implementations.md)
- [OptionSet Implementations](meformatreaderparseadditionalfragmentsstatus/optionset-implementations.md)
- [SetAlgebra Implementations](meformatreaderparseadditionalfragmentsstatus/setalgebra-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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