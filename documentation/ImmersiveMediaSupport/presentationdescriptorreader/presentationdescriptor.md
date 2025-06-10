# presentationDescriptor

**Framework**: Immersive Media Support  
**Kind**: property

The presentationDescriptor containing all the presentation commands that need to be processed.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var presentationDescriptor: PresentationDescriptor { get set }
```

## See Also

- [var cameraID: String?](presentationdescriptorreader/cameraid.md)
  The current camera ID string of the ImmersiveCamera that needs to be rendered during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var colorFade: simd_float3](presentationdescriptorreader/colorfade.md)
  The current fade color for color fading of the video frames during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var colorFadeOpacity: Float](presentationdescriptorreader/colorfadeopacity.md)
  The current color fade opacity of the video frames during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var environmentFadeOpacity: Float](presentationdescriptorreader/environmentfadeopacity.md)
  The current opacity of the environment backdrops during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var isShotFlopped: Bool](presentationdescriptorreader/isshotflopped.md)
  The flag to indicate if the video frame needs to be shot flopped (Horizontally flipped) or not for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var isSideloaded: Bool](presentationdescriptorreader/issideloaded.md)
  The flag to indicate if the reader input is sideloaded or is it set during playback.
- [var presentationCommands: [any PresentationCommand]](presentationdescriptorreader/presentationcommands.md)
  All the presentationCommands active for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/presentationdescriptor)*