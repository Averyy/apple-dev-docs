# quickTimeMetadataKeyFullFrameRatePlaybackIntent

**Framework**: AVFoundation  
**Kind**: property

An key that represents whether this movie should play at full frame rate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static let quickTimeMetadataKeyFullFrameRatePlaybackIntent: AVMetadataKey
```

#### Discussion

Some apps play movies recorded at frame rates of 120fps or higher in slow motion. If your app records high-frame-rate movies, you can add this movie-level metadata to indicate whether the movie intends to play at the full frame rate (1) or at a slow motion rate (0). Apps that play movies may use this metadata, when present, to guide their behavior.

## See Also

- [static let quickTimeMetadataKeyAccessibilityDescription: AVMetadataKey](avmetadatakey/quicktimemetadatakeyaccessibilitydescription.md)
  A key that represents the accessibility description for the movie file content.
- [static let quickTimeMetadataKeyAlbum: AVMetadataKey](avmetadatakey/quicktimemetadatakeyalbum.md)
  A key that represents the name of the album or collection in QuickTime.
- [static let quickTimeMetadataKeyArranger: AVMetadataKey](avmetadatakey/quicktimemetadatakeyarranger.md)
  A key that represents the name of the arranger of the movie file content.
- [static let quickTimeMetadataKeyArtist: AVMetadataKey](avmetadatakey/quicktimemetadatakeyartist.md)
  A key that represents the name of the artist of the movie file content.
- [static let quickTimeMetadataKeyArtwork: AVMetadataKey](avmetadatakey/quicktimemetadatakeyartwork.md)
  A key that represents an image relating to the movie file content.
- [static let quickTimeMetadataKeyAuthor: AVMetadataKey](avmetadatakey/quicktimemetadatakeyauthor.md)
  A key that represents the name of the author of the movie file content.
- [static let quickTimeMetadataKeyCameraFrameReadoutTime: AVMetadataKey](avmetadatakey/quicktimemetadatakeycameraframereadouttime.md)
  A key that represents the camera frame readout time in QuickTime.
- [static let quickTimeMetadataKeyCameraIdentifier: AVMetadataKey](avmetadatakey/quicktimemetadatakeycameraidentifier.md)
  A key that represents the camera identifier in QuickTime.
- [static let quickTimeMetadataKeyCollectionUser: AVMetadataKey](avmetadatakey/quicktimemetadatakeycollectionuser.md)
  A key that represents a name that indicates a user-defined collection.
- [static let quickTimeMetadataKeyComment: AVMetadataKey](avmetadatakey/quicktimemetadatakeycomment.md)
  A key that represents a comment regarding the movie file content.
- [static let quickTimeMetadataKeyComposer: AVMetadataKey](avmetadatakey/quicktimemetadatakeycomposer.md)
  A key that represents the name of the composer of the movie file content.
- [static let quickTimeMetadataKeyContentIdentifier: AVMetadataKey](avmetadatakey/quicktimemetadatakeycontentidentifier.md)
  A key that represents the content identifier in QuickTime.
- [static let quickTimeMetadataKeyCopyright: AVMetadataKey](avmetadatakey/quicktimemetadatakeycopyright.md)
  A key that represents the copyright statement for the movie file content.
- [static let quickTimeMetadataKeyCreationDate: AVMetadataKey](avmetadatakey/quicktimemetadatakeycreationdate.md)
  A key that represents the creation date of the movie file content.
- [static let quickTimeMetadataKeyCredits: AVMetadataKey](avmetadatakey/quicktimemetadatakeycredits.md)
  A key that represents the credits of the movie source content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatakey/quicktimemetadatakeyfullframerateplaybackintent)*