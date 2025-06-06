# contextMenu(menuItems:)

**Framework**: SwiftUI  
**Kind**: method

Adds a context menu to a tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func contextMenu<M>(@ViewBuilder menuItems: () -> M) -> some TabContent<Self.TabValue> where M : View
```

#### Return Value

A row that can display a context menu.

#### Discussion

Use this modifier to add a context menu to a tab’s sidebar representation. Compose the menu by returning controls like [`Button`](button.md), [`Toggle`](toggle.md) and [`Picker`](picker.md) from the `menuItems` closure. You can also use [`Menu`](menu.md) to define submenus, or [`Section`](section.md) to group items.

The following example adds the ability to pin the tab or share the tab’s books with a friend.

```swift
Tab("Currently Reading", systemImage: "book") {
    CurrentBooksList()
}
.contextMenu {
    Button {
        // Pin this tab.
    } label: {
        Label("Pin", systemImage: "pin")
    }
    Button {
        // Open a share sheet to share
    } label: {
        Label("Share", systemImage: "square.and.arrow.up")
    }
}
```

## Parameters

- `menuItems`: A closure that produces the menu’s contents. You   can deactivate the context menu by returning nothing from the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/contextmenu(menuitems:))*