# CPListImageRowItemCondensedElement.Shape

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Shapes you can apply to an element’s image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum Shape
```

```c
enum CPListImageRowItemCondensedElementShape : NSInteger;
```

## Overview

When creating a condensed row element, use the constants in this type to specify the shape to apply to the image in each element.

## Topics

### Enumeration Cases
- [CPListImageRowItemCondensedElement.Shape.circular](./shape/circular.md)
  A circular shape for the element’s image.
- [CPListImageRowItemCondensedElement.Shape.roundedRectangle](./shape/roundedrectangle.md)
  A rounded rectangle shape for the element’s image.
### Initializers
- [init?(rawValue: Int)](./shape/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the element’s shape
- [var imageShape: CPListImageRowItemCondensedElement.Shape](./imageshape.md)
  The shape to apply to the current element’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement/shape)*