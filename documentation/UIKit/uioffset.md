# UIOffset

**Framework**: UIKit  
**Kind**: struct

A structure that specifies an amount to offset a position.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
struct UIOffset
```

#### Overview

The components are positive for right or down, negative for left or up.

See also [`Initializing offsets`](uioffset#Initializing-offsets.md) and [`zero`](uioffset/zero.md).

## Topics

### Initializing offsets
- [init(horizontal: CGFloat, vertical: CGFloat)](uioffset/init(horizontal:vertical:)-9wl8x.md)
  Creates an offset structure from the given components.
- [init()](uioffset/init.md)
  Creates an offset structure.
### Getting the offset values
- [var horizontal: CGFloat](uioffset/horizontal.md)
  The amount of horizontal offset from a position.
- [var vertical: CGFloat](uioffset/vertical.md)
  The amount of vertical offset from a position.
### Comparing offsets
- [func UIOffsetEqualToOffset(UIOffset, UIOffset) -> Bool](uioffsetequaltooffset(_:_:).md)
  Returns a Boolean value that indicates whether two offsets are equal.
### Converting to and from strings
- [class func string(for offset: UIOffset) -> String](../Foundation/NSCoder/string(for:)-454dj.md)
  Returns a string formatted to contain the data from an offset structure.
- [class func uiOffset(for string: String) -> UIOffset](../Foundation/NSCoder/uiOffset(for:).md)
  Returns a UIKit offset structure corresponding to the data in a given string.
### Getting the empty offset value
- [static let zero: UIOffset](uioffset/zero.md)
  An offset structure with no offset in the horizontal and vertical directions.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct UIAxis](uiaxis.md)
  A structure that specifies the layout axes.
- [struct UIEdgeInsets](uiedgeinsets.md)
  The inset distances for views.
- [struct NSDirectionalEdgeInsets](nsdirectionaledgeinsets.md)
  The inset distances for views, taking the user interface layout direction into account.
- [struct NSDirectionalRectEdge](nsdirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [enum NSRectAlignment](nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [struct UIDirectionalRectEdge](uidirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [UIKit macros](uikit-macros.md)
  Macros that UIKit defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioffset)*