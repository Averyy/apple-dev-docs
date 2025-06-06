# contextMenu(menuItems:)

**Framework**: SwiftUI  
**Kind**: method

Adds a context menu to a table row.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func contextMenu<M>(@ViewBuilder menuItems: () -> M) -> ModifiedContent<Self, _ContextMenuTableRowModifier<M>> where M : View
```

#### Return Value

A row that can display a context menu.

#### Discussion

Use this modifier to add a context menu to a table row. Compose the menu by returning controls like [`Button`](button.md), [`Toggle`](toggle.md), and [`Picker`](picker.md) from the `menuItems` closure. You can also use [`Menu`](menu.md) to define submenus, or [`Section`](section.md) to group items.

The following example adds a context menu to each row in a table that people can use to send an email to the person represented by that row:

```swift
Table(of: Person.self) {
    TableColumn("Given Name", value: \.givenName)
    TableColumn("Family Name", value: \.familyName)
} rows: {
    ForEach(people) { person in
        TableRow(person)
            .contextMenu {
                Button("Send Email...") { }
            }
    }
}
```

If you want to display a preview beside the context menu, use [`contextMenu(menuItems:preview:)`](tablerowcontent/contextmenu(menuitems:preview:).md). If you want to display a context menu that’s based on the current selection, use [`contextMenu(forSelectionType:menu:primaryAction:)`](view/contextmenu(forselectiontype:menu:primaryaction:).md). To add context menus to other kinds of views, use [`contextMenu(menuItems:)`](view/contextmenu(menuitems:).md).

## Parameters

- `menuItems`: A closure that produces the menu’s contents. You   can deactivate the context menu by returning nothing from the closure.

## See Also

- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>>](tablerowcontent/contextmenu(menuitems:preview:).md)
  Adds a context menu with a preview to a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowcontent/contextmenu(menuitems:))*