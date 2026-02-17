# ImagePlaygroundOptions

**Framework**: Image Playground  
**Kind**: struct

A structure that stores a set of options influencing image creation.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
struct ImagePlaygroundOptions
```

#### Overview

You can create a set of options and pass it to `ImageCreator`, `ImagePlaygroundViewController`, or `SwiftUI.View.imagePlaygroundSheet`, in order to create images that satisfy those options.

## Topics

### Initializers
- [init()](imageplaygroundoptions/init.md)
  Creates a set of options with default behaviors.
### Instance Properties
- [var creationVariety: ImagePlaygroundOptions.CreationVariety](imageplaygroundoptions/creationvariety-swift.property.md)
  An option for enabling or disabling variety when creating multiple images from the same set of concepts.
- [var personalization: ImagePlaygroundOptions.Personalization](imageplaygroundoptions/personalization-swift.property.md)
  An option for enabling or disabling personalization.
### Enumerations
- [ImagePlaygroundOptions.CreationVariety](imageplaygroundoptions/creationvariety-swift.enum.md)
  An option for determining when the system should provide better variety when creating multiple images from the same set of concepts.
- [ImagePlaygroundOptions.Personalization](imageplaygroundoptions/personalization-swift.enum.md)
  An option for enabling or disabling people support in the system interface.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions)*