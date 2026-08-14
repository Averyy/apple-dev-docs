# ImagePlaygroundOptions

**Framework**: Image Playground  
**Kind**: struct

A type that stores the options that affect the image-generation process.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
struct ImagePlaygroundOptions
```

#### Overview

Create an instance of this structure and use it to specify the options you want to use when generating images. Apply these options to your SwiftUI sheet using the [`imagePlaygroundOptions(_:)`](https://developer.apple.com/documentation/swiftui/view/imageplaygroundoptions(_:)) modifier, or assign them to properties of the [`ImagePlaygroundViewController`](imageplaygroundviewcontroller.md) or [`ImageCreator`](imagecreator.md) type before generating any images.

## Topics

### Structures
- [ImagePlaygroundOptions.SizeSpecification](imageplaygroundoptions/sizespecification-swift.struct.md)
  A type that specifies image size and aspect ratio information.
### Initializers
- [init()](imageplaygroundoptions/init.md)
  Initializes a new instance of this structure with a default set of options.
### Instance Properties
- [var creationStrategy: ImagePlaygroundOptions.CreationStrategy](imageplaygroundoptions/creationstrategy-swift.property.md)
  The options that specify how to interpret the content in the provided input image.
- [var creationVariety: ImagePlaygroundOptions.CreationVariety](imageplaygroundoptions/creationvariety-swift.property.md)
  The amount to vary the creation parameters when generating multiple images from the same inputs.
- [var personalization: ImagePlaygroundOptions.Personalization](imageplaygroundoptions/personalization-swift.property.md)
  The option to enable or disable personalization features.
- [var sizeSpecification: ImagePlaygroundOptions.SizeSpecification](imageplaygroundoptions/sizespecification-swift.property.md)
  The requested size for any generated images.
### Enumerations
- [ImagePlaygroundOptions.CreationStrategy](imageplaygroundoptions/creationstrategy-swift.enum.md)
  Options that specify the system strategy for preserving the original image content.
- [ImagePlaygroundOptions.CreationVariety](imageplaygroundoptions/creationvariety-swift.enum.md)
  Options that specify how much variety to use when creating multiple images from the same concepts.
- [ImagePlaygroundOptions.Personalization](imageplaygroundoptions/personalization-swift.enum.md)
  Options for enabling and disabling personalization features when generating images.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions)*