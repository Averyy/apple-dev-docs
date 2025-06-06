# quickTimeMetadataFullFrameRatePlaybackIntent

**Framework**: AVFoundation  
**Kind**: property

An identifier that represents whether this movie should play at full frame rate.

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
static let quickTimeMetadataFullFrameRatePlaybackIntent: AVMetadataIdentifier
```

#### Discussion

Some apps play movies recorded at frame rates of 120fps or higher in slow motion. If your app records high-frame-rate movies, you can add this movie-level metadata to indicate whether the movie intends to play at the full frame rate (1) or at a slow motion rate (0). Apps that play movies may use this metadata, when present, to guide their behavior.

## See Also

- [static let quickTimeMetadataAccessibilityDescription: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataaccessibilitydescription.md)
  An identifier that represents the accessibility description for the movie file content.
- [static let quickTimeMetadataAlbum: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataalbum.md)
  An identifier that represents the name of the album or collection in QuickTime.
- [static let quickTimeMetadataArranger: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataarranger.md)
  An identifier that represents the name of the arranger of the movie file content.
- [static let quickTimeMetadataArtist: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataartist.md)
  An identifier that represents the name of the artist of the movie file content.
- [static let quickTimeMetadataArtwork: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataartwork.md)
  An identifier that represents an image relating to the movie file content.
- [static let quickTimeMetadataAuthor: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataauthor.md)
  An identifier that represents the name of the author of the movie file content.
- [static let quickTimeMetadataAutoLivePhoto: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataautolivephoto.md)
  An identifier that represents whether the live photo movie used auto mode.
- [static let quickTimeMetadataCameraFrameReadoutTime: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameraframereadouttime.md)
  An identifier that represents the camera frame readout time in QuickTime.
- [static let quickTimeMetadataCameraIdentifier: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameraidentifier.md)
  An identifier that represents the camera identifier in QuickTime.
- [static let quickTimeMetadataCollectionUser: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacollectionuser.md)
  An identifier that represents a name that indicates a user-defined collection.
- [static let quickTimeMetadataComment: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacomment.md)
  An identifier that represents a comment regarding the movie file content.
- [static let quickTimeMetadataComposer: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacomposer.md)
  An identifier that represents the name of the composer of the movie file content.
- [static let quickTimeMetadataContentIdentifier: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacontentidentifier.md)
  An identifier that represents the content identifier in QuickTime.
- [static let quickTimeMetadataCopyright: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacopyright.md)
  An identifier that represents the copyright statement for the movie file content.
- [static let quickTimeMetadataCreationDate: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacreationdate.md)
  An identifier that represents the creation date of the movie file content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatafullframerateplaybackintent)*