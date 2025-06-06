# AVMediaSelectionOption

**Framework**: AVFoundation  
**Kind**: class

An object that represents a specific option for the presentation of media within a group of options.

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
class AVMediaSelectionOption
```

## Mentions

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)

## Topics

### Accessing Media Information
- [var mediaType: AVMediaType](avmediaselectionoption/mediatype.md)
  The media type of the media data.
- [var mediaSubTypes: [NSNumber]](avmediaselectionoption/mediasubtypes.md)
  The media sub-types of the media data associated with the option.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmediaselectionoption/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the receiver has media with the given media characteristic.
### Managing Metadata
- [var commonMetadata: [AVMetadataItem]](avmediaselectionoption/commonmetadata.md)
  An array of metadata items for each common metadata key for which a value is available.
- [var availableMetadataFormats: [String]](avmediaselectionoption/availablemetadataformats.md)
  The metadata formats that contain metadata associated with the option.
- [func metadata(forFormat: String) -> [AVMetadataItem]](avmediaselectionoption/metadata(forformat:).md)
  Returns an array of metadata items—one for each metadata item in the container of a given format.
### Determining Playability
- [var isPlayable: Bool](avmediaselectionoption/isplayable.md)
  A Boolean value that indicates whether the media selection option is playable.
### Getting the Language and Locale Settings
- [var displayName: String](avmediaselectionoption/displayname.md)
  A string suitable for display using the current system locale.
- [func displayName(with: Locale) -> String](avmediaselectionoption/displayname(with:).md)
  Returns a string suitable for display using the specified locale.
- [var locale: Locale?](avmediaselectionoption/locale.md)
  The locale for which the media option was authored.
- [var extendedLanguageTag: String?](avmediaselectionoption/extendedlanguagetag.md)
  The IETF BCP 47 language tag associated with the option
### Getting the Associated Media Selection Option
- [func associatedMediaSelectionOption(in: AVMediaSelectionGroup) -> AVMediaSelectionOption?](avmediaselectionoption/associatedmediaselectionoption(in:).md)
  Returns a media selection option associated with the receiver in a given group.
### Creating a Now Playing Language Option
- [func makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption?](avmediaselectionoption/makenowplayinginfolanguageoption.md)
  Creates a language option for a media selection option.
### Creating a Property List Representation
- [func propertyList() -> Any](avmediaselectionoption/propertylist.md)
  Returns a serializable property list that’s sufficient to identify the option within its group.

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

## See Also

- [Selecting Subtitles and Alternative Audio Tracks](selecting-subtitles-and-alternative-audio-tracks.md)
  Extend your app’s appeal to users by adding subtitles and alternative audio tracks in their native language.
- [class AVMediaSelection](avmediaselection.md)
  An object that represents a complete rendition of media selection options on an asset.
- [class AVMediaSelectionGroup](avmediaselectiongroup.md)
  An object that represents a collection of mutually exclusive options for the presentation of media within an asset.
- [class AVMutableMediaSelection](avmutablemediaselection.md)
  A mutable object that represents a complete rendition of media selection options on an asset.
- [class AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md)
  An object that specifies the preferred languages and media characteristics for a player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption)*