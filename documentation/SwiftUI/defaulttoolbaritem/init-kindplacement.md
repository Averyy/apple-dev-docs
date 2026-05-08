# init(kind:placement:)

**Framework**: SwiftUI  
**Kind**: init

Creates a system-defined toolbar item from a `ToolbarDefaultItemKind` at the given `placement`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(kind: ToolbarDefaultItemKind, placement: ToolbarItemPlacement = .automatic)
```

#### Return Value

A `ToolbarItem` with content provided by the `kind`.

#### Discussion

Combinations of `kind` and `placement` may be valid on some platforms, but not on others. If the system has already placed a matching item `kind` in the toolbar, using a valid `DefaultToolbarItem` created by this initializer will implicitly replace the default-placed instance. You can use this to move default item kinds to other [`ToolbarItemPlacement`](toolbaritemplacement.md)s, or to reposition default item kinds relative to other toolbar content. For example, the below code repositions the `.search` item in between other items in the bottom bar. The search item is the leading-most item by default:

```swift
NavigationSplitView {
    AllCalendarsView()
} detail: {
    SelectedCalendarView()
        .searchable($query)
        .toolbar {
            ToolbarItem(placement: .bottomBar) {
                CalendarPicker()
            }
            ToolbarItem(placement: .bottomBar) {
                Invites()
            }
            DefaultToolbarItem(kind: .search, placement: .bottomBar)
            ToolbarSpacer(placement: .bottomBar)
            ToolbarItem(placement: .bottomBar) { NewEventButton() }
        }
}
```

##### Specifying the Search Column

`DefaultToolbarItem` also can be used to identify which column should be responsible for search when a [`NavigationSplitView`](navigationsplitview.md) is collapsed. Place the `DefaultToolbarItem` with the kind of `.search` in the column that should display the search field in compact. In the example below, the sidebar shows search in compact:

```swift
NavigationSplitView {
    SidebarView()
        .toolbar {
            DefaultToolbarItem(kind: .search, placement: .bottomBar)
        }
} content: {
    ContentView()
} detail: {
    DetailView()
}
.searchable(text: $text)
```

Note that this only applies when the search modifier is placed on the `NavigationSplitView`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaulttoolbaritem/init(kind:placement:))*