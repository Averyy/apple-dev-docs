# sparselyInterleavedWithMainMediaData

**Framework**: AVFoundation  
**Kind**: property

Indicates that there may be large segments of time without any media data from this track. When mediaDataLocation is set to this value, AVAssetWriter will interleave the media data, but will not wait for media data from this track to achieve tight interleaving with other tracks.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let sparselyInterleavedWithMainMediaData: AVAssetWriterInput.MediaDataLocation
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/mediadatalocation-swift.struct/sparselyinterleavedwithmainmediadata)*