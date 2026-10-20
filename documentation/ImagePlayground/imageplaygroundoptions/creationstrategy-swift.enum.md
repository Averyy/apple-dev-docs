# ImagePlaygroundOptions.CreationStrategy

**Framework**: Image Playground  
**Kind**: enum  
**Role**: Enumeration

Options that specify the system strategy for preserving the original image content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum CreationStrategy
```

#### Overview

Use these options to specify how much you want the system to preserve the original image you provide.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.CreationStrategy.automatic](./creationstrategy-swift.enum/automatic.md)
  An option to let the system select the creation strategy.
- [ImagePlaygroundOptions.CreationStrategy.editExisting](./creationstrategy-swift.enum/editexisting.md)
  An option to create an image that more closely resembles the original image, but also has the modifications you specify.
- [ImagePlaygroundOptions.CreationStrategy.generateNew](./creationstrategy-swift.enum/generatenew.md)
  An option to create a brand new image, driven primarily by the specified concepts and loosely inspired by the input image.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationstrategy-swift.enum)*