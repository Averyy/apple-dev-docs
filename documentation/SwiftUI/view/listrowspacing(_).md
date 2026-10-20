# listRowSpacing(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the vertical spacing between two adjacent rows in a List.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 27.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listRowSpacing(_ spacing: CGFloat?) -> some View
```

#### Discussion

The following example creates a List with 10 pts of spacing between each row:

```swift
List {
    Text("Blue")
    Text("Red")
}
.listRowSpacing(10.0)
```

## Parameters

- `spacing`: The spacing value to use. A value of `nil` uses the default spacing.

## See Also

### Configuring a list’s layout
- [func listRowInsets(EdgeInsets?) -> some View](./listrowinsets%28_%29.md)
  Applies an inset to the rows in a list.
- [func listRowInsets(Edge.Set, CGFloat?) -> some View](./listrowinsets%28_,_%29.md)
  Sets the insets of rows in a list on the specified edges.
- [var defaultMinListRowHeight: CGFloat](../environmentvalues/defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [var defaultMinListHeaderHeight: CGFloat?](../environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [func listSectionSpacing(_:)](./listsectionspacing%28_%29.md)
  Sets the spacing between adjacent sections in a [`List`](../list.md) to a custom value.
- [struct ListSectionSpacing](../listsectionspacing.md)
  The spacing options between two adjacent sections in a list.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](./listsectionmargins%28_,_%29.md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowspacing(_:))*