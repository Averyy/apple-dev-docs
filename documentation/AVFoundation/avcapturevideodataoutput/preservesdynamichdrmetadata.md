# preservesDynamicHDRMetadata

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var preservesDynamicHDRMetadata: Bool { get set }
```

#### Discussion

Indicates whether the receiver should preserve dynamic HDR metadata as an attachment on the output sample buffer’s underlying CVPixelBufferRef.

Set this property to YES if you wish to use AVCaptureVideoDataOutput with AVAssetWriter to record HDR movies. You must also set `kVTCompressionPropertyKey_PreserveDynamicHDRMetadata` to `true` in the compression settings you pass to your `AVAssetWriterInput`. These compression settings are represented under the `AVVideoCompressionPropertiesKey` sub-dictionary of your top-level AVVideoSettings. When this key is set to true, performance improves, as the encoder is able to skip HDR metadata calculation for every frame. The default value is NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/preservesdynamichdrmetadata)*