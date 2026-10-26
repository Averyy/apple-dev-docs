# CGSize

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

A structure that contains width and height values.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CGSize
```

```c
struct CGSize;
```

#### Overview

A [`CGSize`](./cgsize.md) structure is sometimes used to represent a distance vector, rather than a physical size. As a vector, its values can be negative. To normalize a [`CGRect`](./cgrect.md) structure so that its size is represented by positive values, call the [`standardized`](./cgrect/standardized.md) function.

## Topics

### Geometric Properties
- [var width: Double](./cgsize/width.md)
  A width value.
- [var height: Double](./cgsize/height.md)
  A height value.
### Special Values
- [static var zero: CGSize](./cgsize/zero.md)
- [init()](./cgsize/init%28%29.md)
  Creates a size with zero width and height.
### Transforming Sizes
- [func applying(CGAffineTransform) -> CGSize](./cgsize/applying%28_%29.md)
### Alternate Representations
- [var dictionaryRepresentation: CFDictionary](./cgsize/dictionaryrepresentation.md)
- [init?(dictionaryRepresentation: CFDictionary)](./cgsize/init%28dictionaryrepresentation%29.md)
- [var customPlaygroundQuickLook: PlaygroundQuickLook](./cgsize/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
### Comparing Sizes
- [func CGSizeEqualToSize(CGSize, CGSize) -> Bool](../CoreGraphics/cgsizeequaltosize%28_,_%29.md)
  Returns whether two sizes are equal.
### Initializers
- [init(CVImageSize)](./cgsize/init%28_%29.md)
  Convert `CVImageSize` to [`CGSize`](./cgsize.md)
- [init(width: Double, height: Double)](./cgsize/init%28width,height%29-2du3k.md)
- [init(width: Double, height: Double)](./cgsize/init%28width,height%29-63ffm.md)
- [init(width: Int, height: Int)](./cgsize/init%28width,height%29-83b96.md)
### Instance Properties
- [var formattedDescription: String](./cgsize/formatteddescription.md)
### Instance Methods
- [func equalTo(CGSize) -> Bool](./cgsize/equalto%28_%29.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structures
- [struct CGAffineTransform](./cgaffinetransform.md)
- [struct CGAffineTransformComponents](./cgaffinetransformcomponents.md)
- [struct CGFloat](./cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](./cgpoint.md)
- [struct CGRect](./cgrect.md)
- [struct CGVector](./cgvector.md)
  A structure that contains a two-dimensional vector.
- [IUnknownVTbl](./iunknownvtbl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgsize)*