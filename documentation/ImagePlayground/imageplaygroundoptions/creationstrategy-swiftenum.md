# ImagePlaygroundOptions.CreationStrategy

**Framework**: Image Playground  
**Kind**: enum

Options that specify the system strategy for preserving the original image content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum CreationStrategy
```

#### Overview

Use these options to specify how much you want the system to preserve the original image you provide.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.CreationStrategy.automatic](imageplaygroundoptions/creationstrategy-swift.enum/automatic.md)
  An option to let the system select the creation strategy.
- [ImagePlaygroundOptions.CreationStrategy.editExisting](imageplaygroundoptions/creationstrategy-swift.enum/editexisting.md)
  An option to create an image that more closely resembles the original image, but also has the modifications you specify.
- [ImagePlaygroundOptions.CreationStrategy.generateNew](imageplaygroundoptions/creationstrategy-swift.enum/generatenew.md)
  An option to create a brand new image, driven primarily by the specified concepts and loosely inspired by the input image.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationstrategy-swift.enum)*