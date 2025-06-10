# machineGenerated

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track was generated in an automated fashion by a machine.

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
static let machineGenerated: AVMediaCharacteristic
```

#### Discussion

This media characteristic can be used to distinguish machine generated content from human authored content. The value of this characteristic is @“public.machine-generated”.

Note for content authors: for QuickTime movie and .m4v files and for HTTP Live Streaming, a media option is considered to have the characteristic AVMediaCharacteristicIsOriginalContent only if it’s explicitly tagged with the characteristic. See the discussion of the tagging of tracks with media characteristics below.

Also see -[AVAssetTrack hasMediaCharacteristic:] and -[AVMediaSelectionOption hasMediaCharacteristic:].


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/machinegenerated)*