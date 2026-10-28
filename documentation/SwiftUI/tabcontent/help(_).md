# help(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds help text to a tab using a text view that you provide.

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
func help(_ text: Text) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
nonisolated
func help(_ textKey: LocalizedStringKey) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func help(_ textResource: LocalizedStringResource) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func help<S>(_ text: S) -> some TabContent<Self.TabValue> where S : StringProtocol
```

## Discussion

Adding help to a tab configures the tab’s accessibility hint and its help tag (also called a *tooltip*) in macOS or visionOS. For more information on using help tags, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) in the Human Interface Guidelines.

```swift
TabView {
    Tab("List", systemImage: "list.dash") {
        ListView()
    }
    .help(Text("Display symbols in list format"))
}
```

## Parameters

- `text`: The [`Text`](../text.md) view to use as help.

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
- [func defaultSectionExpansion(TabSectionExpansion) -> some TabContent<Self.TabValue>
](./defaultsectionexpansion%28_%29.md)
  Sets the default expansion state for the section containing this tab when displayed in the sidebar.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/help(_:))*