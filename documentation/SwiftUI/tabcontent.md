# TabContent

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A type that provides content for programmatically selectable tabs in a tab view.

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
@MainActor
@preconcurrency protocol TabContent<TabValue>
```

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Setting tab content
- [var body: Self.Body](./tabcontent/body-swift.property.md)
  The value of this type’s nested content.
- [associatedtype Body : TabContent](./tabcontent/body-swift.associatedtype.md)
  The type of content representing the body of this content type.
- [associatedtype TabValue : Hashable](./tabcontent/tabvalue.md)
  The type used to drive selection for the containing tab view.
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
- [struct TabSectionExpansion](./tabsectionexpansion.md)
  The default expansion state for a tab section in the sidebar.
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
- [func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: () -> T) -> some TabContent<Self.TabValue>
](./tabcontent/swipeactions%28edge,allowsfullswipe,content%29.md)
  Adds custom swipe actions to a tab in a tab view.
- [func tabPlacement(TabPlacement) -> some TabContent<Self.TabValue>
](./tabcontent/tabplacement%28_%29.md)
  Specifies the placement of a tab.
- [struct TabPlacement](./tabplacement.md)
  A place that a tab can appear.
### Configuring tab accessibility
- [func accessibilityHint(_:isEnabled:)](./tabcontent/accessibilityhint%28_,isenabled%29.md)
  Communicates to the user what happens after selecting the tab.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](./tabcontent/accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityInputLabels(_:isEnabled:)](./tabcontent/accessibilityinputlabels%28_,isenabled%29.md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](./tabcontent/accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the tab that describes its contents.
- [func accessibilityValue(_:isEnabled:)](./tabcontent/accessibilityvalue%28_,isenabled%29.md)
  Adds a textual description of the value that the tab contains.

## Relationships

### Conforming Types
- [AnyTabContent](./anytabcontent.md)
- [ForEach](./foreach.md)
- [Group](./group.md)
- [Tab](./tab.md)
- [TabSection](./tabsection.md)

## See Also

### Configuring a tab
- [func sectionActions<Content>(content: () -> Content) -> some View](./view/sectionactions%28content%29.md)
  Adds custom actions to a section.
- [struct TabPlacement](./tabplacement.md)
  A place that a tab can appear.
- [struct TabContentBuilder](./tabcontentbuilder.md)
  A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [struct AnyTabContent](./anytabcontent.md)
  Type erased tab content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent)*