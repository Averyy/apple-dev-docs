# UIAxis

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A structure that specifies the layout axes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
struct UIAxis
```

```c
enum UIAxis : NSUInteger;
```

## Topics

### Constants
- [static var horizontal: UIAxis](./uiaxis/horizontal.md)
  A value that represents the horizontal axis.
- [static var vertical: UIAxis](./uiaxis/vertical.md)
  A value that represents the vertical axis.
- [static var both: UIAxis](./uiaxis/both.md)
  A value that represents both axes.
### Initializers
- [init(rawValue: UInt)](./uiaxis/init%28rawvalue%29.md)
  Creates an axis with the specified raw value.
- [UIAxisNeither](./uiaxis/uiaxisneither.md)
  A value that represents neither axis.

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
- [struct UIEdgeInsets](./uiedgeinsets.md)
  The inset distances for views.
- [struct NSDirectionalEdgeInsets](./nsdirectionaledgeinsets.md)
  The inset distances for views, taking the user interface layout direction into account.
- [struct NSDirectionalRectEdge](./nsdirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [enum NSRectAlignment](./nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](./uikit-macros.md)
  Macros that UIKit defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaxis)*