# init(assetWriterInput:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a new caption adaptor that writes to the specified asset writer input.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputCaptionReceiver(for:) instead

## Declaration

```swift
init(assetWriterInput input: AVAssetWriterInput)
```

```objc
- (instancetype) initWithAssetWriterInput:(AVAssetWriterInput *) input;
```

## Parameters

- `input`: The asset writer input.

## See Also

### Creating a caption adaptor
- [+ assetWriterInputCaptionAdaptorWithAssetWriterInput:](./assetwriterinputcaptionadaptorwithassetwriterinput_.md)
  A class method that creates a new caption adaptor that writes to the specified asset writer input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/init(assetwriterinput:))*