# UIRectEdge

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the edges of a rectangle.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct UIRectEdge
```

```c
enum UIRectEdge : NSUInteger;
```

#### Overview

You can add these constants together to specify multiple edges at the same time.

## Topics

### Edges
- [static var top: UIRectEdge](./uirectedge/top.md)
  The top edge of the rectangle.
- [static var left: UIRectEdge](./uirectedge/left.md)
  The left edge of the rectangle.
- [static var bottom: UIRectEdge](./uirectedge/bottom.md)
  The bottom edge of the rectangle.
- [static var right: UIRectEdge](./uirectedge/right.md)
  The right edge of the rectangle.
- [static var all: UIRectEdge](./uirectedge/all.md)
  All edges of the rectangle.
### Initializers
- [init(rawValue: UInt)](./uirectedge/init%28rawvalue%29.md)
  Creates an edges structure with the specified raw value.

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

## See Also

### Specifying the starting edges
- [var edges: UIRectEdge](./uiscreenedgepangesturerecognizer/edges.md)
  The acceptable starting edges for the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectedge)*