# defaultMinListRowHeight

**Framework**: SwiftUI  
**Kind**: property

The default minimum height of rows in a list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var defaultMinListRowHeight: CGFloat { get set }
```

#### Discussion

The height of list rows is bounded below by this default value, and is otherwise determined by the height of the row’s content and the row insets.

## See Also

- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [func listRowSpacing(CGFloat?) -> some View](view/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](view/listsectionspacing(_:).md)
  Sets the spacing between adjacent sections in a [`List`](list.md) to a custom value.
- [struct ListSectionSpacing](listsectionspacing.md)
  The spacing options between two adjacent sections in a list.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](view/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/defaultminlistrowheight)*