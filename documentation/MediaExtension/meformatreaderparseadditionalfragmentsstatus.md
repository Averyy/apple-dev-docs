# MEFormatReaderParseAdditionalFragmentsStatus

**Framework**: MediaExtension  
**Kind**: struct  
**Role**: Structure

Informational status flags that the format reader returns after parsing additional fragments.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MEFormatReaderParseAdditionalFragmentsStatus
```

```c
enum MEFormatReaderParseAdditionalFragmentsStatus : NSUInteger;
```

## Topics

### Creating informational status flags
- [init(rawValue: UInt)](./meformatreaderparseadditionalfragmentsstatus/init%28rawvalue%29.md)
  Create a new information status flag for parsing additional fragments.
### Evaluating a fragment parsing operation
- [static var sizeIncreased: MEFormatReaderParseAdditionalFragmentsStatus](./meformatreaderparseadditionalfragmentsstatus/sizeincreased.md)
  Indicates that the format reader file size increased.
- [static var fragmentAdded: MEFormatReaderParseAdditionalFragmentsStatus](./meformatreaderparseadditionalfragmentsstatus/fragmentadded.md)
  Indicates that the format reader received one or more fragments.
- [static var fragmentsComplete: MEFormatReaderParseAdditionalFragmentsStatus](./meformatreaderparseadditionalfragmentsstatus/fragmentscomplete.md)
  Indicates that the format reader can’t receive any more fragments.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Reading and parsing media assets
- [func loadFileInfo(completionHandler: (MEFileInfo?, (any Error)?) -> Void)](./meformatreader/loadfileinfo%28completionhandler%29.md)
  Loads the file info object with the properties of the media asset.
- [func loadMetadata(completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](./meformatreader/loadmetadata%28completionhandler%29.md)
  Loads the array of metadata items from the media asset.
- [func loadTrackReaders(completionHandler: ([any METrackReader]?, (any Error)?) -> Void)](./meformatreader/loadtrackreaders%28completionhandler%29.md)
  Loads the array of track readers that represent the tracks in the media asset.
- [func parseAdditionalFragments(completionHandler: (MEFormatReaderParseAdditionalFragmentsStatus, (any Error)?) -> Void)](./meformatreader/parseadditionalfragments%28completionhandler%29.md)
  Incorporates additional fragments that the file received after the last time the format reader parsed it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meformatreaderparseadditionalfragmentsstatus)*