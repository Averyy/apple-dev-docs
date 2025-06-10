# init(kind:placement:)

**Framework**: SwiftUI  
**Kind**: init

Creates a system-defined toolbar item from a `ToolbarDefaultItemKind` at the given `placement`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaulttoolbaritem/init(kind:placement:))*