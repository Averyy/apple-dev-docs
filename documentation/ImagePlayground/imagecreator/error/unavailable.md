# ImageCreator.Error.unavailable

**Framework**: Image Playground  
**Kind**: case  
**Role**: Case

An error that indicates image creation is currently unavailable.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
case unavailable
```

## Discussion

This error can occur if the device doesn’t yet have the models it needs to complete the request.

## See Also

### Getting the error codes
- [ImageCreator.Error.notSupported](./notsupported.md)
  An error that indicates the device doesn’t support image generation.
- [ImageCreator.Error.creationCancelled](./creationcancelled.md)
  An error that occurs in response to cancellation of the parent task.
- [ImageCreator.Error.faceInImageTooSmall](./faceinimagetoosmall.md)
  An error that indicates the system cannot use one of the source images because the face in it is too small.
- [ImageCreator.Error.unsupportedLanguage](./unsupportedlanguage.md)
  An error that indicates the input text uses an unsupported language.
- [ImageCreator.Error.unsupportedInputImage](./unsupportedinputimage.md)
  An error that indicates the system cannot use one of the specified source images.
- [ImageCreator.Error.backgroundCreationForbidden](./backgroundcreationforbidden.md)
  An error that indicates the app is hidden or in the background.
- [ImageCreator.Error.creationFailed](./creationfailed.md)
  An error that indicates a general failure occurred during image creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/error/unavailable)*