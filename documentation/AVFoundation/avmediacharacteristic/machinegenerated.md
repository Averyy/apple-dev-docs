# machineGenerated

**Framework**: AVFoundation  
**Kind**: property

A media characteristic that indicates that a track was generated in an automated fashion by a machine.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static let machineGenerated: AVMediaCharacteristic
```

#### Discussion

This media characteristic can be used to distinguish machine generated content from human authored content. The value of this characteristic is @“public.machine-generated”.

Note for content authors: for QuickTime movie and .m4v files and for HTTP Live Streaming, a media option is considered to have the characteristic AVMediaCharacteristicIsOriginalContent only if it’s explicitly tagged with the characteristic. See the discussion of the tagging of tracks with media characteristics below.

Also see -[AVAssetTrack hasMediaCharacteristic:] and -[AVMediaSelectionOption hasMediaCharacteristic:].

## See Also

- [static let isOriginalContent: AVMediaCharacteristic](avmediacharacteristic/isoriginalcontent.md)
  A media characteristic that indicates that a track or media selection option contains original content.
- [static let isMainProgramContent: AVMediaCharacteristic](avmediacharacteristic/ismainprogramcontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [static let isAuxiliaryContent: AVMediaCharacteristic](avmediacharacteristic/isauxiliarycontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/machinegenerated)*