# listSectionMargins(_:_:)

**Framework**: SwiftUI  
**Kind**: method

Set the section margins for the specific edges.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func listSectionMargins(_ edges: Edge.Set = .all, _ length: CGFloat?) -> some View
```

#### Return Value

A view in which the margins of list sections are set to the specified amount on the specified edges.

#### Discussion

Use this modifier on a list section to set customize its margins. Indicate the edges to set the margin of by naming either a single value from  [`Edge.Set`](edge/set.md), or by specifying an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that contains edge values. Margins for the other edges remain unchanged.

The default section margins are based on the list style, list section spacing and content margins of the list. Using this modifier overrides these default values completely.

For sections that have headers or footers, the section margins are applied around these.

## Parameters

- `edges`: The set of edges to pad for sections in this view. The   default is  .
- `length`: An amount, given in points, to pad section on the   specified edges.

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
- [struct ListSectionSpacing](listsectionspacing.md)
  The spacing options between two adjacent sections in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionmargins(_:_:))*