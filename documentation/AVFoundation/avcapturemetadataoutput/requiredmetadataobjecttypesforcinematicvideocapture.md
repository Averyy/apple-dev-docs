# requiredMetadataObjectTypesForCinematicVideoCapture

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var requiredMetadataObjectTypesForCinematicVideoCapture: [AVMetadataObject.ObjectType] { get }
```

#### Discussion

Indicates the required metadata object types when Cinematic Video capture is enabled.

Since the Cinematic Video algorithm requires a particular set of metadata objects to function optimally, you must set your `metadataObjectTypes` property to this property’s returned value if you’ve set `cinematicVideoCaptureEnabled` to YES on the connected device input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/requiredmetadataobjecttypesforcinematicvideocapture)*