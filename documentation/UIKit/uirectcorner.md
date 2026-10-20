# UIRectCorner

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The corners of a rectangle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
struct UIRectCorner
```

```c
enum UIRectCorner : NSUInteger;
```

#### Overview

The specified constants reflect the corners of a rectangle that has not been modified by an affine transform and is drawn in the default coordinate system (where the origin is in the upper-left corner and positive values extend down and to the right).

## Topics

### Constants
- [static var topLeft: UIRectCorner](./uirectcorner/topleft.md)
  The top-left corner of the rectangle.
- [static var topRight: UIRectCorner](./uirectcorner/topright.md)
  The top-right corner of the rectangle.
- [static var bottomLeft: UIRectCorner](./uirectcorner/bottomleft.md)
  The bottom-left corner of the rectangle.
- [static var bottomRight: UIRectCorner](./uirectcorner/bottomright.md)
  The bottom-right corner of the rectangle.
- [static var allCorners: UIRectCorner](./uirectcorner/allcorners.md)
  All corners of the rectangle.
### Initializer
- [init(rawValue: UInt)](./uirectcorner/init%28rawvalue%29.md)
  Creates a structure that represents the corners of a rectangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectcorner)*