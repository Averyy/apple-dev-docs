# AVMediaSelectionGroup

**Framework**: AVFoundation  
**Kind**: class

An object that represents a collection of mutually exclusive options for the presentation of media within an asset.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVMediaSelectionGroup
```

## Mentions

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

## Topics

### Accessing Media Selection Options
- [var options: [AVMediaSelectionOption]](avmediaselectiongroup/options.md)
  A collection of mutually exclusive media selection options
- [func mediaSelectionOption(withPropertyList: Any) -> AVMediaSelectionOption?](avmediaselectiongroup/mediaselectionoption(withpropertylist:).md)
  Returns the media selection options that match the given property list.
- [var defaultOption: AVMediaSelectionOption?](avmediaselectiongroup/defaultoption.md)
  The default option in the group.
### Configuring Empty Selection Behavior
- [var allowsEmptySelection: Bool](avmediaselectiongroup/allowsemptyselection.md)
  A Boolean value that indicates whether it’s possible to present none of the options in the group when an associated player item is played.
### Filtering Selection Options
- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](avmediaselectiongroup/playablemediaselectionoptions(from:).md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:with:).md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:withoutmediacharacteristics:).md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](avmediaselectiongroup/mediaselectionoptions(from:filteredandsortedaccordingtopreferredlanguages:).md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
### Creating a Now Playing Language Option Group
- [func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup](avmediaselectiongroup/makenowplayinginfolanguageoptiongroup.md)
  Creates a language option group from the media selection group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAssetWriterInputGroup](avassetwriterinputgroup.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelection](avmediaselection.md)
  An object that represents a complete rendition of media selection options on an asset.
- [class AVMediaSelectionOption](avmediaselectionoption.md)
  An object that represents a specific option for the presentation of media within a group of options.
- [class AVMutableMediaSelection](avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.
- [class AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md)
  An object that specifies the preferred languages and media characteristics for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)*