# CGSize

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains width and height values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CGSize
```

#### Overview

A [`CGSize`](cgsize.md) structure is sometimes used to represent a distance vector, rather than a physical size. As a vector, its values can be negative. To normalize a [`CGRect`](cgrect.md) structure so that its size is represented by positive values, call the [`standardized`](cgrect/standardized.md) function.

## Topics

### Geometric Properties
- [var width: Double](cgsize/width.md)
  A width value.
- [var height: Double](cgsize/height.md)
  A height value.
### Special Values
- [static var zero: CGSize](cgsize/zero.md)
- [init()](cgsize/init.md)
  Creates a size with zero width and height.
### Transforming Sizes
- [func applying(CGAffineTransform) -> CGSize](cgsize/applying(_:).md)
### Alternate Representations
- [var dictionaryRepresentation: CFDictionary](cgsize/dictionaryrepresentation.md)
- [init?(dictionaryRepresentation: CFDictionary)](cgsize/init(dictionaryrepresentation:).md)
- [var customPlaygroundQuickLook: PlaygroundQuickLook](cgsize/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
### Comparing Sizes
- [func CGSizeEqualToSize(CGSize, CGSize) -> Bool](../coregraphics/cgsizeequaltosize(_:_:).md)
  Returns whether two sizes are equal.
### Initializers
- [init(CVImageSize)](cgsize/init(_:).md)
  Convert `CVImageSize` to [`CGSize`](cgsize.md)
- [init(width: Double, height: Double)](cgsize/init(width:height:)-2du3k.md)
- [init(width: Double, height: Double)](cgsize/init(width:height:)-63ffm.md)
- [init(width: Int, height: Int)](cgsize/init(width:height:)-83b96.md)
### Instance Properties
- [var formattedDescription: String](cgsize/formatteddescription.md)
### Instance Methods
- [func equalTo(CGSize) -> Bool](cgsize/equalto(_:).md)

## Relationships

### Conforms To
- [Animatable](../swiftui/animatable.md)
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct CGAffineTransform](cgaffinetransform.md)
- [struct CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [struct CGFloat](cgfloat-swift.struct.md)
  The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [struct CGPoint](cgpoint.md)
- [struct CGRect](cgrect.md)
- [struct CGVector](cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgsize)*