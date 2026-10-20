# requiredMetadataObjectTypesForCinematicVideoCapture

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<NSString *> * requiredMetadataObjectTypesForCinematicVideoCapture;
```

#### Discussion

Since the Cinematic Video algorithm requires a particular set of metadata objects to function optimally, you must set your [`metadataObjectTypes`](./metadataobjecttypes.md) property to this property’s returned value if you’ve set [`isCinematicVideoCaptureEnabled`](../avcapturedeviceinput/iscinematicvideocaptureenabled.md) to `true` on the connected device input, otherwise an `NSInvalidArgumentException` is thrown.

## See Also

### Configuring metadata capture
- [var availableMetadataObjectTypes: [AVMetadataObject.ObjectType]](./availablemetadataobjecttypes.md)
  An array of strings identifying the types of metadata objects that can be captured.
- [var metadataObjectTypes: [AVMetadataObject.ObjectType]!](./metadataobjecttypes.md)
  An array of strings identifying the types of metadata objects  to process.
- [var rectOfInterest: CGRect](./rectofinterest.md)
  A rectangle of interest for limiting the search area for visual metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture)*