# ImageCreator.Error.notSupported

**Framework**: Image Playground  
**Kind**: case  
**Role**: Case

An error that indicates the device doesn’t support image generation.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
case notSupported
```

## Discussion

Make sure the device has the hardware required to run models.

## See Also

### Getting the error codes
- [ImageCreator.Error.unavailable](./unavailable.md)
  An error that indicates image creation is currently unavailable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/error/notsupported)*