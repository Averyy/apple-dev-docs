# UINavigationBar

**Framework**: UIKit  
**Kind**: class

Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UINavigationBar
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

A [`UINavigationBar`](uinavigationbar.md) object is a bar, typically displayed at the top of the window, containing buttons for navigating within a hierarchy of screens. The primary components are a left (back) button, a center title, and an optional right button. You can use a navigation bar as a standalone object or in conjunction with a navigation controller object.

![A diagram that identifies the primary components of a navigation bar, including the back item title that connects to the previous view controller, shown on the left side of the diagram, the top item title of the navigation bar and the navigation bar prompt in the middle, and the right bar button item, with the text Done.](https://docs-assets.developer.apple.com/published/eac8a05db61b89a933c041e28611cde9/media-2759891%402x.png)

A navigation bar is most commonly used within a navigation controller. The [`UINavigationController`](uinavigationcontroller.md) object creates, displays, and manages its associated navigation bar, and uses attributes of the view controllers you add to control the content displayed in the navigation bar.

To control a navigation bar when using a navigation controller, the following steps are required:

- Create a navigation controller in Interface Builder or in the code.
- Configure the appearance of the navigation bar using the [`navigationBar`](uinavigationcontroller/navigationbar.md) property on the [`UINavigationController`](uinavigationcontroller.md) object.
- Control the content of the navigation bar by setting the [`title`](uiviewcontroller/title.md) and [`navigationItem`](uiviewcontroller/navigationitem.md) properties on each [`UIViewController`](uiviewcontroller.md) you push onto the navigation controller’s stack.

You can also use a standalone navigation bar, without using a navigation controller. To add a navigation bar to your interface, the following steps are required:

- Set up Auto Layout rules to govern the position of the navigation bar in your interface.
- Create a root navigation item to supply the initial title.
- Configure a delegate object to handle user interactions with the navigation bar.
- Customize the appearance of the navigation bar.
- Configure your app to push and pop relevant navigation items as the user navigates through the hierarchical screens.

##### Use a Navigation Bar with a Navigation Controller

If you use a navigation controller to manage the navigation between different screens of content, the navigation controller creates a navigation bar automatically and pushes and pops navigation items when appropriate.

A navigation controller uses the [`navigationItem`](uiviewcontroller/navigationitem.md) property on [`UIViewController`](uiviewcontroller.md) to provide the model objects to its navigation bar when navigating a stack of view controllers. The default navigation item uses the view controller’s title, but you can override the [`navigationItem`](uiviewcontroller/navigationitem.md) on a [`UIViewController`](uiviewcontroller.md) subclass to gain complete control of the navigation bar’s content.

A navigation controller automatically assigns itself as the delegate of its navigation bar object. Therefore, when using a navigation controller, don’t assign a custom delegate object to the corresponding navigation bar.

To access the navigation bar associated with a navigation controller, use the [`navigationBar`](uinavigationcontroller/navigationbar.md) property on [`UINavigationController`](uinavigationcontroller.md). See [`Customize the appearance of a navigation bar`](uinavigationbar#Customize-the-appearance-of-a-navigation-bar.md) for details on how to customize the appearance of a navigation bar.

For information about navigation controllers, see [`UINavigationController`](uinavigationcontroller.md).

##### Add Content to a Standalone Navigation Bar

In the vast majority of scenarios you use a navigation bar as part of a navigation controller. However, there are situations for which you might want to use the navigation bar UI and implement your own approach to content navigation. In these situations, you can use a standalone navigation bar.

When you use a navigation bar as a standalone object, you’re responsible for providing its content. Unlike other types of views, you don’t add subviews to a navigation bar directly. Instead, you use a navigation item (an instance of the [`UINavigationItem`](uinavigationitem.md) class) to specify what buttons or custom views you want displayed. A navigation item has properties for specifying views on the left, right, and center of the navigation bar and for specifying a custom prompt string.

A navigation bar manages a stack of [`UINavigationItem`](uinavigationitem.md) objects. Although the stack is there mostly to support navigation controllers, you can use it to implement your own custom navigation interface. The topmost item in the stack represents the navigation item whose contents are currently displayed by the navigation bar. You push new navigation items onto the stack using the [`pushItem(_:animated:)`](uinavigationbar/pushitem(_:animated:).md) method and pop items off the stack using the [`popItem(animated:)`](uinavigationbar/popitem(animated:).md) method. Both of these changes can be animated for the benefit of the user.

In addition to pushing and popping items, you can also set the contents of the stack directly using either the [`items`](uinavigationbar/items.md) property or the [`setItems(_:animated:)`](uinavigationbar/setitems(_:animated:).md) method. You might use this method at launch time to restore your interface to its previous state or to push or pop more than one navigation item at a time. The following figure shows the part of the [`UINavigationBar`](uinavigationbar.md) API responsible for managing the stack of navigation items.

![A flowchart diagram of the navigation bar and a stack of navigation items. A new navigation item enters the navigation bar from the left side of the diagram. In the center, the UINavigationBar contains properties that provide access to items in the stack, and methods that allow mutation by pushing on and popping off the stack, depicted on the right of the diagram.](https://docs-assets.developer.apple.com/published/22a4cdb2afd3e24633e4a5ec88b1c4ae/media-2759892%402x.png)

If you’re using a navigation bar as a standalone object, assign a custom delegate object to the [`delegate`](uinavigationbar/delegate.md) property and use that object to intercept messages coming from the navigation bar. Delegate objects must conform to the [`UINavigationBarDelegate`](uinavigationbardelegate.md) protocol. The delegate notifications let you track when navigation items are pushed or popped from the stack. You use these notifications to update the rest of your app’s user interface.

For more information about creating navigation items, see [`UINavigationItem`](uinavigationitem.md). For more information about implementing a delegate object, see [`UINavigationBarDelegate`](uinavigationbardelegate.md).

##### Customize the Appearance of a Navigation Bar

Navigation bars have two standard appearance styles: white with dark text or black with light text. Use the [`barStyle`](uinavigationbar/barstyle.md) property to select the style. Any changes you make to other navigation bar appearance properties override those inferred from the bar style.

Navigation bars are translucent by default; their background color is semitransparent. You can make the navigation bar opaque by setting the [`isTranslucent`](uinavigationbar/istranslucent.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

You can specify a custom tint color for a navigation bar background using the [`barTintColor`](uinavigationbar/bartintcolor.md) property. Setting this property overrides the default color inferred from the bar style. As with all [`UIView`](uiview.md) subclasses, you can control the color of the interactive elements within navigation bars, including button images and titles, using the [`tintColor`](uiview/tintcolor.md) property.

The [`titleTextAttributes`](uinavigationbar/titletextattributes.md) property specifies the attributes for displaying the bar’s title text. You can specify the font, text color, text shadow color, and text shadow offset for the title in the text attributes dictionary using the [`NSFontAttributeName`](nsfontattributename.md), [`NSForegroundColorAttributeName`](nsforegroundcolorattributename.md), and [`NSShadowAttributeName`](nsshadowattributename.md) keys. For more information about string-formatting attributes, see `Character Attributes`.

Use the [`setTitleVerticalPositionAdjustment(_:for:)`](uinavigationbar/settitleverticalpositionadjustment(_:for:).md) method to adjust the vertical position of the title. This method allows you to specify the adjustment dependent on the bar height, which is represented by the [`UIBarMetrics`](uibarmetrics.md) enum. The following figure shows a navigation bar with custom tint color, title text attributes, and bar tint color.

![A navigation bar diagram that depicts the fonts, color, and layout of a navigation bar, including the tint color, title text attributes, bar tint color, and the title vertical position.](https://docs-assets.developer.apple.com/published/ba68ec16c51161060a4894d0ea2586e6/media-2759893%402x.png)

To allow complete customization over the appearance of navigation bars, you can additionally provide custom background and shadow images. To provide a custom background image, use the [`setBackgroundImage(_:for:barMetrics:)`](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md) method, providing a [`UIImage`](uiimage.md) object for the appropriate bar position and metrics values. Use a [`UIBarPosition`](uibarposition.md) value for the bar position argument to specify whether to use the supplied image at the bottom or the top of the window, and if it appears at the top, whether to extend it upward under the status bar. Similarly, you can specify that the image should be used for either compact or default bar metrics, with or without a prompt, by providing a [`UIBarMetrics`](uibarmetrics.md) value to the bar metrics argument.

To add a shadow, provide a resizable [`UIImage`](uiimage.md) to the [`shadowImage`](uinavigationbar/shadowimage.md) property. To use the custom shadow image, you need to have specified a custom background image. The following figure shows a navigation bar with a custom background image, supplied using [`setBackgroundImage(_:for:barMetrics:)`](uinavigationbar/setbackgroundimage(_:for:barmetrics:).md) with a bar position value of [`UIBarPosition.topAttached`](uibarposition/topattached.md) and a bar metrics value of [`UIBarMetrics.default`](uibarmetrics/default.md). A custom image has also been provided to the [`shadowImage`](uinavigationbar/shadowimage.md) property.

![A screenshot of a navigation bar with the location of a background image and a shadow image labeled.](https://docs-assets.developer.apple.com/published/d1fcd89059fad88c63657b42c2e75548/media-2759894%402x.png)

To see examples of customizing a navigation bar, see [`Customizing your app’s navigation bar`](customizing-your-app-s-navigation-bar.md).

##### Customize a Navigation Bar with Interface Builder

The following table lists the core attributes that you configure for navigations bars in the Attributes Inspector within Interface Builder.

| Attribute | Description |
| --- | --- |
| Style | Specifies the UI bar style to apply to the navigation bar. The bar style controls the title color and the bar tint color, but you can override it by providing values for those attributes. Select Translucent to make the navigation bar semitransparent. Access these values at runtime with the [`barStyle`](uinavigationbar/barstyle.md) and [`isTranslucent`](uinavigationbar/istranslucent.md) properties. |
| Bar Tint | Controls the tint color of the navigation bar. This overrides the value implied by the Style attribute. If the Translucent attribute is selected, the Bar Tint color is automatically made semitransparent. Access this value at runtime with the [`barTintColor`](uinavigationbar/bartintcolor.md) property. |
| Shadow Image | Represents the image used as a shadow beneath the navigation bar. This image is stretched horizontally to match the width of the bar. Access this value at runtime with the [`shadowImage`](uinavigationbar/shadowimage.md) property. |
| Back Image | Specifies the image that appears at the leading edge of the back button. This attribute must be used in combination with the Back Mask attribute. Access this value at runtime with the [`backIndicatorImage`](uinavigationbar/backindicatorimage.md) property. |
| Back Mask | Specifies the mask associated with the Back Image attribute. This is used to control the appearance of the Back button during animated transitions, and therefore must be used in conjunction with the Back Image attribute. Access this value at runtime with the [`backIndicatorTransitionMaskImage`](uinavigationbar/backindicatortransitionmaskimage.md) property. |

The following table lists the Interface Builder attributes that affect the appearance of the navigation bar’s title.

| Attribute | Description |
| --- | --- |
| Title Font | The font used to render the title in the center of the navigation bar. Access this value at runtime with the value stored against the [`NSFontAttributeName`](nsfontattributename.md) key in the dictionary in the [`titleTextAttributes`](uinavigationbar/titletextattributes.md) property. |
| Title Color | The color used to render the navigation bar title. Access this value at runtime using the [`NSForegroundColorAttributeName`](nsforegroundcolorattributename.md) key in the dictionary in the [`titleTextAttributes`](uinavigationbar/titletextattributes.md) property. |
| Title Shadow | Specifies the color and offset of the shadow used when rendering the navigation bar’s title. Access these values at runtime with the dictionary in the [[`titleTextAttributes`](uinavigationbar/titletextattributes.md)] property, using the [`NSShadowAttributeName`](nsshadowattributename.md) key. |

##### Internationalize a Navigation Bar

To internationalize navigation bars, specify a localized string for each of the displayed string properties of the navigation item model objects.

For more information about internationalizing your interface, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

##### Make a Navigation Bar Accessible

Navigation bars are accessible by default. The default accessibility trait for a navigation bar is User Interaction Enabled.

With VoiceOver enabled on an iOS device, after the user navigates to a new view in the hierarchy, VoiceOver reads the navigation bar’s title, followed by the name of the left bar button item. When the user taps an element in a navigation bar, VoiceOver reads the name and the type of the element; for example, “General back button,” “Keyboard heading,” and “Edit button.”

For general information about making your interface accessible, see [`Accessibility Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785).

## Topics

### Responding to navigation bar changes
- [var delegate: (any UINavigationBarDelegate)?](uinavigationbar/delegate.md)
  The navigation bar’s delegate object.
- [protocol UINavigationBarDelegate](uinavigationbardelegate.md)
  Methods that a navigation bar calls before and after it modifies its stack of navigation items.
### Pushing and popping items
- [func pushItem(UINavigationItem, animated: Bool)](uinavigationbar/pushitem(_:animated:).md)
  Pushes the given navigation item onto the navigation bar’s stack and updates the UI.
- [func popItem(animated: Bool) -> UINavigationItem?](uinavigationbar/popitem(animated:).md)
  Pops the top item from the navigation bar’s stack and updates the UI.
- [func setItems([UINavigationItem]?, animated: Bool)](uinavigationbar/setitems(_:animated:).md)
  Replaces the navigation items currently managed by the navigation bar with the specified items.
- [var items: [UINavigationItem]?](uinavigationbar/items.md)
  An array of navigation items managed by the navigation bar.
- [var topItem: UINavigationItem?](uinavigationbar/topitem.md)
  The navigation item at the top of the navigation bar’s stack.
- [var backItem: UINavigationItem?](uinavigationbar/backitem.md)
  The navigation item that is immediately below the topmost item on a navigation bar’s stack.
### Customizing the bar’s appearance
- [var prefersLargeTitles: Bool](uinavigationbar/preferslargetitles.md)
  A Boolean value that indicates whether the title displays in a large format.
- [var standardAppearance: UINavigationBarAppearance](uinavigationbar/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](uinavigationbar/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](uinavigationbar/scrolledgeappearance.md)
  The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](uinavigationbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var isTranslucent: Bool](uinavigationbar/istranslucent.md)
  A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](uinavigationbar-legacy-customizations.md)
  Customize appearance information directly on the navigation bar object.
### Building with Mac Catalyst
- [var behavioralStyle: UIBehavioralStyle](uinavigationbar/behavioralstyle.md)
  The behavioral style of the navigation bar.
- [var preferredBehavioralStyle: UIBehavioralStyle](uinavigationbar/preferredbehavioralstyle.md)
  The preferred behavioral style of the navigation bar.
- [var currentNSToolbarSection: UINavigationBar.NSToolbarSection](uinavigationbar/currentnstoolbarsection.md)
  The toolbar section that the navigation bar is currently using.
- [UINavigationBar.NSToolbarSection](uinavigationbar/nstoolbarsection.md)
  Constants that determine how the system hosts the navigation bar in an AppKit toolbar.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIBarPositioning](uibarpositioning.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)
  Create a composite interface by combining content from one or more view controllers with other custom views.
- [class UISplitViewController](uisplitviewcontroller.md)
  A container view controller that implements a hierarchical interface.
- [class UINavigationController](uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar)*