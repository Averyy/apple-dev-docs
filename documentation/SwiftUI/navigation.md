# Navigation

**Framework**: SwiftUI

Enable people to move between different parts of your app’s view hierarchy within a scene.

#### Overview

Use navigation containers to provide structure to your app’s user interface, enabling people to easily move among the parts of your app.

![None](https://docs-assets.developer.apple.com/published/f89769a3e08273224563454dc8f3ce0d/navigation-hero%402x.png)

For example, people can move forward and backward through a stack of views using a [`NavigationStack`](navigationstack.md), or choose which view to display from a tab bar using a [`TabView`](tabview.md).

Configure navigation containers by adding view modifiers like [`navigationSplitViewStyle(_:)`](view/navigationsplitviewstyle(_:).md) to the container. Use other modifiers on the views inside the container to affect the container’s behavior when showing that view. For example, you can use [`navigationTitle(_:)`](view/navigationtitle(_:).md) on a view to provide a toolbar title to display when showing that view.

## Topics

### Essentials
- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)
  Learn about the navigation stack, links, and how to manage navigation types in your app’s structure.
### Presenting views in columns
- [Bringing robust navigation structure to your SwiftUI app](bringing-robust-navigation-structure-to-your-swiftui-app.md)
  Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](migrating-to-new-navigation-types.md)
  Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [struct NavigationSplitView](navigationsplitview.md)
  A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](view/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [struct NavigationSplitViewVisibility](navigationsplitviewvisibility.md)
  The visibility of the leading columns in a navigation split view.
- [struct NavigationLink](navigationlink.md)
  A view that controls a navigation presentation.
### Stacking views in one column
- [struct NavigationStack](navigationstack.md)
  A view that displays a root view and enables you to present additional views over the root view.
- [struct NavigationPath](navigationpath.md)
  A type-erased list of data representing the content of a navigation stack.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](view/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](view/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
### Managing column collapse
- [struct NavigationSplitViewColumn](navigationsplitviewcolumn.md)
  A view that represents a column in a navigation split view.
### Setting titles for navigation content
- [func navigationTitle(_:)](view/navigationtitle(_:).md)
  Configures the view’s title for purposes of navigation, using a string binding.
- [func navigationSubtitle(_:)](view/navigationsubtitle(_:).md)
  Configures the view’s subtitle for purposes of navigation.
- [func navigationDocument(_:)](view/navigationdocument(_:).md)
  Configures the view’s document for purposes of navigation.
- [func navigationDocument(_:preview:)](view/navigationdocument(_:preview:).md)
  Configures the view’s document for purposes of navigation.
### Configuring the navigation bar
- [func navigationBarBackButtonHidden(Bool) -> some View](view/navigationbarbackbuttonhidden(_:).md)
  Hides the navigation bar back button for the view.
- [func navigationBarTitleDisplayMode(NavigationBarItem.TitleDisplayMode) -> some View](view/navigationbartitledisplaymode(_:).md)
  Configures the title display mode for this view.
- [struct NavigationBarItem](navigationbaritem.md)
  A configuration for a navigation bar that represents a view at the top of a navigation stack.
### Configuring the sidebar
- [var sidebarRowSize: SidebarRowSize](environmentvalues/sidebarrowsize.md)
  The current size of sidebar rows.
- [enum SidebarRowSize](sidebarrowsize.md)
  The standard sizes of sidebar rows.
### Presenting views in tabs
- [Enhancing your app’s content with tab navigation](enhancing-your-app-content-with-tab-navigation.md)
  Keep your app content front and center while providing quick access to navigation using the tab bar.
- [struct TabView](tabview.md)
  A view that switches between multiple child views using interactive user interface elements.
- [struct Tab](tab.md)
  The content for a tab and the tab’s associated tab item in a tab view.
- [struct TabRole](tabrole.md)
  A value that defines the purpose of the tab.
- [struct TabSection](tabsection.md)
  A container that you can use to add hierarchy within a tab view.
- [func tabViewStyle<S>(S) -> some View](view/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.
### Configuring a tab bar
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [struct AdaptableTabBarPlacement](adaptabletabbarplacement.md)
  A placement for tabs in a tab view using the adaptable sidebar style.
- [var tabBarPlacement: TabBarPlacement?](environmentvalues/tabbarplacement.md)
  The current placement of the tab bar.
- [struct TabBarPlacement](tabbarplacement.md)
  A placement for tabs in a tab view.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [struct TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [enum TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md)
  A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
### Configuring a tab
- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.
- [struct TabPlacement](tabplacement.md)
  A place that a tab can appear.
- [struct TabContentBuilder](tabcontentbuilder.md)
  A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [protocol TabContent](tabcontent.md)
  A type that provides content for programmatically selectable tabs in a tab view.
- [struct AnyTabContent](anytabcontent.md)
  Type erased tab content.
### Enabling tab customization
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](view/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [struct TabViewCustomization](tabviewcustomization.md)
  The customizations a person makes to an adaptable sidebar tab view.
- [struct TabCustomizationBehavior](tabcustomizationbehavior.md)
  The customization behavior of customizable tab view content.
### Displaying views in multiple panes
- [struct HSplitView](hsplitview.md)
  A layout container that arranges its children in a horizontal line and allows the user to resize them using dividers placed between them.
- [struct VSplitView](vsplitview.md)
  A layout container that arranges its children in a vertical line and allows the user to resize them using dividers placed between them.
### Deprecated Types
- [struct NavigationView](navigationview.md)
  A view for presenting a stack of views that represents a visible path in a navigation hierarchy.
- [func tabItem<V>(() -> V) -> some View](view/tabitem(_:).md)
  Sets the tab bar item associated with this view.

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
- [Modal presentations](modal-presentations.md)
  Present content in a separate view that offers focused interaction.
- [Toolbars](toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](search.md)
  Enable people to search for text or other content within your app.
- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigation)*