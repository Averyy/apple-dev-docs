# assetWriterInputMetadataAdaptorWithAssetWriterInput:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new metadata adaptor to append timed metadata groups to write to an output file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) assetWriterInputMetadataAdaptorWithAssetWriterInput:(AVAssetWriterInput *) input;
```

## Return Value

An input metadata adaptor.

## Parameters

- `input`: The metadata input to which to append groups of timed metadata.

## See Also

### Creating an input metadata adaptor
- [init(assetWriterInput: AVAssetWriterInput)](./init%28assetwriterinput%29.md)
  Creates a metadata group adaptor to append timed metadata groups to write to an output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/assetwriterinputmetadataadaptorwithassetwriterinput:)*