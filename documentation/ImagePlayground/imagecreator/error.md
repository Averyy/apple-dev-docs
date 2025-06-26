# ImageCreator.Error

**Framework**: Image Playground  
**Kind**: enum

Errors that can occur during the image generation process.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum Error
```

## Topics

### Getting the error codes
- [ImageCreator.Error.notSupported](imagecreator/error/notsupported.md)
  An error that indicates the device doesn’t support image generation.
- [ImageCreator.Error.unavailable](imagecreator/error/unavailable.md)
  An error that indicates image creation is currently unavailable.
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
### Getting error-related information
- [var errorUserInfo: [String : Any]](imagecreator/error/erroruserinfo.md)
  The user-info dictionary.
- [static var errorDomain: String](imagecreator/error/errordomain.md)
  The domain of the error.
### Operators
- [static func == (ImageCreator.Error, ImageCreator.Error) -> Bool](imagecreator/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ImageCreator.Error.promptRequiresPersonIdentity](imagecreator/error/promptrequirespersonidentity.md)
  An error that indicates that a source image containing a person’s face needs to be added in order to complete the request.
### Instance Properties
- [var hashValue: Int](imagecreator/error/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](imagecreator/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [ImageCreator.Error.AllCases](imagecreator/error/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Type Properties
- [static var allCases: [ImageCreator.Error]](imagecreator/error/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [CustomNSError Implementations](imagecreator/error/customnserror-implementations.md)
- [Equatable Implementations](imagecreator/error/equatable-implementations.md)
- [Error Implementations](imagecreator/error/error-implementations.md)
- [LocalizedError Implementations](imagecreator/error/localizederror-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func images(for: [ImagePlaygroundConcept], style: ImagePlaygroundStyle, limit: Int) -> some AsyncSequence<ImageCreator.CreatedImage, any Error>
](imagecreator/images(for:style:limit:).md)
  Starts the creation of images based on the description and style information you provide.
- [let availableStyles: [ImagePlaygroundStyle]](imagecreator/availablestyles.md)
  The set of styles you can apply to the images you create.
- [ImageCreator.CreatedImage](imagecreator/createdimage.md)
  A structure that stores a programmatically generated image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imagecreator/error)*