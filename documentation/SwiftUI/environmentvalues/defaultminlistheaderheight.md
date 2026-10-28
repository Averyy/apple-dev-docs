# defaultMinListHeaderHeight

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The default minimum height of a header in a list.

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
var defaultMinListHeaderHeight: CGFloat? { get set }
```

## Discussion

When this value is `nil`, the system chooses the appropriate height. The default is `nil`.

## See Also

### Configuring a list’s layout
- [func listRowInsets(EdgeInsets?) -> some View](../view/listrowinsets%28_%29.md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](../view/listrowinsets%28_,_%29.md)
  Sets the insets of rows in a list on the specified edges.
- [var defaultMinListRowHeight: CGFloat](./defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [func listRowSpacing(CGFloat?) -> some View](../view/listrowspacing%28_%29.md)
  Sets the vertical spacing between two adjacent rows in a List.
- [func listSectionSpacing(_:)](../view/listsectionspacing%28_%29.md)
  Sets the spacing between adjacent sections in a [`List`](../list.md) to a custom value.
- [struct ListSectionSpacing](../listsectionspacing.md)
  The spacing options between two adjacent sections in a list.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](../view/listsectionmargins%28_,_%29.md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/defaultminlistheaderheight)*