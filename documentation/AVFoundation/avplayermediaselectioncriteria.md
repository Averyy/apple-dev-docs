# AVPlayerMediaSelectionCriteria

**Framework**: AVFoundation  
**Kind**: class

An object that specifies the preferred languages and media characteristics for a player.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVPlayerMediaSelectionCriteria
```

#### Overview

An instance of this object represents the languages and media characteristics of assets that contain media selection options that a player attempts to select automatically when preparing and playing items. It lists the languages and media characteristics in their preferred order.

## Topics

### Creating Media Selection Criteria
- [init(preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)](avplayermediaselectioncriteria/init(preferredlanguages:preferredmediacharacteristics:).md)
  Creates media selection criteria with the preferred languages and media characteristics.
- [init(principalMediaCharacteristics: [AVMediaCharacteristic]?, preferredLanguages: [String]?, preferredMediaCharacteristics: [AVMediaCharacteristic]?)](avplayermediaselectioncriteria/init(principalmediacharacteristics:preferredlanguages:preferredmediacharacteristics:).md)
  Creates media selection criteria with the principal media characteristics, and preferred languages and media characteristics.
### Retrieving Selection Criteria Settings
- [var preferredLanguages: [String]?](avplayermediaselectioncriteria/preferredlanguages.md)
  An array of language identifiers in preferred order.
- [var preferredMediaCharacteristics: [AVMediaCharacteristic]?](avplayermediaselectioncriteria/preferredmediacharacteristics.md)
  An array of media characteristics in preferred order.
- [var principalMediaCharacteristics: [AVMediaCharacteristic]?](avplayermediaselectioncriteria/principalmediacharacteristics.md)
  An array of media characteristics that are essential to select when choosing media with a particular characteristic.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelection](avmediaselection.md)
  An object that represents a complete rendition of media selection options on an asset.
- [class AVMediaSelectionGroup](avmediaselectiongroup.md)
  An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [class AVMediaSelectionOption](avmediaselectionoption.md)
  An object that represents a specific option for the presentation of media within a group of options.
- [class AVMutableMediaSelection](avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayermediaselectioncriteria)*