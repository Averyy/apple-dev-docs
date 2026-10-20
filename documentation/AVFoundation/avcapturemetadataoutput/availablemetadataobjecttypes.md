# availableMetadataObjectTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of strings identifying the types of metadata objects that can be captured.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var availableMetadataObjectTypes: [AVMetadataObject.ObjectType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableMetadataObjectTypes;
```

#### Discussion

Each string in the array corresponds to a possible value in the [`type`](../avmetadataobject/type.md) property of the [`AVMetadataObject`](../avmetadataobject.md) objects reported by the receiver. The available types are dependent on the capabilities of the [`AVCaptureInput.Port`](../avcaptureinput/port.md) to which the receiver’s connection is attached.

## See Also

### Configuring metadata capture
- [var metadataObjectTypes: [AVMetadataObject.ObjectType]!](./metadataobjecttypes.md)
  An array of strings identifying the types of metadata objects  to process.
- [var rectOfInterest: CGRect](./rectofinterest.md)
  A rectangle of interest for limiting the search area for visual metadata.
- [var requiredMetadataObjectTypesForCinematicVideoCapture: [AVMetadataObject.ObjectType]](./requiredmetadataobjecttypesforcinematicvideocapture.md)
  The required metadata object types when Cinematic Video capture is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/availablemetadataobjecttypes)*