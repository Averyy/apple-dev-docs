# AVAssetReaderOutputCaptionAdaptor

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that reads caption group objects from an asset track that contains timed text.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

## Declaration

```swift
class AVAssetReaderOutputCaptionAdaptor
```

```objc
@interface AVAssetReaderOutputCaptionAdaptor : NSObject
```

## Topics

### Creating a caption adaptor
- [init(assetReaderTrackOutput: AVAssetReaderTrackOutput)](./avassetreaderoutputcaptionadaptor/init%28assetreadertrackoutput%29.md)
  Creates a caption adaptor that reads from a track output.
### Accessing the track output
- [var assetReaderTrackOutput: AVAssetReaderTrackOutput](./avassetreaderoutputcaptionadaptor/assetreadertrackoutput.md)
  The associated asset reader track output.
### Managing the validation delegate
- [var validationDelegate: (any AVAssetReaderCaptionValidationHandling)?](./avassetreaderoutputcaptionadaptor/validationdelegate.md)
  A delegate object that handles callbacks to the caption adaptor.
- [protocol AVAssetReaderCaptionValidationHandling](./avassetreadercaptionvalidationhandling.md)
  A protocol that defines the methods for caption validation events.
### Reading caption groups
- [func nextCaptionGroup() -> AVCaptionGroup?](./avassetreaderoutputcaptionadaptor/nextcaptiongroup%28%29.md)
  Returns the next caption group.
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](./avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups%28in%29.md)
  Returns the set of captions in the caption group that weren’t vended by the adaptor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Reading and writing
- [class AVAssetWriterInputCaptionAdaptor](./avassetwriterinputcaptionadaptor.md)
  An object that appends captions to an asset writer input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor)*