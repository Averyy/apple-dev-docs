# defaultSectionExpansion(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the default expansion state for the section containing this tab when displayed in the sidebar.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func defaultSectionExpansion(_ expansion: TabSectionExpansion) -> some TabContent<Self.TabValue>
```

## Discussion

Use this modifier to control whether a tab section starts expanded or collapsed in the sidebar. The user can manually change the expansion state, and subsequent user interactions take precedence over this default.

This modifier has no effect in contexts where sections are not collapsible — for example, on platforms that do not present a collapsible sidebar, or when [`automatic`](../tabsectionexpansion/automatic.md) is supplied.

```swift
TabView {
    TabSection("Library") {
        Tab("Songs", systemImage: "music.note") {
            SongsView()
        }
        Tab("Albums", systemImage: "square.stack") {
            AlbumsView()
        }
    }

    TabSection("Archive") {
        Tab("Old Playlists", systemImage: "archivebox") {
            ArchiveView()
        }
        Tab("Deleted", systemImage: "trash") {
            DeletedView()
        }
    }
    .defaultSectionExpansion(.collapsed)
}
.tabViewStyle(.sidebarAdaptable)
```

## Parameters

- `expansion`: The default expansion behavior for the containing section. The default is [`automatic`](../tabsectionexpansion/automatic.md).

## See Also

### Configuring tab content
- [func badge(_:)](./badge%28_%29.md)
  Generates a badge for the tab from a localized string resource.
- [func contextMenu<M>(menuItems: () -> M) -> some TabContent<Self.TabValue>
](./contextmenu%28menuitems%29.md)
  Adds a context menu to a tab.
- [func customizationBehavior(TabCustomizationBehavior, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](./customizationbehavior%28_,for%29.md)
  Configures the customization behavior of customizable tab view content.
- [func customizationID(String) -> some TabContent<Self.TabValue>
](./customizationid%28_%29.md)
  Sets the identifier for a tab to persist its state.
- [struct TabSectionExpansion](../tabsectionexpansion.md)
  The default expansion state for a tab section in the sidebar.
- [func defaultVisibility(Visibility, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](./defaultvisibility%28_,for%29.md)
  Configures the default visibility of a tab in customizable contexts.
- [func disabled(Bool) -> some TabContent<Self.TabValue>
](./disabled%28_%29.md)
  Controls whether users can interact with this tab.
- [func draggable<T>(@autoclosure () -> T) -> some TabContent<Self.TabValue>
](./draggable%28_%29.md)
  Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TabContent<Self.TabValue>
](./dropdestination%28for,action%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func help(_:)](./help%28_%29.md)
  Adds help text to a tab using a text view that you provide.
- [func hidden(Bool) -> some TabContent<Self.TabValue>
](./hidden%28_%29.md)
  Hides the tab from the user.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some TabContent<Self.TabValue>
](./popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some TabContent<Self.TabValue>
](./popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func sectionActions<Content>(content: () -> Content) -> some TabContent<Self.TabValue>
](./sectionactions%28content%29.md)
  Adds custom actions to a tab section.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some TabContent<Self.TabValue>
](./springloadingbehavior%28_%29.md)
  Sets the spring loading behavior for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/defaultsectionexpansion(_:))*