# CNRenderingSession.FrameAttributes

**Framework**: Cinematic  
**Kind**: struct

Controls the focus distance and aperture of the rendering for the frames.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct FrameAttributes
```

## Topics

### Initializers
- [init?(sampleBuffer: CMSampleBuffer, sessionAttributes: CNRenderingSession.Attributes)](cnrenderingsession-1hzh8/frameattributes/init(samplebuffer:sessionattributes:).md)
  Creates a structure representing a Cinematic rendering session based a sample buffer and session attributes.
- [init?(timedMetadataGroup: AVTimedMetadataGroup, sessionAttributes: CNRenderingSession.Attributes)](cnrenderingsession-1hzh8/frameattributes/init(timedmetadatagroup:sessionattributes:).md)
  Creates a structure representing a Cinematic rendering session based on meta group and session attributes.
### Instance Properties
- [var fNumber: Float](cnrenderingsession-1hzh8/frameattributes/fnumber.md)
  The f-stop value that inversely affects the aperture used to render the Cinematic image.
- [var focusDisparity: Float](cnrenderingsession-1hzh8/frameattributes/focusdisparity.md)
  Represents the focus plane at which the rendered image should be in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/frameattributes)*