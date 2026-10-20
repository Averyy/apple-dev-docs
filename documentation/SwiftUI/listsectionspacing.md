# ListSectionSpacing

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let `default`: ListSectionSpacing](./listsectionspacing/default.md)
  The default spacing between sections
- [static let compact: ListSectionSpacing](./listsectionspacing/compact.md)
  Compact spacing between sections
- [static func custom(CGFloat) -> ListSectionSpacing](./listsectionspacing/custom%28_%29.md)
  Creates a custom spacing value.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring a list’s layout
- [func listRowInsets(EdgeInsets?) -> some View](./view/listrowinsets%28_%29.md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](./view/listrowinsets%28_,_%29.md)
  Sets the insets of rows in a list on the specified edges.
- [var defaultMinListRowHeight: CGFloat](./environmentvalues/defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [var defaultMinListHeaderHeight: CGFloat?](./environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [func listRowSpacing(CGFloat?) -> some View](./view/listrowspacing%28_%29.md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](./view/listsectionspacing%28_%29.md)
  Sets the spacing between adjacent sections in a [`List`](./list.md) to a custom value.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](./view/listsectionmargins%28_,_%29.md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/listsectionspacing)*