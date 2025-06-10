# AVCustomMediaSelectionScheme

**Framework**: AVFoundation  
**Kind**: class

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.

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
class AVCustomMediaSelectionScheme
```

#### Overview

Each selectable setting is associated with a media characteristic that one or more of the AVMediaSelectionOptions in the AVMediaSelectionGroup possesses. By selecting a setting in a user interface based on an AVCustomMediaSelectionScheme, users are essentially indicating a preference for the media characteristic of the selected setting. Selection of a specific AVMediaSelectionOption in the AVMediaSelectionGroup is then derived from the user’s indicated preferences. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Instance Properties
- [var availableLanguages: [String]](avcustommediaselectionscheme/availablelanguages.md)
  Provides available language choices.
- [var selectors: [AVMediaPresentationSelector]](avcustommediaselectionscheme/selectors.md)
  Provides custom settings.
- [var shouldOfferLanguageSelection: Bool](avcustommediaselectionscheme/shouldofferlanguageselection.md)
  Indicates whether an alternative selection interface should provide a menu of language choices.
### Instance Methods
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcustommediaselectionscheme)*