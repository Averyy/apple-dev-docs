# default

**Framework**: AVFoundation  
**Kind**: property

The text styling information is the same level of information that AVFoundation uses within a player layer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let `default`: AVPlayerItemLegibleOutput.TextStylingResolution
```

#### Discussion

Specify this level of text styling resolution to receive attributed strings from an `AVPlayerItemLegibleOutput` that include the same level of styling information that AVFoundation would use itself to render text within an [`AVPlayerLayer`](avplayerlayer.md). The text styling will accommodate user-level Media Accessibility settings.

## See Also

- [static let sourceAndRulesOnly: AVPlayerItemLegibleOutput.TextStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.struct/sourceandrulesonly.md)
  The level of resolution excludes styling provided by the user-level Media Accessibility settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct/default)*