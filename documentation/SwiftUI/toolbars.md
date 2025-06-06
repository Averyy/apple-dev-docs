# Toolbars

**Framework**: SwiftUI

Provide immediate access to frequently used commands and controls.

#### Overview

The system might present toolbars above or below your app’s content, depending on the platform and the context.

![None](https://docs-assets.developer.apple.com/published/16bd7e535a587b44ad58a35c066192d9/toolbars-hero%402x.png)

Add items to a toolbar by applying the [`toolbar(content:)`](view/toolbar(content:).md) view modifier to a view in your app. You can also configure the toolbar using view modifiers. For example, you can set the visibility of a toolbar with the [`toolbar(_:for:)`](view/toolbar(_:for:).md) modifier.

For design guidance, see [`Toolbars`](https://developer.apple.com/design/Human-Interface-Guidelines/toolbars) in the Human Interface Guidelines.

## Topics

### Populating a toolbar
- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.
### Populating a customizable toolbar
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [protocol CustomizableToolbarContent](customizabletoolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a customizable toolbar.
- [struct ToolbarCustomizationBehavior](toolbarcustomizationbehavior.md)
  The customization behavior of customizable toolbar content.
- [struct ToolbarCustomizationOptions](toolbarcustomizationoptions.md)
  Options that influence the default customization behavior of customizable toolbar content.
### Removing default items
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](view/toolbar(removing:).md)
  Remove a toolbar item present by default
- [struct ToolbarDefaultItemKind](toolbardefaultitemkind.md)
  A kind of toolbar item a `View` adds by default.
### Setting toolbar visibility
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [struct ToolbarPlacement](toolbarplacement.md)
  The placement of a toolbar.
### Specifying the role of toolbar content
- [func toolbarRole(ToolbarRole) -> some View](view/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [struct ToolbarRole](toolbarrole.md)
  The purpose of content that populates the toolbar.
### Styling a toolbar
- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func windowToolbarStyle<S>(S) -> some Scene](scene/windowtoolbarstyle(_:).md)
  Sets the style for the toolbar defined within this scene.
- [protocol WindowToolbarStyle](windowtoolbarstyle.md)
  A specification for the appearance and behavior of a window’s toolbar.
- [var toolbarLabelStyle: ToolbarLabelStyle?](environmentvalues/toolbarlabelstyle.md)
  The label style to apply to controls within a toolbar.
- [struct ToolbarLabelStyle](toolbarlabelstyle.md)
  The label style of a toolbar.
### Configuring the toolbar title display mode
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](view/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [struct ToolbarTitleDisplayMode](toolbartitledisplaymode.md)
  A type that defines the behavior of title of a toolbar.
### Setting the toolbar title menu
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](view/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [struct ToolbarTitleMenu](toolbartitlemenu.md)
  The title menu of a toolbar.
### Creating an ornament
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment, ornament: () -> Content) -> some View](view/ornament(visibility:attachmentanchor:contentalignment:ornament:).md)
  Presents an ornament.
- [struct OrnamentAttachmentAnchor](ornamentattachmentanchor.md)
  An attachment anchor for an ornament.

## See Also

- [App organization](app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](documents.md)
  Enable people to open and manage documents.
- [Navigation](navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbars)*