# requiredMetadataObjectTypesForCinematicVideoCapture

**Framework**: AVFoundation  
**Kind**: property

The required metadata object types when Cinematic Video capture is enabled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var requiredMetadataObjectTypesForCinematicVideoCapture: [AVMetadataObject.ObjectType] { get }
```

#### Discussion

Since the Cinematic Video algorithm requires a particular set of metadata objects to function optimally, you must set your [`metadataObjectTypes`](avcapturemetadataoutput/metadataobjecttypes.md) property to this property’s returned value if you’ve set [`isCinematicVideoCaptureEnabled`](avcapturedeviceinput/iscinematicvideocaptureenabled.md) to `true` on the connected device input, otherwise an `NSInvalidArgumentException` is thrown.

## See Also

- [var availableMetadataObjectTypes: [AVMetadataObject.ObjectType]](avcapturemetadataoutput/availablemetadataobjecttypes.md)
  An array of strings identifying the types of metadata objects that can be captured.
- [var metadataObjectTypes: [AVMetadataObject.ObjectType]!](avcapturemetadataoutput/metadataobjecttypes.md)
  An array of strings identifying the types of metadata objects  to process.
- [var rectOfInterest: CGRect](avcapturemetadataoutput/rectofinterest.md)
  A rectangle of interest for limiting the search area for visual metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture)*