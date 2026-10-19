# UINavigationController

**Framework**: UIKit  
**Kind**: class

A container view controller that defines a stack-based scheme for navigating hierarchical content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UINavigationController
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
- [Managing content in your app’s windows](managing-content-in-your-app-s-windows.md)
- [About app development with UIKit](about-app-development-with-uikit.md)
- [Customizing the behavior of segue-based presentations](customizing-the-behavior-of-segue-based-presentations.md)
- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Overview

A navigation controller displays one view controller at a time. The ordered array of view controllers it manages forms the *navigation stack*. When you push a view controller onto the stack, it animates onscreen and covers the view controller that was previously on top.

A navigation interface reflects the structure of your app’s hierarchical data. For each level of the hierarchy, you provide a view controller that displays that level’s content. The following image shows an example in the Settings app. The root view controller displays top-level preference groups. Selecting a group reveals individual settings or additional subgroups. For every view except the root view controller, the navigation controller provides a Back button to return to the previous level.

![An image that shows three phones next to each other, each showing a view from the Settings app. The first shows the title Settings and a list of options, with an arrow pointing from Appearance to the second phone. The second shows Appearance settings, with an arrow pointing from Liquid Glass to the third phone. The third shows Liquid Glass settings.](/images/com.apple.uikit/uinavigationcontroller-01@2x.png)

The first view controller in the navigation stack is the root view controller and represents the bottom of the stack. The last view controller is the topmost item on the stack, and represents the view controller that the system is currently displaying. You add and remove view controllers from the stack using [`show(_:sender:)`](uiviewcontroller/show(_:sender:).md), [`pushViewController(_:animated:)`](uinavigationcontroller/pushviewcontroller(_:animated:).md), [`popViewController(animated:)`](uinavigationcontroller/popviewcontroller(animated:).md), segues, or other methods provided by this class. People can also remove the topmost view controller by tapping the Back button or performing a swipe gesture. When long-pressed, the Back button presents a hierarchical list of all view controllers people can return to.

A navigation controller coordinates its behavior with its [`delegate`](uinavigationcontroller/delegate.md) object. The delegate object can respond to the pushing or popping of view controllers and provide custom animation transitions. Provide a delegate object that conforms to the [`UINavigationControllerDelegate`](uinavigationcontrollerdelegate.md) protocol.

The following image shows the relationships between the navigation controller and the objects it manages. Use the specified properties of the navigation controller to access these objects.

![A diagram that illustrates objects a navigation controller contains and manages. On the left side of the diagram is a box titled UINavigationController. Inside the box are four boxes that each have arrows pointing to boxes outside the UINavigationController box. The first is titled viewControllers (NSArray), and points to three stacked boxes titled View controller, with the caption Navigation stack. The second is titled navigationBar, and points to a box titled UINavigationBar. The UINavigationBar box has an arrow with the caption delegate that points back to the UINavigationController box. The third box is titled toolbar, and points to a box titled UIToolbar. The fourth box is titled delegate, and points to a box titled Custom delegate object.](/images/com.apple.uikit/uinavigationcontroller-02@2x.png)

#### Manage the Navigation Bar and Toolbar

A navigation controller embeds the content of other view controllers in its own view, and it manages the creation, configuration, and display of its bars.

The following image shows how these views combine to form the navigation interface.

![A diagram that shows four parts of a list of emails in the Mail app. The first part on the left, with the caption Navigation view, shows the navigation bar, title, and subtitle at the top, empty space in the middle, and a toolbar with buttons and a search bar at the bottom. The second part, with the caption Custom view hierarchy, shows empty space at the top and a list of emails at the bottom. The third part, with the caption Window, shows empty space. The fourth part on the right, with the caption Assembled views, shows all the parts assembled together into one view, with the parts from the navigation view overlaying the email list.](/images/com.apple.uikit/uinavigationcontroller-03@2x.png)

Prefer using the provided bars and manage their content with [`navigationItem`](uiviewcontroller/navigationitem.md) and [`toolbarItems`](uiviewcontroller/toolbaritems.md). Don’t change the navigation bar’s [`frame`](uiview/frame.md), [`bounds`](uiview/bounds.md), or [`alpha`](uiview/alpha.md) values directly.

If you subclass [`UINavigationBar`](uinavigationbar.md), initialize your navigation controller using the [`init(navigationBarClass:toolbarClass:)`](uinavigationcontroller/init(navigationbarclass:toolbarclass:).md) method. To hide or show the navigation bar, use the [`isNavigationBarHidden`](uinavigationcontroller/isnavigationbarhidden.md) property or [`setNavigationBarHidden(_:animated:)`](uinavigationcontroller/setnavigationbarhidden(_:animated:).md) method.

> 💡 **Tip**: To prevent interfering with Liquid Glass in your navigation bar, avoid using custom backgrounds and [`UIAppearance`](uiappearance.md) APIs.

#### Update Navigation Controls

As people navigate your app, the navigation controller updates its bars. The top-level view controller on the navigation stack defines its navigation and toolbar items. Navigation controllers adapt their layout based on the current [`traitCollection`](uitraitenvironment/traitcollection.md).

##### Horizontal and Vertical Axes

In a horizontal layout, navigation controls appear across the top of the view and toolbars appear along the bottom. On iPhone Duo, the system considers whether your content is better suited for a vertical or horizontal axis. On a vertical axis, navigation controls and toolbar items, along with tab bar items, consolidate into a shared region as a unified vertical stack.

The following sections relate to navigation bar items on a horizontal axis. Designing for the horizontal axis allows your app to adapt for the vertical axis in ways people expect. In most cases, when moved to the vertical axis, horizontal bars effectively rotate 90 degrees to stack their content with the leading item at the top. For more detail on how bar items adjust to the vertical axis, watch [`Raise the bar with iPhone Duo`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/111462). For design guidance, see [`Vertical controls`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls) in Human Interface Guidelines > [`Designing for iPhone Duo`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo).

##### Leading Items

For all but the root view controller on the navigation stack, the leading-most item of the navigation bar provides navigation back to the previous view controller. The navigation controller determines the contents of this leading button as follows:

- If the new top-level view controller defines leading item groups, the navigation bar displays those groups. To specify leading item groups, set the [`leadingItemGroups`](uinavigationitem/leadingitemgroups.md) property of the view controller’s navigation item.
- If [`leftItemsSupplementBackButton`](uinavigationitem/leftitemssupplementbackbutton.md) is `true`, leading items display in addition to the Back button.
- If the top-level view controller doesn’t have a custom leading item, but the navigation item of the previous view controller has an object in its [`backBarButtonItem`](uinavigationitem/backbarbuttonitem.md) property, the navigation bar displays that item.
- If leading items aren’t specified by either of the view controllers, the system uses a default Back button that displays a back image.

When a Back button’s title is too long to fit, the navigation bar displays a back image, but only when the previous view controller provides the Back button. If the new top-level view controller instead has a leading item, the navigation bar doesn’t change that item’s title. If the item’s title is too long to fit, the navigation bar places it in the menu of the overflow item on the trailing edge.

##### Center Items

The navigation controller updates the center of the navigation bar as follows:

- If the new top-level view controller has a custom title view, the navigation bar displays that view in place of the default title view. To specify a custom title view, set the [`titleView`](uinavigationitem/titleview.md) property of the view controller’s navigation item.
- If you don’t set a custom title view, the navigation bar displays a label containing the view controller’s default title. The string for this label is usually obtained from the [`title`](uiviewcontroller/title.md) property of the view controller itself. If you want to display a different title than the one associated with the view controller, set the [`title`](uinavigationitem/title.md) property of the view controller’s navigation item instead. If you want to change the appearance of the title, such as its font or color, use [`attributedTitle`](uinavigationitem/attributedtitle-25fxb.md).
- If you set [`style`](uinavigationitem/style.md) to [`UINavigationItem.ItemStyle.browser`](uinavigationitem/itemstyle/browser.md) or [`UINavigationItem.ItemStyle.editor`](uinavigationitem/itemstyle/editor.md), the navigation item’s title appears on the leading side of the navigation bar, and center items appear in the center of the bar when space is available. To specify center item groups, set the [`centerItemGroups`](uinavigationitem/centeritemgroups.md) property of the view controller’s navigation item.

##### Trailing Items

The navigation controller updates the trailing side of the navigation bar as follows:

- If the new top-level view controller defines trailing item groups, the navigation bar displays those groups. To specify trailing item groups, set the [`trailingItemGroups`](uinavigationitem/trailingitemgroups.md) property of the view controller’s navigation item.
- If the view controller has no custom trailing items, the trailing edge of the navigation bar is empty.
- If leading or center items don’t fit, the navigation bar moves them into an overflow item on the trailing edge, whether or not the view controller has custom trailing items. The overflow item is a button with an ellipsis that opens a menu of the items that moved.

#### Display a Toolbar

A navigation controller object manages an optional toolbar in its view hierarchy. When the navigation controller displays this toolbar, the toolbar obtains its current items from the [`toolbarItems`](uiviewcontroller/toolbaritems.md) property of the active view controller. When the active view controller changes, the navigation controller updates the toolbar items to match the new view controller, animating the new items into position when appropriate.

The toolbar is hidden by default. To hide or show it, use the [`isToolbarHidden`](uinavigationcontroller/istoolbarhidden.md) property or [`setToolbarHidden(_:animated:)`](uinavigationcontroller/settoolbarhidden(_:animated:).md) method of your navigation controller object. Prefer the provided toolbar so the system can decide whether a vertical or horizontal axis better suits your content. To use a custom [`UIToolbar`](uitoolbar.md) subclass, initialize the navigation controller using the [`init(navigationBarClass:toolbarClass:)`](uinavigationcontroller/init(navigationbarclass:toolbarclass:).md) method.

#### Handle Orientation and Presentation Context

A navigation controller supports the following behaviors for its interface:

- **Supported interface orientations**: A navigation controller object doesn’t consult the view controllers on its navigation stack when determining the supported interface orientations. On iPhone and the outer display of iPhone Duo, a navigation controller supports all orientations except portrait upside-down. On iPad and the inner display of iPhone Duo, a navigation controller supports all orientations. If the navigation controller has a delegate object, the delegate can specify a different set of supported orientations using the [`navigationControllerSupportedInterfaceOrientations(_:)`](uinavigationcontrollerdelegate/navigationcontrollersupportedinterfaceorientations(_:).md) method.
- **Presentation context**: A navigation controller defines the presentation context for modally presented view controllers. When [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) is [`UIModalPresentationStyle.currentContext`](uimodalpresentationstyle/currentcontext.md) or [`UIModalPresentationStyle.overCurrentContext`](uimodalpresentationstyle/overcurrentcontext.md), modal presentations from the view controllers in the navigation stack cover the entire navigation interface.

#### Preserve Navigation State

When you assign a value to a navigation controller’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve itself and the contained view controllers on its navigation stack. The navigation controller starts at the bottom of the stack and moves upward, encoding each view controller that also has a valid restoration identifier string. During the next launch, the navigation controller restores the preserved view controllers to the navigation stack in the same order it preserved them.

The view controllers you push onto the navigation stack can use the same restoration identifiers. The navigation controller automatically stores additional information to ensure that each view controller’s restoration path is unique.

For more information about how state preservation and restoration work, see [`Preserving your app’s UI across launches`](preserving-your-app-s-ui-across-launches.md).

## Topics

### Creating a navigation controller
- [init(rootViewController: UIViewController)](uinavigationcontroller/init(rootviewcontroller:).md)
  Initializes and returns a newly created navigation controller.
- [init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)](uinavigationcontroller/init(navigationbarclass:toolbarclass:).md)
  Initializes and returns a newly created navigation controller that uses your custom bar subclasses.
- [init(nibName: String?, bundle: Bundle?)](uinavigationcontroller/init(nibname:bundle:).md)
  Creates a navigation controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uinavigationcontroller/init(coder:).md)
  Creates a navigation controller from data in an unarchiver.
### Customizing the navigation interface behavior
- [var delegate: (any UINavigationControllerDelegate)?](uinavigationcontroller/delegate.md)
  The delegate of the navigation controller object.
- [protocol UINavigationControllerDelegate](uinavigationcontrollerdelegate.md)
  The interface for an object that serves as a navigation controller’s delegate.
### Accessing items on the navigation stack
- [var topViewController: UIViewController?](uinavigationcontroller/topviewcontroller.md)
  The view controller at the top of the navigation stack.
- [var visibleViewController: UIViewController?](uinavigationcontroller/visibleviewcontroller.md)
  The view controller associated with the currently visible view in the navigation interface.
- [var viewControllers: [UIViewController]](uinavigationcontroller/viewcontrollers.md)
  The view controllers currently on the navigation stack.
- [func setViewControllers([UIViewController], animated: Bool)](uinavigationcontroller/setviewcontrollers(_:animated:).md)
  Replaces the view controllers currently managed by the navigation controller with the specified items.
### Pushing and popping stack items
- [func pushViewController(UIViewController, animated: Bool)](uinavigationcontroller/pushviewcontroller(_:animated:).md)
  Pushes a view controller onto the receiver’s stack and updates the display.
- [func popViewController(animated: Bool) -> UIViewController?](uinavigationcontroller/popviewcontroller(animated:).md)
  Pops the top view controller from the navigation stack and updates the display.
- [func popToRootViewController(animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptorootviewcontroller(animated:).md)
  Pops all the view controllers on the stack except the root view controller and updates the display.
- [func popToViewController(UIViewController, animated: Bool) -> [UIViewController]?](uinavigationcontroller/poptoviewcontroller(_:animated:).md)
  Pops view controllers until the specified view controller is at the top of the navigation stack.
- [var interactivePopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivepopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person swipes from the leading screen edge.
- [var interactiveContentPopGestureRecognizer: UIGestureRecognizer?](uinavigationcontroller/interactivecontentpopgesturerecognizer.md)
  The gesture recognizer that handles interactively popping the top view controller off the navigation stack when a person pans horizontally in the view.
### Configuring navigation bars
- [var navigationBar: UINavigationBar](uinavigationcontroller/navigationbar.md)
  The navigation bar managed by the navigation controller.
- [func setNavigationBarHidden(Bool, animated: Bool)](uinavigationcontroller/setnavigationbarhidden(_:animated:).md)
  Sets whether the navigation bar is hidden.
- [Customizing your app’s navigation bar](customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.
### Configuring custom toolbars
- [var toolbar: UIToolbar!](uinavigationcontroller/toolbar.md)
  The custom toolbar associated with the navigation controller.
- [func setToolbarHidden(Bool, animated: Bool)](uinavigationcontroller/settoolbarhidden(_:animated:).md)
  Changes the visibility of the navigation controller’s built-in toolbar.
- [var isToolbarHidden: Bool](uinavigationcontroller/istoolbarhidden.md)
  A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [class let hideShowBarDuration: CGFloat](uinavigationcontroller/hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.
### Hiding the navigation bar
- [var hidesBarsOnTap: Bool](uinavigationcontroller/hidesbarsontap.md)
  A Boolean value indicating whether the navigation controller allows hiding of its bars using a tap gesture.
- [var hidesBarsOnSwipe: Bool](uinavigationcontroller/hidesbarsonswipe.md)
  A Boolean value indicating whether the navigation bar hides its bars in response to a swipe gesture.
- [var hidesBarsWhenVerticallyCompact: Bool](uinavigationcontroller/hidesbarswhenverticallycompact.md)
  A Boolean value indicating whether the navigation controller hides its bars in a vertically compact environment.
- [var hidesBarsWhenKeyboardAppears: Bool](uinavigationcontroller/hidesbarswhenkeyboardappears.md)
  A Boolean value indicating whether the navigation controller hides its bars when the keyboard appears.
- [var isNavigationBarHidden: Bool](uinavigationcontroller/isnavigationbarhidden.md)
  A Boolean value that indicates whether the navigation bar is hidden.
- [var barHideOnTapGestureRecognizer: UITapGestureRecognizer](uinavigationcontroller/barhideontapgesturerecognizer.md)
  The gesture recognizer used to hide and show the navigation and toolbar.
- [var barHideOnSwipeGestureRecognizer: UIPanGestureRecognizer](uinavigationcontroller/barhideonswipegesturerecognizer.md)
  The gesture recognizer used to hide the navigation bar and toolbar.
### Displaying view controllers
- [func show(UIViewController, sender: Any?)](uinavigationcontroller/show(_:sender:).md)
  Presents the specified view controller in the navigation interface.
- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)
  Use the fluid zoom transition to provide a continuously interactive and responsive experience in your app.
- [var preferredTransition: UIViewController.Transition?](uiviewcontroller/preferredtransition.md)
  An object that defines the transition animation when switching to the view controller.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Inherited By
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIVideoEditorController](uivideoeditorcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationBar](uinavigationbar.md)
  A region that displays the title and controls provided by navigation items.
- [class UINavigationItem](uinavigationitem.md)
  The items that a navigation bar displays when the associated view controller is visible.
- [class UITabBarController](uitabbarcontroller.md)
  A container view controller that manages a multiselection interface, where the selection determines which child view controller to display.
- [class UITabBar](uitabbar.md)
  A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [class UITabBarItem](uitabbaritem.md)
  An object that describes an item in a tab bar.
- [class UITab](uitab.md)
  An object that manages a tab in a tab bar.
- [class UITabAccessory](uitabaccessory.md)
- [class UISearchTab](uisearchtab.md)
  A tab subclass that represents the system’s search tab.
- [class UITabGroup](uitabgroup.md)
  An object that manages a collection of tab objects.
- [class UIPageViewController](uipageviewcontroller.md)
  A container view controller that manages navigation between pages of content, where a subview controller manages each page.
- [class UIArrangementViewController](uiarrangementviewcontroller.md)
  A view controller that dynamically lays out primary and secondary view controllers based on size class, orientation, and reserved regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller)*