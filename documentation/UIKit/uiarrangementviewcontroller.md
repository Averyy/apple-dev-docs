# UIArrangementViewController

**Framework**: UIKit  
**Kind**: class

A view controller that dynamically lays out primary and secondary view controllers based on size class, orientation, and reserved regions.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
class UIArrangementViewController
```

#### Overview

Use an arrangement view controller to lay out two related content view controllers differently depending on the current size classes, orientation, and status of reserved regions such as the fold on iPhone Duo. The arrangement view helps you improve how your app handles a folded display in addition to a flat display.

Because an arrangement view controller is a container that lays out other view controllers, avoid adding an arrangement view controller inside another container such as a scroll view, split view controller, collection view, or other container view that lays out other views. Also, avoid placing some container views inside an arrangement view controller, such as a split view controller or tab view controller.

When iPhone Duo is fully open or closed, people interact with the flat display like other iPhone and iPad models. An arrangement view controller is useful when:

- You want to place two views next to each other horizontally when someone is holding a device in landscape orientation or above and below each other when someone is holding a device in portrait orientation, without having to write conditional logic to switch between horizontal and vertical stacks.
- You want to adjust how much space each view takes when someone folds the display.
- You want to layer one view over another view on a flat display, and place the views next to each other when the device is folded. This arrangement works well when there’s a clear foreground and background relationship between your views, such as a view for video playback and a view with playback controls.

Arrangement view controllers offer two distinct types of arrangement: *split* and *overlay*. You specify the split arrangement to indicate the views lay out next to each other, either horizontally or vertically. You specify the overlay arrangement to indicate the views layer over each other on a flat display and next to each other on a folded display.

For more information on designing your app to use an arrangement view, see [`Designing for iPhone Duo`](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo).

#### Configure an Overlay Arrangement

An overlay arrangement view controller places a primary view controller and a secondary view controller in a stacked arrangement when the device has a flat display, or next to each other horizontally when someone is holding a device in landscape orientation or above and below each other when someone is holding a device in portrait orientation. Here’s how the overlay arrangement positions the primary and secondary views:

- In a stacked overlay arrangement, the arrangement places the primary view above the secondary view in the z-axis.
- When someone holds a folded iPhone Duo in landscape orientation, the arrangement places the secondary view in the leading position and the primary view in the trailing position.
- When someone holds a folded iPhone Duo in portrait orientation, the arrangement places the secondary view in the top position and the primary view in the bottom position.

Create an overlay arrangement view controller by specifying a primary and secondary view controller, and call the [`updateArrangement(_:animated:)`](uiarrangementviewcontroller/updatearrangement(_:animated:).md) method with [`overlay`](uiarrangementviewcontroller/arrangement/overlay.md) in Swift, or the [`updateArrangement:`](uiarrangementviewcontroller/updatearrangement:.md) method with [`overlayArrangement`](uioverlayarrangement-c.class/overlayarrangement.md) in Objective-C:

**Swift**:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.overlay)
```

**Objective-C**:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UIOverlayArrangement *arrangement = [UIOverlayArrangement overlayArrangement];
[self.arrangementVC updateArrangement:arrangement];
```

For more information on configuring layout for a folded iPhone Duo in an overlay arrangement, see [`Customize a folded layout`](uioverlayarrangement-c.class#Customize-a-folded-layout.md).

#### Configure a Split Arrangement

Unlike an overlay arrangement, which typically layers its two views and only separates them when the device folds, a split arrangement view always keeps its primary and secondary views in separate spaces: next to each other horizontally when someone is holding the device in landscape orientation, or stacked vertically when someone is holding the device in portrait orientation. Here’s how the split arrangement positions the primary and secondary views:

- In landscape orientation, the arrangement view places the primary view in the leading position and the secondary view in the trailing position.
- In portrait orientation, the arrangement view places the primary view in the top position and the secondary view in the bottom position.
- When someone is holding a closed iPhone Duo in landscape orientation, the split arrangement only shows the primary view.

Create a split arrangement by specifying a primary and secondary view controller, and call the [`updateArrangement(_:animated:)`](uiarrangementviewcontroller/updatearrangement(_:animated:).md) method with [`split`](uiarrangementviewcontroller/arrangement/split.md) in Swift, or the [`updateArrangement:`](uiarrangementviewcontroller/updatearrangement:.md) method with [`splitArrangement`](uisplitarrangement-c.class/splitarrangement.md) in Objective-C:

**Swift**:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.split)
```

**Objective-C**:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UISplitArrangement *arrangement = [UISplitArrangement splitArrangement];
[self.arrangementVC updateArrangement:arrangement];
```

For more information on adjusting view sizes in a split arrangement, see [`Adjust a split arrangement’s layout sizing`](uisplitarrangement-swift.struct#Adjust-a-split-arrangements-layout-sizing.md).

#### Limit an Arrangement By Orientation

You can limit which axes your split or overlay arrangement view controller supports by specifying the axes for the arrangement. The following example shows an arrangement that only splits vertically:

**Swift**:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.split.axes(.vertical))
```

**Objective-C**:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UISplitArrangement *arrangement = [UISplitArrangement splitArrangement];
arrangement.axes = UIAxisVertical;
[self.arrangementVC updateArrangement:arrangement];
```

Use [`axes(_:)`](uisplitarrangement-swift.struct/axes(_:).md) in Swift or [`axes`](uisplitarrangement-c.class/axes.md) in Objective-C to set the axes for a split arrangement, or [`axes(_:)`](uioverlayarrangement-swift.struct/axes(_:).md) in Swift or [`axes`](uioverlayarrangement-c.class/axes.md) in Objective-C to set the axes for an overlay arrangement.

## Topics

### Creating an arrangement view controller
- [init()](uiarrangementviewcontroller/init.md)
  Creates an arrangement view controller.
### Configuring the arrangement
- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [func updateArrangement<A>(A, animated: Bool)](uiarrangementviewcontroller/updatearrangement(_:animated:).md)
  Updates the arrangement of the view controller.
### Managing arrangement view controllers
- [UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](uiarrangementviewcontroller/viewcontroller(for:).md)
  Returns the view controller in the arrangement for the placement you provide.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](uiarrangementviewcontroller/setviewcontroller(_:for:animated:).md)
  Sets the view controller in the arrangement for the specific placement you provide.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](uiarrangementviewcontroller/placement(for:).md)
  Returns the placement for the view controller you provide in the arrangement.
### Getting view state
- [UIArrangementViewController.ViewState](uiarrangementviewcontroller/viewstate.md)
  The state of a view within an arrangement.
- [func state(for: UIArrangementViewController.ViewPlacement) -> UIArrangementViewController.ViewState?](uiarrangementviewcontroller/state(for:).md)
  Returns the view state for a placement in the arrangement.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
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
- [class UINavigationController](uinavigationcontroller.md)
  A container view controller that defines a stack-based scheme for navigating hierarchical content.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller)*