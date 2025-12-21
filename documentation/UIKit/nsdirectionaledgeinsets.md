# NSDirectionalEdgeInsets

**Framework**: UIKit  
**Kind**: struct

The inset distances for views, taking the user interface layout direction into account.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct NSDirectionalEdgeInsets
```

## Topics

### Creating directional edge insets
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](nsdirectionaledgeinsets/init(top:leading:bottom:trailing:)-6wnda.md)
  Creates a directional edge insets structure that contains the specified values.
- [init()](nsdirectionaledgeinsets/init.md)
  Creates a directional edge insets structure that contains default values.
- [init(EdgeInsets)](nsdirectionaledgeinsets/init(_:).md)
  Creates a directional edge insets structure from a SwiftUI edge insets structure.
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
- [class func string(for: NSDirectionalEdgeInsets) -> String](../Foundation/NSCoder/string(for:)-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func nsDirectionalEdgeInsets(for: String) -> NSDirectionalEdgeInsets](../Foundation/NSCoder/nsDirectionalEdgeInsets(for:).md)
  Returns a directional edge insets structure based on data in the specified string.
### Getting the empty edge insets
- [static let zero: NSDirectionalEdgeInsets](nsdirectionaledgeinsets/zero.md)
  A directional edge insets structure whose top, leading, bottom, and trailing fields all have a value of `0`.

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
- [struct UIEdgeInsets](uiedgeinsets.md)
  The inset distances for views.
- [struct NSDirectionalRectEdge](nsdirectionalrectedge.md)
  Constants that specify an edge or a set of edges, taking the user interface layout direction into account.
- [enum NSRectAlignment](nsrectalignment.md)
  Constants that specify alignment to an edge or a set of edges depending on the user interface layout direction.
- [UIKit macros](uikit-macros.md)
  Macros that UIKit defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsets)*