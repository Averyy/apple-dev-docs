# tableColumnHeaders(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls the visibility of a `Table`’s column header views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func tableColumnHeaders(_ visibility: Visibility) -> some View
```

#### Discussion

By default, `Table` will display a global header view with the labels of each table column. This area is also where users can sort, resize, and rearrange the columns. For simple cases that don’t require those features, this header can be hidden.

This will not affect the header of any `Section`s in a table.

```swift
Table(article.authors) {
    TableColumn("Name", value: \.name)
    TableColumn("Title", value: \.title)
}
.tableColumnHeaders(.hidden)
```

## Parameters

- `visibility`: A value of   will show table columns,    will remove them, and   will defer to default   behavior.

## See Also

- [struct TableColumnCustomization](tablecolumncustomization.md)
  A representation of the state of the columns in a table.
- [struct TableColumnCustomizationBehavior](tablecolumncustomizationbehavior.md)
  A set of customization behaviors of a column that a table can offer to a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tablecolumnheaders(_:))*