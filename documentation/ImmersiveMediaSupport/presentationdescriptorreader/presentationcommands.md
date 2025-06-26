# presentationCommands

**Framework**: Immersive Media Support  
**Kind**: property

All the presentationCommands active for the PTS specified in the last call to `update(presentationTimeStamp:)`

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var presentationCommands: [PresentationCommand] { get }
```

## See Also

- [var cameraID: String?](presentationdescriptorreader/cameraid.md)
  The current camera ID string of the ImmersiveCamera that needs to be rendered during playback for the PTS specified in the last call to `update(presentationTimeStamp:)`
- [var colorFade: simd_float3](presentationdescriptorreader/colorfade.md)
  The current fade color for color fading of the video frames during playback for the PTS specified in the last call to `update(presentationTimeStamp:)`
- [var colorFadeOpacity: Float](presentationdescriptorreader/colorfadeopacity.md)
  The current color fade opacity of the video frames during playback for the PTS specified in the last call to `update(presentationTimeStamp:)`
- [var environmentFadeOpacity: Float](presentationdescriptorreader/environmentfadeopacity.md)
  The current opacity of the environment backdrops during playback for the PTS specified in the last call to `update(presentationTimeStamp:)`
- [var isShotFlopped: Bool](presentationdescriptorreader/isshotflopped.md)
  A Boolean value that indicates whether the video frame needs to be shot flopped (Horizontally flipped) for the PTS specified in the last call to `update(presentationTimeStamp:)`
- [var isSideloaded: Bool](presentationdescriptorreader/issideloaded.md)
  A Boolean value that indicates whether the reader input is sideloaded or is it set during playback.
- [var presentationDescriptor: PresentationDescriptor](presentationdescriptorreader/presentationdescriptor.md)
  The presentationDescriptor containing all the presentation commands that need to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/presentationcommands)*