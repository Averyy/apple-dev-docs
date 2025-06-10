# quickTimeMetadataCinematicVideoIntent

**Framework**: AVFoundation  
**Kind**: property

A value of type `kCMMetadataBaseDataType_UInt8` indicating whether this movie is intended as a Cinematic Video (1) or not (0).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static let quickTimeMetadataCinematicVideoIntent: AVMetadataIdentifier
```

#### Discussion

This movie-level metadata is automatically added (with a value of 1) to a movie recorded using the Cinematic Video API. Clients can override it with a value of 0 to signal that this movie is not to be treated as a Cinematic Video by Apple’s software like Photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacinematicvideointent)*