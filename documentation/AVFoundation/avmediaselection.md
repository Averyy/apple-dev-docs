# AVMediaSelection

**Framework**: AVFoundation  
**Kind**: class

An object that represents a complete rendition of media selection options on an asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVMediaSelection
```

## Topics

### Inspecting the media selection
- [func selectedMediaOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](avmediaselection/selectedmediaoption(in:).md)
  Returns the media selection option that’s currently selected in the specified group.
- [func mediaSelectionCriteriaCanBeAppliedAutomatically(to: AVMediaSelectionGroup) -> Bool](avmediaselection/mediaselectioncriteriacanbeappliedautomatically(to:).md)
  Indicates whether the specified media selection group is subject to automatic media selection.
### Accessing the asset
- [var asset: AVAsset?](avmediaselection/asset.md)
  The asset associated with the media selection.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableMediaSelection](avmutablemediaselection.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelectionGroup](avmediaselectiongroup.md)
  An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [class AVMediaSelectionOption](avmediaselectionoption.md)
  An object that represents a specific option for the presentation of media within a group of options.
- [class AVMutableMediaSelection](avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.
- [class AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md)
  An object that specifies the preferred languages and media characteristics for a player.
- [class AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [class AVMediaPresentationSelector](avmediapresentationselector.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [class AVMediaPresentationSetting](avmediapresentationsetting.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselection)*