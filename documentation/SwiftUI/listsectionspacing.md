# ListSectionSpacing

**Framework**: SwiftUI  
**Kind**: struct

The spacing options between two adjacent sections in a list.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct ListSectionSpacing
```

## Topics

### Getting section spacing
- [static let `default`: ListSectionSpacing](listsectionspacing/default.md)
  The default spacing between sections
- [static let compact: ListSectionSpacing](listsectionspacing/compact.md)
  Compact spacing between sections
- [static func custom(CGFloat) -> ListSectionSpacing](listsectionspacing/custom(_:).md)
  Creates a custom spacing value.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [func listRowSpacing(CGFloat?) -> some View](view/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](view/listsectionspacing(_:).md)
  Sets the spacing between adjacent sections in a [`List`](list.md) to a custom value.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](view/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listsectionspacing)*