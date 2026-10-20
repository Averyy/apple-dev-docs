# UIDirectionalRectEdge

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify an edge or a set of edges, taking the user interface layout direction into account.

**Availability**:
- iOS 13.0+ - Deprecated in 13.0 (renamed: NSDirectionalRectEdge)
- iPadOS 13.0+ - Deprecated in 13.0 (renamed: NSDirectionalRectEdge)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSDirectionalRectEdge)
- tvOS 13.0+ - Deprecated in 13.0 (renamed: NSDirectionalRectEdge)
- watchOS 6.0+ - Deprecated in 6.0 (renamed: NSDirectionalRectEdge)

> **Deprecated**: Use [`NSDirectionalRectEdge`](./nsdirectionalrectedge.md) instead.

## Declaration

```swift
struct UIDirectionalRectEdge
```

```c
enum UIDirectionalRectEdge : NSUInteger;
```

## Topics

### Constants
- [static var top: UIDirectionalRectEdge](./uidirectionalrectedge/top.md)
  The top edge.
- [static var leading: UIDirectionalRectEdge](./uidirectionalrectedge/leading.md)
  The leading edge.
- [static var bottom: UIDirectionalRectEdge](./uidirectionalrectedge/bottom.md)
  The bottom edge.
- [static var trailing: UIDirectionalRectEdge](./uidirectionalrectedge/trailing.md)
  The trailing edge.
- [static var all: UIDirectionalRectEdge](./uidirectionalrectedge/all.md)
  All edges.
### Initializers
- [init(rawValue: UInt)](./uidirectionalrectedge/init%28rawvalue%29.md)
  Creates an edge with the specified raw value.

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

### Deprecated enumerations
- [enum UIStatusBarAnimation](./uistatusbaranimation.md)
  Constants that specify the animation of the status bar as it’s hidden or made visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidirectionalrectedge)*