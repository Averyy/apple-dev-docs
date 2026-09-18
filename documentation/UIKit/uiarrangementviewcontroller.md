# UIArrangementViewController

**Framework**: UIKit  
**Kind**: class

A view controller that presents its container view controllers through an arrangement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
class UIArrangementViewController
```

#### Overview

You create an arrangement view controller and set a primary and secondary view controller. The arrangement view controller computes a layout for its content based on the context it is presented in, including the available size, size class, and hardware features.

Use [`updateArrangement(_:animated:)`](uiarrangementviewcontroller/updatearrangement(_:animated:).md) to choose how the arrangement view lays out its content. The default style is [`UISplitArrangement`](uisplitarrangement-swift.struct.md). The other built-in style is [`UIOverlayArrangement`](uioverlayarrangement-swift.struct.md).

##### Overlay Arrangements

An overlay arrangement layers the primary view on top of the secondary view in z-order. This layout is well-suited for full-screen experiences like media players, where playback controls overlay a video surface:

**Swift**:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.overlay.axes(.horizontal))
```

**Objective-C**:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UIOverlayArrangement *arrangement = [UIOverlayArrangement overlayArrangement];
arrangement.axes = UIAxisHorizontal;
[self.arrangementVC updateArrangement:arrangement];
```

When the environment changes, such as when a foldable device is folded, the overlay arrangement can transition its views from a layered layout into a side-by-side layout. Use [`axes(_:)`](uioverlayarrangement-swift.struct/axes(_:).md) to control which axes are supported.

##### Split Arrangements

A split arrangement places the primary and secondary views side-by-side along one or more axes. Use this layout for experiences that display two distinct pieces of content simultaneously, such as a music player alongside its lyrics:

**Swift**:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.split.axes(.horizontal))
```

**Objective-C**:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UISplitArrangement *arrangement = [UISplitArrangement splitArrangement];
arrangement.axes = UIAxisHorizontal;
[self.arrangementVC updateArrangement:arrangement];
```

The split arrangement adapts its axis based on the available size and size class. You can constrain which axes the split supports using [`axes(_:)`](uisplitarrangement-swift.struct/axes(_:).md).

## Topics

### Creating an arrangement view controller
- [init()](uiarrangementviewcontroller/init.md)
  Creates an arrangement view controller.
### Configuring the arrangement
- [UIArrangementViewController.Arrangement](uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that overlays views.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that splits views.
- [func updateArrangement<A>(A, animated: Bool)](uiarrangementviewcontroller/updatearrangement(_:animated:).md)
  Updates the arrangement of the view controller.
### Managing arrangement view controllers
- [UIArrangementViewController.ViewPlacement](uiarrangementviewcontroller/viewplacement.md)
  A placement of a view controller within an arrangement view controller.
- [func viewController(for: UIArrangementViewController.ViewPlacement) -> UIViewController?](uiarrangementviewcontroller/viewcontroller(for:).md)
  The view controller in the arrangement for the provided placement.
- [func setViewController(UIViewController?, for: UIArrangementViewController.ViewPlacement, animated: Bool)](uiarrangementviewcontroller/setviewcontroller(_:for:animated:).md)
  Sets the view controller in the arrangement for a specific placement.
- [func placement(for: UIViewController) -> UIArrangementViewController.ViewPlacement?](uiarrangementviewcontroller/placement(for:).md)
  Returns the placement for the provided view controller in the arrangement.
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
  Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
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