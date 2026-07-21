# Auxiliary view modifiers

**Framework**: SwiftUI

Add and configure supporting views, like toolbars and context menus.

#### Overview

Use these modifiers to manage supplemental views that present context-specific controls and information. For example, you can add titles and buttons to navigation bars, manage the status bar, create context menus, and add badges to many different kinds of views.

## Topics

### Navigation titles
- [Configure your apps navigation titles](configure-your-apps-navigation-titles.md)
  Use a navigation title to display the current navigation state of an interface.
- [func navigationTitle(_:)](view/navigationtitle(_:).md)
  Configures the view’s title for purposes of navigation, using a localized string resource.
- [func navigationSubtitle(_:)](view/navigationsubtitle(_:).md)
  Configures the view’s subtitle for purposes of navigation, using a localized string resource.
### Navigation title configuration
- [func navigationDocument(_:)](view/navigationdocument(_:).md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(_:preview:)](view/navigationdocument(_:preview:).md)
  Configures the view’s document for purposes of navigation.
### Navigation bars
- [func navigationBarBackButtonHidden(Bool) -> some View](view/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](view/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
### Navigation stacks and columns
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](view/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](view/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](view/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationLinkIndicatorVisibility(Visibility) -> some View](view/navigationlinkindicatorvisibility(_:).md)
  Configures whether navigation links show a disclosure indicator.
- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.
### Scroll view edges
- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](view/scrolledgeeffecthidden(_:for:).md)
  Hides any scroll edge effects for scroll views within this hierarchy.
### Tab views
- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](view/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultTabBarPlacement(AdaptableTabBarPlacement) -> some View](view/defaulttabbarplacement(_:).md)
  Specifies the preferred placement for the tabs of a [`TabView`](tabview.md) in the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown.
- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](view/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](view/tabviewbottomaccessory(content:).md)
  Places a view as the bottom accessory of the tab view.
- [func tabViewBottomAccessory<Content>(isEnabled: Bool, content: () -> Content) -> some View](view/tabviewbottomaccessory(isenabled:content:).md)
  Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](view/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSearchActivation(TabSearchActivation) -> some View](view/tabviewsearchactivation(_:).md)
  Configures the activation and deactivation behavior of search in the search tab.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
### Toolbars
- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func contentToolbar(for:content:)](view/contenttoolbar(for:content:).md)
  Populates the toolbar of the specified content view type with the views you provide.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](view/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](view/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarOverflowMenu<C>(content: () -> C) -> some View](view/toolbaroverflowmenu(content:).md)
  Configures the overflow menu of a toolbar.
- [func toolbarRole(ToolbarRole) -> some View](view/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarMinimizationBehavior(ToolbarMinimizationBehavior, for: ToolbarPlacement...) -> some View](view/toolbarminimizationbehavior(_:for:).md)
  Sets the minimize behavior for the specified bars.
- [func toolbarMinimizationRestoration(ToolbarMinimizationRestoration, for: ToolbarPlacement...) -> some View](view/toolbarminimizationrestoration(_:for:).md)
  Sets the restoration behavior for the specified bars during minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](view/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](view/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.
- [func ornament<Content>(visibility: Visibility, attachmentAnchor: OrnamentAttachmentAnchor, contentAlignment: Alignment3D, ornament: () -> Content) -> some View](view/ornament(visibility:attachmentanchor:contentalignment:ornament:).md)
  Presents an ornament.
### Context menus
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](view/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](view/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](view/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
### Badges
- [func badge(_:)](view/badge(_:).md)
  Generates a badge for the view from a localized string resource.
- [func badgeProminence(BadgeProminence) -> some View](view/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
### Lists
- [func sectionIndexLabel(_:)](view/sectionindexlabel(_:).md)
  Sets the label that is used in a section index to point to this section, typically only a single character long.
### Help text
- [func help(_:)](view/help(_:).md)
  Adds help text to a view using a localized string resource that you provide.
### Status bar
- [func statusBarHidden(Bool) -> some View](view/statusbarhidden(_:).md)
  Sets the visibility of the status bar.
### External displays
- [func sceneAccessory<C>(content: () -> C) -> some View](view/sceneaccessory(content:).md)
  Defines any scene accessories associated with `self`.
### Touch Bar
- [func touchBar<Content>(content: () -> Content) -> some View](view/touchbar(content:).md)
  Sets the content that the Touch Bar displays.
- [func touchBar<Content>(TouchBar<Content>) -> some View](view/touchbar(_:).md)
  Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [func touchBarItemPrincipal(Bool) -> some View](view/touchbaritemprincipal(_:).md)
  Sets principal views that have special significance to this Touch Bar.
- [func touchBarCustomizationLabel(Text) -> some View](view/touchbarcustomizationlabel(_:).md)
  Sets a user-visible string that identifies the view’s functionality.
- [func touchBarItemPresence(TouchBarItemPresence) -> some View](view/touchbaritempresence(_:).md)
  Sets the behavior of the user-customized view.

## See Also

- [Accessibility modifiers](view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Chart view modifiers](view-chart-view.md)
  Configure charts that you declare with Swift Charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-auxiliary-views)*