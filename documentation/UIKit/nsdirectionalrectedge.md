# NSDirectionalRectEdge

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify an edge or a set of edges, taking the user interface layout direction into account.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct NSDirectionalRectEdge
```

```c
enum NSDirectionalRectEdge : NSUInteger;
```

## Topics

### Constants
- [static var top: NSDirectionalRectEdge](./nsdirectionalrectedge/top.md)
  The top edge.
- [static var leading: NSDirectionalRectEdge](./nsdirectionalrectedge/leading.md)
  The leading edge.
- [static var bottom: NSDirectionalRectEdge](./nsdirectionalrectedge/bottom.md)
  The bottom edge.
- [static var trailing: NSDirectionalRectEdge](./nsdirectionalrectedge/trailing.md)
  The trailing edge.
- [static var all: NSDirectionalRectEdge](./nsdirectionalrectedge/all.md)
  All edges.
- [NSDirectionalRectEdgeNone](./nsdirectionalrectedge/nsdirectionalrectedgenone.md)
  No specified edge.
### Initializers
- [init(rawValue: UInt)](./nsdirectionalrectedge/init%28rawvalue%29.md)
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

### Related types
- [struct UIOffset](./uioffset.md)
  A structure that specifies an amount to offset a position.
- [struct UIAxis](./uiaxis.md)
  A structure that specifies the layout axes.
- [struct UIEdgeInsets](./uiedgeinsets.md)
  The inset distances for views.
- [struct NSDirectionalEdgeInsets](./nsdirectionaledgeinsets.md)
  The inset distances for views, taking the user interface layout direction into account.
- [enum NSRectAlignment](./nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](./uikit-macros.md)
  Macros that UIKit defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdirectionalrectedge)*