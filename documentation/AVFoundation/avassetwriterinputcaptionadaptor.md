# AVAssetWriterInputCaptionAdaptor

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that appends captions to an asset writer input.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputCaptionReceiver(for:) instead

## Declaration

```swift
class AVAssetWriterInputCaptionAdaptor
```

```objc
@interface AVAssetWriterInputCaptionAdaptor : NSObject
```

## Topics

### Creating a caption adaptor
- [init(assetWriterInput: AVAssetWriterInput)](./avassetwriterinputcaptionadaptor/init%28assetwriterinput%29.md)
  Creates a new caption adaptor that writes to the specified asset writer input.
### Accessing the writer input
- [var assetWriterInput: AVAssetWriterInput](./avassetwriterinputcaptionadaptor/assetwriterinput.md)
  The associated asset writer input.
### Appending captions
- [func append(AVCaption) -> Bool](./avassetwriterinputcaptionadaptor/append%28_%29-910lp.md)
  Appends a caption to the writer input.
- [func append(AVCaptionGroup) -> Bool](./avassetwriterinputcaptionadaptor/append%28_%29-4ils8.md)
  Appends a caption group that the system writes to the output.

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
- [class AVAssetReaderOutputCaptionAdaptor](./avassetreaderoutputcaptionadaptor.md)
  An object that reads caption group objects from an asset track that contains timed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor)*