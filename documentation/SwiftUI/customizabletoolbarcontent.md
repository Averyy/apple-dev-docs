# CustomizableToolbarContent

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

Conforming types represent items that can be placed in various locations in a customizable toolbar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol CustomizableToolbarContent : ToolbarContent where Self.Body : CustomizableToolbarContent
```

## Topics

### Using default options
- [func defaultCustomization(Visibility, options: ToolbarCustomizationOptions) -> some CustomizableToolbarContent](./customizabletoolbarcontent/defaultcustomization%28_,options%29.md)
  Configures the way customizable toolbar items with the default behavior behave.
- [func defaultCustomization() -> some CustomizableToolbarContent](./customizabletoolbarcontent/defaultcustomization%28%29.md)
  Configures customizable toolbar content with the default visibility and options.
### Customizing behaviors
- [func axisBehavior(ToolbarItemAxisBehavior) -> some CustomizableToolbarContent](./customizabletoolbarcontent/axisbehavior%28_%29.md)
  The bar axis behavior of the toolbar item.
- [func customizationBehavior(ToolbarCustomizationBehavior) -> some CustomizableToolbarContent](./customizabletoolbarcontent/customizationbehavior%28_%29.md)
  Configures the customization behavior of customizable toolbar content.
### Setting visibility
- [func hidden(Bool) -> some CustomizableToolbarContent](./customizabletoolbarcontent/hidden%28_%29.md)
  Hides a toolbar item within its toolbar.
- [func sharedBackgroundVisibility(Visibility) -> some CustomizableToolbarContent](./customizabletoolbarcontent/sharedbackgroundvisibility%28_%29.md)
  Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.
- [func visibilityPriority(ToolbarItemVisibilityPriority) -> some CustomizableToolbarContent](./customizabletoolbarcontent/visibilitypriority%28_%29.md)
  Defines the visibility priority for a toolbar item.
### Coordinating with animations
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some CustomizableToolbarContent](./customizabletoolbarcontent/matchedtransitionsource%28id,in%29.md)
  Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
### Adjusting content margins
- [func contentMarginsRemoved(Bool) -> some CustomizableToolbarContent](./customizabletoolbarcontent/contentmarginsremoved%28_%29.md)
  Configures whether the content margins are removed.

## Relationships

### Inherits From
- [ToolbarContent](./toolbarcontent.md)
### Conforming Types
- [EmptyView](./emptyview.md)
- [ForEach](./foreach.md)
- [Group](./group.md)
- [ToolbarItem](./toolbaritem.md)
- [ToolbarOverflowMenu](./toolbaroverflowmenu.md)
- [ToolbarSpacer](./toolbarspacer.md)
- [ToolbarTitleMenu](./toolbartitlemenu.md)
- [TupleContent](./tuplecontent.md)

## See Also

### Populating a customizable toolbar
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](./view/toolbar%28id,content%29.md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbarItemHidden(Bool) -> some View](./view/toolbaritemhidden%28_%29.md)
  Hides an individual view within a control group toolbar item.
- [struct ToolbarCustomizationBehavior](./toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct ToolbarCustomizationOptions](./toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.
- [struct SearchToolbarBehavior](./searchtoolbarbehavior.md)
  The behavior of a search field in a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent)*