# indicatesNonRectilinearProjection

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates the video track carries information related to how it should be projected for display.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static let indicatesNonRectilinearProjection: AVMediaCharacteristic
```

#### Discussion

This media characteristic is currently synthesized if the CMVideoFormatDescription specifies a non-rectilinear projection. To determine which kind of projection is indicated, look for the format description extension with key kCMFormatDescriptionExtension_ProjectionKind. The value of this characteristic is @“public.indicates-non-rectilinear-projection”. Note for content authors: the presence of this characteristic is strictly inferred from the format description of the associated track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/indicatesnonrectilinearprojection)*