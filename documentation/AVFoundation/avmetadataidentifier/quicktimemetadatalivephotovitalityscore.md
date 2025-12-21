# quickTimeMetadataLivePhotoVitalityScore

**Framework**: AVFoundation  
**Kind**: property

An identifier that represents the vitality score of the Live Photo movie.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let quickTimeMetadataLivePhotoVitalityScore: AVMetadataIdentifier
```

#### Discussion

Live Photo movies may be algorithmically scored from `0.0` to `1.0` on their level of vitality. A Live Photo movie with a low vitality score offers little dynamism to the still photo it accompanies. The vitality score is normalized and independent of the vitality scoring version of the algorithm defined by [`quickTimeMetadataLivePhotoVitalityScoringVersion`](avmetadataidentifier/quicktimemetadatalivephotovitalityscoringversion.md).

If a Live Photo movie contains the [`quickTimeMetadataAutoLivePhoto`](avmetadataidentifier/quicktimemetadataautolivephoto.md) key and its value is nonzero, apps should read the [`quickTimeMetadataLivePhotoVitalityScore`](avmetadataidentifier/quicktimemetadatalivephotovitalityscore.md) value and only display the movie’s content if the score is `0.5` or higher.

If the capture session includes a metadata output configured to provide face, dog, or cat metadata objects, their presence greatly increases the vitality score.

## See Also

- [static let quickTimeMetadataAIMEData: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadataaimedata.md)
  A value of type kCMMetadataBaseDataType_RawData
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
- [static let quickTimeMetadataCameraFocalLength35mmEquivalent: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacamerafocallength35mmequivalent.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating focal length normalized to the 35mm film equivalent value (e.g. “50.00mm”).
- [static let quickTimeMetadataCameraFrameReadoutTime: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameraframereadouttime.md)
  An identifier that represents the camera frame readout time in QuickTime.
- [static let quickTimeMetadataCameraISOSensitivity: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameraisosensitivity.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the sensitivity of the camera to light in terms of ISO exposure index (e.g. “800”). See SMPTE RDD 18.
- [static let quickTimeMetadataCameraIdentifier: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameraidentifier.md)
  An identifier that represents the camera identifier in QuickTime.
- [static let quickTimeMetadataCameraLensIrisFNumber: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameralensirisfnumber.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating measure of the amount of light transmitted through the lens. It is the focal length divided by the effective lens aperture diameter (e.g. “F2.8” or “2.8”).
- [static let quickTimeMetadataCameraLensModel: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacameralensmodel.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the lens model (e.g. “iPhone 16 Pro back camera 6.765mm f/1.78”).
- [static let quickTimeMetadataCameraShutterSpeedAngle: AVMetadataIdentifier](avmetadataidentifier/quicktimemetadatacamerashutterspeedangle.md)
  A value of type kCMMetadataBaseDataType_UTF8 indicating the exposure period expressed as an angle in minutes (1/60 degree) (e.g. “21600” or “360.00deg””).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatalivephotovitalityscore)*