# popover(isPresented:attachmentAnchor:arrowEdge:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a popover when a given condition is true.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ContentBuilder content: @escaping () -> Content) -> some TabContent<Self.TabValue> where Content : View
```

## Discussion

Use this method to show a popover whose contents are a SwiftUI view that you provide when a bound Boolean variable is `true`. In the example below, a popover displays whenever the user toggles the `isShowingPopover` state variable by pressing the “Show Popover” button:

```swift
struct PopoverExample: View {
    @State private var isShowingPopover = false

    var body: some View {
        TabView {
            Tab("Popover Anchor", systemImage: "arrow.down") {
                Button("Show Popover") {
                    self.isShowingPopover = true
                }
            }
            .popover(isPresented: $isShowingPopover) {
                Text("Popover Content")
                    .padding()
            }
        }
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether to present the popover content that you return from the modifier’s `content` closure.
- `attachmentAnchor`: The positioning anchor that defines the attachment point of the popover. The default is [`bounds`](../anchor/source/bounds.md).
- `arrowEdge`: The edge of the `attachmentAnchor` that defines the location of the popover’s arrow in macOS. The default is [`Edge.top`](../edge/top.md).
- `content`: A closure returning the content of the popover.

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
- [func help(_:)](./help%28_%29.md)
  Adds help text to a tab using a text view that you provide.
- [func hidden(Bool) -> some TabContent<Self.TabValue>
](./hidden%28_%29.md)
  Hides the tab from the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:))*