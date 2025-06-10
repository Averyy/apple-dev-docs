# CustomizableToolbarContent

**Framework**: SwiftUI  
**Kind**: protocol

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
- [func defaultCustomization() -> some CustomizableToolbarContent](customizabletoolbarcontent/defaultcustomization.md)
  Configures customizable toolbar content with the default visibility and options.
- [func defaultCustomization(Visibility, options: ToolbarCustomizationOptions) -> some CustomizableToolbarContent](customizabletoolbarcontent/defaultcustomization(_:options:).md)
  Configures the way customizable toolbar items with the default behavior behave.
### Customizing the behavior
- [func customizationBehavior(ToolbarCustomizationBehavior) -> some CustomizableToolbarContent](customizabletoolbarcontent/customizationbehavior(_:).md)
  Configures the customization behavior of customizable toolbar content.
### Instance Methods
- [func hidden(Bool) -> some CustomizableToolbarContent](customizabletoolbarcontent/hidden(_:).md)
  Hides a toolbar item within its toolbar.
- [func matchedTransitionSource(id: some Hashable, in: Namespace.ID) -> some CustomizableToolbarContent](customizabletoolbarcontent/matchedtransitionsource(id:in:).md)
  Identifies this toolbar content as the source of a navigation transition, such as a zoom transition.
- [func sharedBackgroundVisibility(Visibility) -> some CustomizableToolbarContent](customizabletoolbarcontent/sharedbackgroundvisibility(_:).md)
  Controls the visibility of the glass background effect on items in the toolbar. In certain contexts, such as the navigation bar on iOS and the window toolbar on macOS, toolbar items will be given a glass background effect that is shared with other items in the same logical grouping.

## Relationships

### Inherits From
- [ToolbarContent](toolbarcontent.md)
### Conforming Types
- [Group](group.md)
- [ToolbarItem](toolbaritem.md)
- [ToolbarSpacer](toolbarspacer.md)
- [ToolbarTitleMenu](toolbartitlemenu.md)

## See Also

- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [struct ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct ToolbarCustomizationOptions](toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.
- [struct SearchToolbarBehavior](searchtoolbarbehavior.md)
  The behavior of a search field in a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/customizabletoolbarcontent)*