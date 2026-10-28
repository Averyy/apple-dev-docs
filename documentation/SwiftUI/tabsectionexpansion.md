# TabSectionExpansion

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The default expansion state for a tab section in the sidebar.

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
struct TabSectionExpansion
```

## Overview

Use this type in conjunction with the [`defaultSectionExpansion(_:)`](./tabcontent/defaultsectionexpansion%28_%29.md) modifier.

## Topics

### Tab section expansion options
- [static let automatic: TabSectionExpansion](./tabsectionexpansion/automatic.md)
  The system determines the default expansion state.
- [static let collapsed: TabSectionExpansion](./tabsectionexpansion/collapsed.md)
  The section is initially collapsed in the sidebar.
- [static let expanded: TabSectionExpansion](./tabsectionexpansion/expanded.md)
  The section is initially expanded in the sidebar.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring tab content
- [func badge(_:)](./tabcontent/badge%28_%29.md)
  Generates a badge for the tab from a localized string resource.
- [func contextMenu<M>(menuItems: () -> M) -> some TabContent<Self.TabValue>
](./tabcontent/contextmenu%28menuitems%29.md)
  Adds a context menu to a tab.
- [func customizationBehavior(TabCustomizationBehavior, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](./tabcontent/customizationbehavior%28_,for%29.md)
  Configures the customization behavior of customizable tab view content.
- [func customizationID(String) -> some TabContent<Self.TabValue>
](./tabcontent/customizationid%28_%29.md)
  Sets the identifier for a tab to persist its state.
- [func defaultSectionExpansion(TabSectionExpansion) -> some TabContent<Self.TabValue>
](./tabcontent/defaultsectionexpansion%28_%29.md)
  Sets the default expansion state for the section containing this tab when displayed in the sidebar.
- [func defaultVisibility(Visibility, for: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
](./tabcontent/defaultvisibility%28_,for%29.md)
  Configures the default visibility of a tab in customizable contexts.
- [func disabled(Bool) -> some TabContent<Self.TabValue>
](./tabcontent/disabled%28_%29.md)
  Controls whether users can interact with this tab.
- [func draggable<T>(@autoclosure () -> T) -> some TabContent<Self.TabValue>
](./tabcontent/draggable%28_%29.md)
  Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some TabContent<Self.TabValue>
](./tabcontent/dropdestination%28for,action%29.md)
  Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [func help(_:)](./tabcontent/help%28_%29.md)
  Adds help text to a tab using a text view that you provide.
- [func hidden(Bool) -> some TabContent<Self.TabValue>
](./tabcontent/hidden%28_%29.md)
  Hides the tab from the user.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some TabContent<Self.TabValue>
](./tabcontent/popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some TabContent<Self.TabValue>
](./tabcontent/popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func sectionActions<Content>(content: () -> Content) -> some TabContent<Self.TabValue>
](./tabcontent/sectionactions%28content%29.md)
  Adds custom actions to a tab section.
- [func springLoadingBehavior(SpringLoadingBehavior) -> some TabContent<Self.TabValue>
](./tabcontent/springloadingbehavior%28_%29.md)
  Sets the spring loading behavior for the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsectionexpansion)*