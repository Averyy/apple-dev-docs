# ImageCreator.Error.unavailable

**Framework**: Image Playground  
**Kind**: case

An error that indicates image creation is currently unavailable.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
case unavailable
```

#### Discussion

This error can occur if the device doesn’t yet have the models it needs to complete the request.

## See Also

- [ImageCreator.Error.notSupported](imagecreator/error/notsupported.md)
  An error that indicates the device doesn’t support image generation.
- [ImageCreator.Error.creationCancelled](imagecreator/error/creationcancelled.md)
  An error that occurs in response to cancellation of the parent task.
- [ImageCreator.Error.faceInImageTooSmall](imagecreator/error/faceinimagetoosmall.md)
  An error that indicates the system cannot use one of the source images because the face in it is too small.
- [ImageCreator.Error.unsupportedLanguage](imagecreator/error/unsupportedlanguage.md)
  An error that indicates the input text uses an unsupported language.
- [ImageCreator.Error.unsupportedInputImage](imagecreator/error/unsupportedinputimage.md)
  An error that indicates the system cannot use one of the specified source images.
- [ImageCreator.Error.backgroundCreationForbidden](imagecreator/error/backgroundcreationforbidden.md)
  An error that indicates the app is hidden or in the background.
- [ImageCreator.Error.creationFailed](imagecreator/error/creationfailed.md)
  An error that indicates a general failure occurred during image creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/error/unavailable)*