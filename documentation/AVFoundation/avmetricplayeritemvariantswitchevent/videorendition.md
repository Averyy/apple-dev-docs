# videoRendition

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Represents the currently selected video rendition’s identifiers.

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
var videoRendition: AVMetricMediaRendition { get }
```

```objc
@property (readonly) AVMetricMediaRendition * videoRendition;
```

## Discussion

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## See Also

### Inspecting the event
- [var didSucceed: Bool](./didsucceed.md)
- [var fromVariant: AVAssetVariant?](./fromvariant.md)
- [var loadedTimeRanges: [CMTimeRange]](./loadedtimeranges-5lkmg.md)
- [var toVariant: AVAssetVariant](./tovariant.md)
- [var audioRendition: AVMetricMediaRendition](./audiorendition.md)
  Represents the currently selected video rendition’s identifiers.
- [var subtitleRendition: AVMetricMediaRendition](./subtitlerendition.md)
  Represents the currently selected audio rendition’s identifiers.
- [loadedTimeRanges](./loadedtimeranges-4rhjw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplayeritemvariantswitchevent/videorendition)*