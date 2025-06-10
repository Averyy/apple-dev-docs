# UIEdgeInsets

**Framework**: UIKit  
**Kind**: struct

The inset distances for views.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
struct UIEdgeInsets
```

#### Overview

Edge inset values are applied to a rectangle to shrink or expand the area represented by that rectangle. Typically, edge insets are used during view layout to modify the view’s frame. Positive values cause the frame to be inset (or shrunk) by the specified amount. Negative values cause the frame to be outset (or expanded) by the specified amount.

See also [`init(top:left:bottom:right:)`](uiedgeinsets/init(top:left:bottom:right:)-1s1t9.md) and [`zero`](uiedgeinsets/zero.md).

## Topics

### Creating edge insets
- [init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)](uiedgeinsets/init(top:left:bottom:right:)-6ff7.md)
  Creates an edge insets structure with the specified edges.
- [init()](uiedgeinsets/init.md)
  Initializes the edge insets structure to default values.
### Getting the edge values
- [var bottom: CGFloat](uiedgeinsets/bottom.md)
  The bottom edge inset value.
- [var left: CGFloat](uiedgeinsets/left.md)
  The left edge inset value.
- [var right: CGFloat](uiedgeinsets/right.md)
  The right edge inset value.
- [var top: CGFloat](uiedgeinsets/top.md)
  The top edge inset value.
### Managing edge insets
- [func inset(by insets: UIEdgeInsets) -> CGRect](../CoreFoundation/CGRect/inset(by:).md)
### Converting to and from strings
- [class func string(for insets: UIEdgeInsets) -> String](../Foundation/NSCoder/string(for:)-26b4z.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [class func uiEdgeInsets(for string: String) -> UIEdgeInsets](../Foundation/NSCoder/uiEdgeInsets(for:).md)
  Returns a UIKit edge insets structure based on the data in the specified string.
### Getting the empty edge insets
- [static let zero: UIEdgeInsets](uiedgeinsets/zero.md)
  An edge insets struct whose top, left, bottom, and right fields are all set to `0`.
### Comparing edge insets
- [func UIEdgeInsetsEqualToEdgeInsets(UIEdgeInsets, UIEdgeInsets) -> Bool](uiedgeinsetsequaltoedgeinsets(_:_:).md)
  Returns a Boolean value indicating whether the two edge insets are the same.

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

- [struct UIOffset](uioffset.md)
  A structure that specifies an amount to offset a position.
- [struct UIAxis](uiaxis.md)
  A structure that specifies the layout axes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiedgeinsets)*