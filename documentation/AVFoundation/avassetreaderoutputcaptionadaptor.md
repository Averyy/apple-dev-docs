# AVAssetReaderOutputCaptionAdaptor

**Framework**: AVFoundation  
**Kind**: class

An object that reads caption group objects from an asset track that contains timed text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVAssetReaderOutputCaptionAdaptor
```

## Topics

### Creating a caption adaptor
- [init(assetReaderTrackOutput: AVAssetReaderTrackOutput)](avassetreaderoutputcaptionadaptor/init(assetreadertrackoutput:).md)
  Creates a caption adaptor that reads from a track output.
### Accessing the track output
- [var assetReaderTrackOutput: AVAssetReaderTrackOutput](avassetreaderoutputcaptionadaptor/assetreadertrackoutput.md)
  The associated asset reader track output.
### Managing the validation delegate
- [var validationDelegate: (any AVAssetReaderCaptionValidationHandling)?](avassetreaderoutputcaptionadaptor/validationdelegate.md)
  A delegate object that handles callbacks to the caption adaptor.
- [protocol AVAssetReaderCaptionValidationHandling](avassetreadercaptionvalidationhandling.md)
  A protocol that defines the methods for caption validation events.
### Reading caption groups
- [func nextCaptionGroup() -> AVCaptionGroup?](avassetreaderoutputcaptionadaptor/nextcaptiongroup.md)
  Returns the next caption group.
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:).md)
  Returns the set of captions in the caption group that weren’t vended by the adaptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAssetWriterInputCaptionAdaptor](avassetwriterinputcaptionadaptor.md)
  An object that appends captions to an asset writer input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor)*