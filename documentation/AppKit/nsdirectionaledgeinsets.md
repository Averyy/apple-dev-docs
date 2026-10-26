# NSDirectionalEdgeInsets

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The inset distances for views, taking the user interface layout direction into account.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct NSDirectionalEdgeInsets
```

```c
typedef struct NSDirectionalEdgeInsets { ... } NSDirectionalEdgeInsets;
```

## Topics

### Creating directional edge insets
- [init()](./nsdirectionaledgeinsets/init%28%29.md)
  Creates a directional edge insets structure that contains default values.
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](./nsdirectionaledgeinsets/init%28top,leading,bottom,trailing%29.md)
  Creates a directional edge insets structure that contains the specified values.
- [NSDirectionalEdgeInsetsMake](./nsdirectionaledgeinsetsmake.md)
### Getting the edge values
- [var bottom: CGFloat](./nsdirectionaledgeinsets/bottom.md)
  The bottom edge inset value.
- [var leading: CGFloat](./nsdirectionaledgeinsets/leading.md)
  The leading edge inset value.
- [var top: CGFloat](./nsdirectionaledgeinsets/top.md)
  The top edge inset value.
- [var trailing: CGFloat](./nsdirectionaledgeinsets/trailing.md)
  The trailing edge inset value.
### Converting to and from strings
- [class func string(for: NSDirectionalEdgeInsets) -> String](../Foundation/nscoder/string%28for%29-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func nsDirectionalEdgeInsets(for: String) -> NSDirectionalEdgeInsets](../Foundation/nscoder/nsdirectionaledgeinsets%28for%29.md)
  Returns a directional edge insets structure based on data in the specified string.
### Getting the empty edge insets
- [let NSDirectionalEdgeInsetsZero: NSDirectionalEdgeInsets](./nsdirectionaledgeinsetszero.md)
  A directional edge insets structure whose top, leading, bottom, and trailing fields all have a value of `0`.
### Initializers
- [init(EdgeInsets)](./nsdirectionaledgeinsets/init%28_%29.md)
  Create edge insets from the equivalent EdgeInsets.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related types
- [enum NSRectAlignment](./nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [struct NSDirectionalRectEdge](./nsdirectionalrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdirectionaledgeinsets)*