# customizationID(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the identifier for a tab to persist its state.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func customizationID(_ id: String) -> some TabContent<Self.TabValue>
```

#### Discussion

The identifier needs to be stable, including across app version updates.

Only the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style supports supports customization. To enable customization, attach a [`TabViewCustomization`](tabviewcustomization.md) to the [`TabView`](tabview.md) using [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md).

All tabs and tab sections that support customization are required to have a customization ID. You can mark a tab as being non-customizable by specifying a [`disabled`](tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [`customizationBehavior(_:for:)`](tabcontent/customizationbehavior(_:for:).md).

If you apply a customization ID to a [`TabSection`](tabsection.md), ensure you specify customization IDs for all of the tabs within the section, unless the tab has been marked as having customization turned off.

The following example adds customization identifiers to all tabs and tab sections.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }
        .customizationID("com.myApp.climate")

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
        .customizationID("com.myApp.lights")
    }
    .customizationID("com.myApp.categories")
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## Parameters

- `id`: The identifier to associate with a tab or section.

## See Also

- [func badge(_:)](tabcontent/badge(_:).md)
  Generates a badge for a tab from an integer value.
- [func contextMenu<M>(menuItems: () -> M) -> some TabContent<Self.TabValue>
](tabcontent/contextmenu(menuitems:).md)
  Adds a context menu to a tab.
- [func customizationBehavior(TabCustomizationBehavior, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](tabcontent/customizationbehavior(_:for:).md)
  Configures the customization behavior of customizable tab view content.
- [func defaultSectionExpansion(TabSectionExpansion) -> some TabContent<Self.TabValue>
](tabcontent/defaultsectionexpansion(_:).md)
  Sets the default expansion state for the section containing this tab when displayed in the sidebar.
- [struct TabSectionExpansion](tabsectionexpansion.md)
  The default expansion state for a tab section in the sidebar.
- [func defaultVisibility(Visibility, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](tabcontent/defaultvisibility(_:for:).md)
  Configures the default visibility of a tab in customizable contexts.
- [func disabled(Bool) -> some TabContent<Self.TabValue>
](tabcontent/disabled(_:).md)
  Controls whether users can interact with this tab.
- [func draggable<T>(@autoclosure () -> T) -> some TabContent<Self.TabValue>
](tabcontent/draggable(_:).md)
  Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TabContent<Self.TabValue>
](tabcontent/dropdestination(for:action:).md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func help(_:)](tabcontent/help(_:).md)
  Adds help text to a tab using a text view that you provide.
- [func hidden(Bool) -> some TabContent<Self.TabValue>
](tabcontent/hidden(_:).md)
  Hides the tab from the user.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some TabContent<Self.TabValue>
](tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some TabContent<Self.TabValue>
](tabcontent/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func sectionActions<Content>(content: () -> Content) -> some TabContent<Self.TabValue>
](tabcontent/sectionactions(content:).md)
  Adds custom actions to a tab section.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some TabContent<Self.TabValue>
](tabcontent/springloadingbehavior(_:).md)
  Sets the spring loading behavior for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/customizationid(_:))*