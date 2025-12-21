# AVAssetWriterInputCaptionAdaptor

**Framework**: AVFoundation  
**Kind**: class

An object that appends captions to an asset writer input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVAssetWriterInputCaptionAdaptor
```

## Topics

### Creating a caption adaptor
- [init(assetWriterInput: AVAssetWriterInput)](avassetwriterinputcaptionadaptor/init(assetwriterinput:).md)
  Creates a new caption adaptor that writes to the specified asset writer input.
### Accessing the writer input
- [var assetWriterInput: AVAssetWriterInput](avassetwriterinputcaptionadaptor/assetwriterinput.md)
  The associated asset writer input.
### Appending captions
- [func append(AVCaption) -> Bool](avassetwriterinputcaptionadaptor/append(_:)-910lp.md)
  Appends a caption to the writer input.
- [func append(AVCaptionGroup) -> Bool](avassetwriterinputcaptionadaptor/append(_:)-4ils8.md)
  Appends a caption group that the system writes to the output.

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

- [class AVAssetReaderOutputCaptionAdaptor](avassetreaderoutputcaptionadaptor.md)
  An object that reads caption group objects from an asset track that contains timed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor)*