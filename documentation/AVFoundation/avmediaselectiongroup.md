# AVMediaSelectionGroup

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMediaSelectionGroup : NSObject
```

## Mentions

- [Selecting subtitles and alternative audio tracks](./selecting-subtitles-and-alternative-audio-tracks.md)

## Topics

### Accessing media selection options
- [var options: [AVMediaSelectionOption]](./avmediaselectiongroup/options.md)
  A collection of mutually exclusive media selection options
- [func mediaSelectionOption(withPropertyList: Any) -> AVMediaSelectionOption?](./avmediaselectiongroup/mediaselectionoption%28withpropertylist%29.md)
  Returns the media selection options that match the given property list.
- [var defaultOption: AVMediaSelectionOption?](./avmediaselectiongroup/defaultoption.md)
  The default option in the group.
### Configuring empty selection behavior
- [var allowsEmptySelection: Bool](./avmediaselectiongroup/allowsemptyselection.md)
  A Boolean value that indicates whether it’s possible to present none of the options in the group when an associated player item is played.
### Filtering selection options
- [class func playableMediaSelectionOptions(from: [AVMediaSelectionOption]) -> [AVMediaSelectionOption]](./avmediaselectiongroup/playablemediaselectionoptions%28from%29.md)
  Returns an array containing the media selection options from a given array that are playable.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], with: Locale) -> [AVMediaSelectionOption]](./avmediaselectiongroup/mediaselectionoptions%28from,with%29.md)
  Returns an array containing the media selection options from a given array that match the specified locale.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./avmediaselectiongroup/mediaselectionoptions%28from,withmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], withoutMediaCharacteristics: [AVMediaCharacteristic]) -> [AVMediaSelectionOption]](./avmediaselectiongroup/mediaselectionoptions%28from,withoutmediacharacteristics%29.md)
  Returns an array containing the media selection options from a given array that do not match given media characteristics.
- [class func mediaSelectionOptions(from: [AVMediaSelectionOption], filteredAndSortedAccordingToPreferredLanguages: [String]) -> [AVMediaSelectionOption]](./avmediaselectiongroup/mediaselectionoptions%28from,filteredandsortedaccordingtopreferredlanguages%29.md)
  Returns an array of media selection options, filtering them according to whether their locales match one of the specified languages.
- [var customMediaSelectionScheme: AVCustomMediaSelectionScheme?](./avmediaselectiongroup/custommediaselectionscheme.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
### Creating a Now Playing language option group
- [func makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup](./avmediaselectiongroup/makenowplayinginfolanguageoptiongroup%28%29.md)
  Creates a language option group from the media selection group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVAssetWriterInputGroup](./avassetwriterinputgroup.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media selection
- [Selecting subtitles and alternative audio tracks](./selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelection](./avmediaselection.md)
  An object that represents a complete rendition of media selection options on an asset.
- [class AVMediaSelectionOption](./avmediaselectionoption.md)
  An object that represents a specific option for the presentation of media within a group of options.
- [class AVMutableMediaSelection](./avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.
- [class AVPlayerMediaSelectionCriteria](./avplayermediaselectioncriteria.md)
  An object that specifies the preferred languages and media characteristics for a player.
- [class AVCustomMediaSelectionScheme](./avcustommediaselectionscheme.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVCustomMediaSelectionScheme provides a collection of custom settings for controlling the presentation of the media.
- [class AVMediaPresentationSelector](./avmediapresentationselector.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.
- [class AVMediaPresentationSetting](./avmediapresentationsetting.md)
  For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSetting represents a selectable setting for controlling the presentation of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup)*