# AVMediaPresentationSetting

**Framework**: AVFoundation  
**Kind**: class

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.

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
class AVMediaPresentationSetting
```

#### Overview

Each selectable setting is associated with a media characteristic that one or more of the AVMediaSelectionOptions in the AVMediaSelectionGroup possesses. By selecting a setting in a user interface that offers AVMediaPresentationSettings, users are essentially indicating a preference for the media characteristic of the selected setting. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Instance Properties
- [var mediaCharacteristic: AVMediaCharacteristic](avmediapresentationsetting/mediacharacteristic.md)
  Provides the media characteristic that corresponds to the selectable setting.
### Instance Methods
- [func displayName(forLocaleIdentifier: String) -> String](avmediapresentationsetting/displayname(forlocaleidentifier:).md)
  Returns the display name for the selectable setting that best matches the specified locale identifier.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediapresentationsetting)*