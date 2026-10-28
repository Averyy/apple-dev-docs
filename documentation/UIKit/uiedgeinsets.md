# UIEdgeInsets

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The inset distances for views.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
struct UIEdgeInsets
```

```c
typedef struct UIEdgeInsets { ... } UIEdgeInsets;
```

## Overview

Edge inset values are applied to a rectangle to shrink or expand the area represented by that rectangle. Typically, edge insets are used during view layout to modify the view’s frame. Positive values cause the frame to be inset (or shrunk) by the specified amount. Negative values cause the frame to be outset (or expanded) by the specified amount.

See also [`init(top:left:bottom:right:)`](./uiedgeinsets/init%28top,left,bottom,right%29-1s1t9.md) and [`zero`](./uiedgeinsets/zero.md).

## Topics

### Creating edge insets
- [init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)](./uiedgeinsets/init%28top,left,bottom,right%29-6ff7.md)
  Creates an edge insets structure with the specified edges.
- [init()](./uiedgeinsets/init%28%29.md)
  Initializes the edge insets structure to default values.
- [UIEdgeInsetsMake](./uiedgeinsets/init%28top,left,bottom,right%29-1s1t9.md)
  Creates an edge insets structure with the specified edges.
### Getting the edge values
- [var bottom: CGFloat](./uiedgeinsets/bottom.md)
  The bottom edge inset value.
- [var left: CGFloat](./uiedgeinsets/left.md)
  The left edge inset value.
- [var right: CGFloat](./uiedgeinsets/right.md)
  The right edge inset value.
- [var top: CGFloat](./uiedgeinsets/top.md)
  The top edge inset value.
### Managing edge insets
- [func inset(by: UIEdgeInsets) -> CGRect](../CoreFoundation/cgrect/inset%28by%29.md)
- [UIEdgeInsetsInsetRect](./uiedgeinsetsinsetrect.md)
  Adjusts a rectangle by the given edge insets.
### Converting to and from strings
- [class func string(for: UIEdgeInsets) -> String](../Foundation/nscoder/string%28for%29-26b4z.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [class func uiEdgeInsets(for: String) -> UIEdgeInsets](../Foundation/nscoder/uiedgeinsets%28for%29.md)
  Returns a UIKit edge insets structure based on the data in the specified string.
- [NSStringFromUIEdgeInsets](./nsstringfromuiedgeinsets.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [UIEdgeInsetsFromString](./uiedgeinsetsfromstring.md)
  Returns a UIKit edge insets structure based on the data in the specified string.
### Getting the empty edge insets
- [static let zero: UIEdgeInsets](./uiedgeinsets/zero.md)
  An edge insets struct whose top, left, bottom, and right fields are all set to `0`.
### Comparing edge insets
- [func UIEdgeInsetsEqualToEdgeInsets(UIEdgeInsets, UIEdgeInsets) -> Bool](./uiedgeinsetsequaltoedgeinsets%28_,_%29.md)
  Returns a Boolean value indicating whether the two edge insets are the same.
- [UIEdgeInsetsEqualToEdgeInsets](./uiedgeinsetsequaltoedgeinsets.md)
  Returns a Boolean value indicating whether the two edge insets are the same.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related types
- [struct UIOffset](./uioffset.md)
  A structure that specifies an amount to offset a position.
- [struct UIAxis](./uiaxis.md)
  A structure that specifies the layout axes.
- [struct NSDirectionalEdgeInsets](./nsdirectionaledgeinsets.md)
  The inset distances for views, taking the user interface layout direction into account.
- [struct NSDirectionalRectEdge](./nsdirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [enum NSRectAlignment](./nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](./uikit-macros.md)
  Macros that UIKit defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiedgeinsets)*