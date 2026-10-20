# ImageCreator.Error

**Framework**: Image Playground  
**Kind**: enum  
**Role**: Enumeration

Errors that can occur during the image generation process.

**Availability**:
- iOS 18.4+ - Deprecated in 27.0
- iPadOS 18.4+ - Deprecated in 27.0
- Mac Catalyst 18.4+ - Deprecated in 27.0
- macOS 15.4+ - Deprecated in 27.0
- visionOS 2.4+ - Deprecated in 27.0

## Declaration

```swift
enum Error
```

## Topics

### Getting the error codes
- [ImageCreator.Error.notSupported](./error/notsupported.md)
  An error that indicates the device doesn’t support image generation.
- [ImageCreator.Error.unavailable](./error/unavailable.md)
  An error that indicates image creation is currently unavailable.
- [ImageCreator.Error.creationCancelled](./error/creationcancelled.md)
  An error that occurs in response to cancellation of the parent task.
- [ImageCreator.Error.faceInImageTooSmall](./error/faceinimagetoosmall.md)
  An error that indicates the system cannot use one of the source images because the face in it is too small.
- [ImageCreator.Error.unsupportedLanguage](./error/unsupportedlanguage.md)
  An error that indicates the input text uses an unsupported language.
- [ImageCreator.Error.unsupportedInputImage](./error/unsupportedinputimage.md)
  An error that indicates the system cannot use one of the specified source images.
- [ImageCreator.Error.backgroundCreationForbidden](./error/backgroundcreationforbidden.md)
  An error that indicates the app is hidden or in the background.
- [ImageCreator.Error.creationFailed](./error/creationfailed.md)
  An error that indicates a general failure occurred during image creation.
### Enumeration Cases
- [ImageCreator.Error.conceptsRequirePersonIdentity](./error/conceptsrequirepersonidentity.md)
  An error that indicates that a source image containing a person’s face needs to be added in order to complete the request.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomNSError](../../Foundation/customnserror.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Generating images
- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](./images%28for,style,limit%29.md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](./availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.CreatedImage](./createdimage.md)
  A structure that stores a programmatically generated image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/error)*