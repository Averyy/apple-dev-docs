# AVVideoCleanApertureKey

**Framework**: AVFoundation  
**Kind**: var

A key that defines the region within the video dimension displayed during playback.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVVideoCleanApertureKey: String
```

#### Discussion

The value for this key is an instance of `NSDictionary` containing one or more of the following keys: [`AVVideoCleanApertureWidthKey`](avvideocleanaperturewidthkey.md), [`AVVideoCleanApertureHeightKey`](avvideocleanapertureheightkey.md), [`AVVideoCleanApertureHorizontalOffsetKey`](avvideocleanaperturehorizontaloffsetkey.md), or [`AVVideoCleanApertureVerticalOffsetKey`](avvideocleanapertureverticaloffsetkey.md). If no clean aperture region is specified, the playback displays the entire frame.

## See Also

- [let AVVideoCleanApertureWidthKey: String](avvideocleanaperturewidthkey.md)
  A key to access the width of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureHeightKey: String](avvideocleanapertureheightkey.md)
  A key to access the height of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureVerticalOffsetKey: String](avvideocleanapertureverticaloffsetkey.md)
  A key to access the vertical offset of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureHorizontalOffsetKey: String](avvideocleanaperturehorizontaloffsetkey.md)
  A key to access the horizontal offset of video that’s free from transition artifacts caused by signal encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocleanaperturekey)*