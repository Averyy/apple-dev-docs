# AVCustomMediaSelectionScheme

**Framework**: AVFoundation  
**Kind**: class

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.

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
class AVCustomMediaSelectionScheme
```

#### Overview

Each selectable setting is associated with a media characteristic that one or more of the AVMediaSelectionOptions in the AVMediaSelectionGroup possesses. By selecting a setting in a user interface based on an AVCustomMediaSelectionScheme, users are essentially indicating a preference for the media characteristic of the selected setting. Selection of a specific AVMediaSelectionOption in the AVMediaSelectionGroup is then derived from the user’s indicated preferences. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Inspecting the scheme
- [var availableLanguages: [String]](avcustommediaselectionscheme/availablelanguages.md)
  Provides available language choices.
- [var selectors: [AVMediaPresentationSelector]](avcustommediaselectionscheme/selectors.md)
  Provides custom settings.
- [var shouldOfferLanguageSelection: Bool](avcustommediaselectionscheme/shouldofferlanguageselection.md)
  Indicates whether an alternative selection interface should provide a menu of language choices.
- [func mediaPresentationSettings(for: AVMediaPresentationSelector, complementaryToLanguage: String?, settings: [AVMediaPresentationSetting]) -> [AVMediaPresentationSetting]](avcustommediaselectionscheme/mediapresentationsettings(for:complementarytolanguage:settings:).md)
  Provides an array of media presentation settings that can be effective at the same time as the specified language and settings for other selectors of the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Selecting subtitles and alternative audio tracks](selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelection](avmediaselection.md)
  An object that represents a complete rendition of media selection options on an asset.
- [class AVMediaSelectionGroup](avmediaselectiongroup.md)
  An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [class AVMediaSelectionOption](avmediaselectionoption.md)
  An object that represents a specific option for the presentation of media within a group of options.
- [class AVMutableMediaSelection](avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.
- [class AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md)
  An object that specifies the preferred languages and media characteristics for a player.
- [class AVMediaPresentationSelector](avmediapresentationselector.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [class AVMediaPresentationSetting](avmediapresentationsetting.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme)*