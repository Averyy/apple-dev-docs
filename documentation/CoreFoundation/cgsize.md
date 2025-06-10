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

A [`CGSize`](cgsize.md) structure is sometimes used to represent a distance vector, rather than a physical size. As a vector, its values can be negative. To normalize a [`CGRect`](cgrect.md) structure so that its size is represented by positive values, call the [`standardized`](CGRect/standardized.md) function.

## Topics

### Geometric Properties
- [var width: Double](cgsize/width.md)
  A width value.
- [var height: Double](cgsize/height.md)
  A height value.
### Special Values
- [static var zero: CGSize { get }](CGSize/zero.md)
- [init()](cgsize/init.md)
  Creates a size with zero width and height.
### Transforming Sizes
- [func applying(_ t: CGAffineTransform) -> CGSize](CGSize/applying(_:).md)
### Alternate Representations
- [var dictionaryRepresentation: CFDictionary { get }](CGSize/dictionaryRepresentation.md)
- [init?(dictionaryRepresentation dict: CFDictionary)](CGSize/init(dictionaryRepresentation:).md)
- [var debugDescription: String](../coregraphics/cgsize/1645822-debugdescription.md)
  A textual representation of the size’s dimensions.
- [var customMirror: Mirror](../coregraphics/cgsize/1645828-custommirror.md)
  A representation of the size’s structure and display style for use in debugging.
- [var customPlaygroundQuickLook: PlaygroundQuickLook { get }](CGSize/customPlaygroundQuickLook.md)
  A custom playground Quick Look for this instance.
### Comparing Sizes
- [func CGSizeEqualToSize(_ size1: CGSize, _ size2: CGSize) -> Bool](../CoreGraphics/CGSizeEqualToSize(_:_:).md)
  Returns whether two sizes are equal.
### Initializers
- [init(CVImageSize)](cgsize/init(_:).md)
  Convert `CVImageSize` to [`CGSize`](cgsize.md)
- [init?(dictionaryRepresentation: CFDictionary)](cgsize/init(dictionaryrepresentation:).md)
- [init(width: Double, height: Double)](cgsize/init(width:height:)-2du3k.md)
- [init(width: Double, height: Double)](cgsize/init(width:height:)-63ffm.md)
- [init(width: Int, height: Int)](cgsize/init(width:height:)-83b96.md)
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](cgsize/customplaygroundquicklook.md)
  A custom playground Quick Look for this instance.
- [var dictionaryRepresentation: CFDictionary](cgsize/dictionaryrepresentation.md)
### Instance Methods
- [func applying(CGAffineTransform) -> CGSize](cgsize/applying(_:).md)
- [func equalTo(CGSize) -> Bool](cgsize/equalto(_:).md)
### Type Properties
- [static var zero: CGSize](cgsize/zero.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/Animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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