# Tables

**Framework**: SwiftUI

Display selectable, sortable data arranged in rows and columns.

#### Overview

Use a table to display multiple values across a collection of elements. Each element in the collection appears in a different row of the table, while each value for a given element appears in a different column. Narrow displays may adapt to show only the first column of the table.

![None](https://docs-assets.developer.apple.com/published/a784f68f4e1b73d07143c7d57ae3f586/tables-hero%402x.png)

When you create a table, you provide a collection of elements, and then tell the table how to find the needed value for each column. In simple cases, SwiftUI infers the element for each row, but you can also specify the row elements explicitly in more complex scenarios. With a small amount of additional configuration, you can also make the items in the table selectable, and the columns sortable.

Like a [`List`](list.md), a table includes implicit vertical scrolling that you can configure using the view modifiers described in [`Scroll views`](scroll-views.md). For design guidance, see [`Lists and tables`](https://developer.apple.com/design/Human-Interface-Guidelines/lists-and-tables) in the Human Interface Guidelines.

## Topics

### Creating a table
- [Building a great Mac app with SwiftUI](building-a-great-mac-app-with-swiftui.md)
  Create engaging SwiftUI Mac apps by incorporating side bars, tables, toolbars, and several other popular user interface elements.
- [struct Table](table.md)
  A container that presents rows of data arranged in one or more columns, optionally providing the ability to select one or more members.
- [func tableStyle<S>(S) -> some View](view/tablestyle(_:).md)
  Sets the style for tables within this view.
### Creating columns
- [struct TableColumn](tablecolumn.md)
  A column that displays a view for each row in a table.
- [protocol TableColumnContent](tablecolumncontent.md)
  A type used to represent columns within a table.
- [struct TableColumnAlignment](tablecolumnalignment.md)
  Describes the alignment of the content of a table column.
- [struct TableColumnBuilder](tablecolumnbuilder.md)
  A result builder that creates table column content from closures.
- [struct TableColumnForEach](tablecolumnforeach.md)
  A structure that computes columns on demand from an underlying collection of identified data.
### Customizing columns
- [func tableColumnHeaders(Visibility) -> some View](view/tablecolumnheaders(_:).md)
  Controls the visibility of a `Table`’s column header views.
- [struct TableColumnCustomization](tablecolumncustomization.md)
  A representation of the state of the columns in a table.
- [struct TableColumnCustomizationBehavior](tablecolumncustomizationbehavior.md)
  A set of customization behaviors of a column that a table can offer to a user.
### Creating rows
- [struct TableRow](tablerow.md)
  A row that represents a data value in a table.
- [protocol TableRowContent](tablerowcontent.md)
  A type used to represent table rows.
- [struct TableHeaderRowContent](tableheaderrowcontent.md)
  A table row that displays a single view instead of columned content.
- [struct TupleTableRowContent](tupletablerowcontent.md)
  A type of table column content that creates table rows created from a Swift tuple of table rows.
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.
- [struct TableRowBuilder](tablerowbuilder.md)
  A result builder that creates table row content from closures.
### Adding progressive disclosure
- [struct DisclosureTableRow](disclosuretablerow.md)
  A kind of table row that shows or hides additional rows based on the state of a disclosure control.
- [struct TableOutlineGroupContent](tableoutlinegroupcontent.md)
  An opaque table row type created by a table’s hierarchical initializers.

## See Also

- [Layout fundamentals](layout-fundamentals.md)
  Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md)
  Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md)
  Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md)
  Display a structured, scrollable column of information.
- [View groupings](view-groupings.md)
  Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md)
  Enable people to scroll to content that doesn’t fit in the current display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tables)*