# quickTimeMetadataCinematicVideoIntent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A value of type `kCMMetadataBaseDataType_UInt8` indicating whether this movie is intended as a Cinematic Video (1) or not (0).

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
static let quickTimeMetadataCinematicVideoIntent: AVMetadataIdentifier
```

```c
extern AVMetadataIdentifier const AVMetadataIdentifierQuickTimeMetadataCinematicVideoIntent;
```

## Discussion

This movie-level metadata is automatically added (with a value of 1) to a movie recorded using the Cinematic Video API. Clients can override it with a value of 0 to signal that this movie is not to be treated as a Cinematic Video by Apple’s software like Photos.

## See Also

### QuickTime metadata identifiers
- [static let quickTimeMetadataAIMEData: AVMetadataIdentifier](./quicktimemetadataaimedata.md)
  A value of type kCMMetadataBaseDataType_RawData
- [static let quickTimeMetadataAccessibilityDescription: AVMetadataIdentifier](./quicktimemetadataaccessibilitydescription.md)
  An identifier that represents the accessibility description for the movie file content.
- [static let quickTimeMetadataAlbum: AVMetadataIdentifier](./quicktimemetadataalbum.md)
  An identifier that represents the name of the album or collection in QuickTime.
- [static let quickTimeMetadataArranger: AVMetadataIdentifier](./quicktimemetadataarranger.md)
  An identifier that represents the name of the arranger of the movie file content.
- [static let quickTimeMetadataArtist: AVMetadataIdentifier](./quicktimemetadataartist.md)
  An identifier that represents the name of the artist of the movie file content.
- [static let quickTimeMetadataArtwork: AVMetadataIdentifier](./quicktimemetadataartwork.md)
  An identifier that represents an image relating to the movie file content.
- [static let quickTimeMetadataAuthor: AVMetadataIdentifier](./quicktimemetadataauthor.md)
  An identifier that represents the name of the author of the movie file content.
- [static let quickTimeMetadataAutoLivePhoto: AVMetadataIdentifier](./quicktimemetadataautolivephoto.md)
  An identifier that represents whether the live photo movie used auto mode.
- [static let quickTimeMetadataCameraFocalLength35mmEquivalent: AVMetadataIdentifier](./quicktimemetadatacamerafocallength35mmequivalent.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating focal length normalized to the 35mm film equivalent value (e.g. “50.00mm”).
- [static let quickTimeMetadataCameraFrameReadoutTime: AVMetadataIdentifier](./quicktimemetadatacameraframereadouttime.md)
  An identifier that represents the camera frame readout time in QuickTime.
- [static let quickTimeMetadataCameraISOSensitivity: AVMetadataIdentifier](./quicktimemetadatacameraisosensitivity.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the sensitivity of the camera to light in terms of ISO exposure index (e.g. “800”). See SMPTE RDD 18.
- [static let quickTimeMetadataCameraIdentifier: AVMetadataIdentifier](./quicktimemetadatacameraidentifier.md)
  An identifier that represents the camera identifier in QuickTime.
- [static let quickTimeMetadataCameraLensIrisFNumber: AVMetadataIdentifier](./quicktimemetadatacameralensirisfnumber.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating measure of the amount of light transmitted through the lens. It is the focal length divided by the effective lens aperture diameter (e.g. “F2.8” or “2.8”).
- [static let quickTimeMetadataCameraLensModel: AVMetadataIdentifier](./quicktimemetadatacameralensmodel.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the lens model (e.g. “iPhone 16 Pro back camera 6.765mm f/1.78”).
- [static let quickTimeMetadataCameraShutterSpeedAngle: AVMetadataIdentifier](./quicktimemetadatacamerashutterspeedangle.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the exposure period expressed as an angle in minutes (1/60 degree) (e.g. “21600” or “360.00deg””).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacinematicvideointent)*