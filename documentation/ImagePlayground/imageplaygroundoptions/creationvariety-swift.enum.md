# ImagePlaygroundOptions.CreationVariety

**Framework**: Image Playground  
**Kind**: enum  
**Role**: Enumeration

Options that specify how much variety to use when creating multiple images from the same concepts.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
enum CreationVariety
```

#### Overview

When you generate multiple images, use this type to specify how much to adjust the creation parameters for each image. The amount of variability determines how similar each image is to the others. These options apply only when creating multiple images at the same time.

## Topics

### Enumeration Cases
- [ImagePlaygroundOptions.CreationVariety.automatic](./creationvariety-swift.enum/automatic.md)
  An option to programmatically determine how much variety to use when creating images.
- [ImagePlaygroundOptions.CreationVariety.high](./creationvariety-swift.enum/high.md)
  An option to use a lot of variety when creating images.
- [ImagePlaygroundOptions.CreationVariety.low](./creationvariety-swift.enum/low.md)
  An option to use a low amount of variety when creating images.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions/creationvariety-swift.enum)*