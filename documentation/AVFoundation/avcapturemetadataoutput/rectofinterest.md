# rectOfInterest

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A rectangle of interest for limiting the search area for visual metadata.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var rectOfInterest: CGRect { get set }
```

```objc
@property (nonatomic) CGRect rectOfInterest;
```

#### Discussion

The value of this property is a [`CGRect`](../../CoreFoundation/cgrect.md) value that determines the object’s rectangle of interest for each frame of video.

The rectangle’s origin is top left and is relative to the coordinate space of the device providing the metadata.

Specifying a rectangle of interest may improve detection performance for certain types of metadata.  Metadata objects whose bounds do not intersect with the `rectOfInterest` will not be returned.

The default value of this property is a rectangle of `(0.0, 0.0, 1.0, 1.0)`.

## See Also

### Configuring metadata capture
- [var availableMetadataObjectTypes: [AVMetadataObject.ObjectType]](./availablemetadataobjecttypes.md)
  An array of strings identifying the types of metadata objects that can be captured.
- [var metadataObjectTypes: [AVMetadataObject.ObjectType]!](./metadataobjecttypes.md)
  An array of strings identifying the types of metadata objects  to process.
- [var requiredMetadataObjectTypesForCinematicVideoCapture: [AVMetadataObject.ObjectType]](./requiredmetadataobjecttypesforcinematicvideocapture.md)
  The required metadata object types when Cinematic Video capture is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/rectofinterest)*