# listSectionSpacing(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the spacing between adjacent sections in a [`List`](list.md) to a custom value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func listSectionSpacing(_ spacing: CGFloat) -> some View
```

#### Discussion

The following example creates a [`List`](list.md) with 5 pts of spacing between sections:

```swift
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
}
.listSectionSpacing(5.0)
```

Spacing can also be specified on an individual [`Section`](section.md), as in this example:

```swift
Section("Borders") {
    Text("Dashed")
    Text("Solid")
}
.listSectionSpacing(10.0)
```

If adjacent sections have different spacing applied, each section applies half its spacing above and below. Sections without explicit spacing apply the spacing of their adjacent sections.

```swift
List {
    Section("Colors") {
        Text("Blue")
        Text("Red")
    }

    Section("Borders") {
        Text("Dashed")
        Text("Solid")
    }
    .listSectionSpacing(10.0)

    Section("Shapes") {
        Text("Square")
        Text("Circle")
    }
    .listSectionSpacing(100.0)
}
```

In the above example, the “Colors” and “Borders” section are separated by 10 pts of spacing, and the “Borders” and “Shapes” section are separated by 55 pts of spacing.

Spacing applied on sections in the [`List`](list.md) overrides spacing applied on the [`List`](list.md) as a whole.

## Parameters

- `spacing`: The amount of spacing to apply.

## See Also

- [func listRowInsets(EdgeInsets?) -> some View](view/listrowinsets(_:).md)
  Applies an inset to the rows in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [func listRowSpacing(CGFloat?) -> some View](view/listrowspacing(_:).md)
  Sets the vertical spacing between two adjacent rows in a List.
- [struct ListSectionSpacing](listsectionspacing.md)
  The spacing options between two adjacent sections in a list.
- [func listSectionMargins(Edge.Set, CGFloat?) -> some View](view/listsectionmargins(_:_:).md)
  Set the section margins for the specific edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionspacing(_:))*