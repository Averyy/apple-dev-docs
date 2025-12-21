# isSideloaded

**Framework**: Immersive Media Support  
**Kind**: property

A Boolean value that indicates whether the reader input is sideloaded or is it set during playback.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var isSideloaded: Bool { get }
```

## See Also

- [var cameraID: String?](presentationdescriptorreader/cameraid.md)
  The current camera ID string of the immersive camera to use when rendering playback for the PTS specified in the last call to the update method.
- [var colorFade: simd_float3](presentationdescriptorreader/colorfade.md)
  The current fade color for color fading of the video frames during playback for the PTS specified in the last call to the update method.
- [var colorFadeOpacity: Float](presentationdescriptorreader/colorfadeopacity.md)
  The current color fade opacity of the video frames during playback for the PTS specified in the last call to the update method.
- [var environmentFadeOpacity: Float](presentationdescriptorreader/environmentfadeopacity.md)
  The current opacity of the environment backdrops during playback for the PTS specified in the last call to the update method.
- [var isShotFlopped: Bool](presentationdescriptorreader/isshotflopped.md)
  A Boolean value that indicates whether to horizontally flip the video frame for the PTS specified in the last call to the update method.
- [var presentationCommands: [PresentationCommand]](presentationdescriptorreader/presentationcommands.md)
  The active presentation commands for the PTS specified in the last call to the update method.
- [var presentationDescriptor: PresentationDescriptor](presentationdescriptorreader/presentationdescriptor.md)
  The presentation descriptor that contains the presentation commands to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/issideloaded)*