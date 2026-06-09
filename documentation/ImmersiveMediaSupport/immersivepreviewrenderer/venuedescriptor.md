# venueDescriptor

**Framework**: Immersive Media Support  
**Kind**: property

The venue descriptor for rendering immersive video frames.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
var venueDescriptor: VenueDescriptor?
```

#### Discussion

The venue descriptor provides the necessary camera calibration data, mesh geometry, and masking information required to properly render immersive video frames. Update this property to switch between different venues or camera configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivepreviewrenderer/venuedescriptor)*