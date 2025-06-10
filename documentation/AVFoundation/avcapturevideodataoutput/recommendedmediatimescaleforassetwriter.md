# recommendedMediaTimeScaleForAssetWriter

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 16.0+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var recommendedMediaTimeScaleForAssetWriter: CMTimeScale { get }
```

#### Discussion

Indicates the recommended media timescale for the video track.

This will return a recommended media timescale based on the active capture session’s inputs. It will not be less than 600. It may or may not be a multiple of 600.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/recommendedmediatimescaleforassetwriter)*