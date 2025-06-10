# NSDirectionalEdgeInsets

**Framework**: AppKit  
**Kind**: struct

The inset distances for views, taking the user interface layout direction into account.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct NSDirectionalEdgeInsets
```

## Topics

### Creating directional edge insets
- [init()](nsdirectionaledgeinsets/init.md)
  Creates a directional edge insets structure that contains default values.
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](nsdirectionaledgeinsets/init(top:leading:bottom:trailing:).md)
  Creates a directional edge insets structure that contains the specified values.
### Getting the edge values
- [var bottom: CGFloat](nsdirectionaledgeinsets/bottom.md)
  The bottom edge inset value.
- [var leading: CGFloat](nsdirectionaledgeinsets/leading.md)
  The leading edge inset value.
- [var top: CGFloat](nsdirectionaledgeinsets/top.md)
  The top edge inset value.
- [var trailing: CGFloat](nsdirectionaledgeinsets/trailing.md)
  The trailing edge inset value.
### Converting to and from strings
- [class func string(for insets: NSDirectionalEdgeInsets) -> String](../Foundation/NSCoder/string(for:)-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func nsDirectionalEdgeInsets(for string: String) -> NSDirectionalEdgeInsets](../Foundation/NSCoder/nsDirectionalEdgeInsets(for:).md)
  Returns a directional edge insets structure based on data in the specified string.
### Getting the empty edge insets
- [let NSDirectionalEdgeInsetsZero: NSDirectionalEdgeInsets](nsdirectionaledgeinsetszero.md)
  A directional edge insets structure whose top, leading, bottom, and trailing fields all have a value of `0`.
### Initializers
- [init(EdgeInsets)](nsdirectionaledgeinsets/init(_:).md)
  Create edge insets from the equivalent EdgeInsets.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum NSRectAlignment](nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [struct NSDirectionalRectEdge](nsdirectionalrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdirectionaledgeinsets)*