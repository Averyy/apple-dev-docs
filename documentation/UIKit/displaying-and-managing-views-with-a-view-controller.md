# Displaying and managing views with a view controller

**Framework**: UIKit

Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.

#### Overview

In the model-view-controller design paradigm, a view controller fits between the view objects that present information onscreen and the data objects that store your app’s content. Specifically, a view controller manages a view hierarchy and the state information needed to keep those views up-to-date. Every UIKit app relies heavily on view controllers to present content, and you frequently define custom view controllers to manage your views and UI-related logic.

Most custom view controllers you create are  — that is, the view controller owns all of its views and manages interactions with those views. Use content view controllers to present your app’s custom content onscreen, and use your view controller object to manage the transfer of data to and from your custom views.

![An illustration of the relationship between a view controller, its views, and the data objects from your app.](https://docs-assets.developer.apple.com/published/734a881eaebde585c9cbad47bd162a53/media-3375402%402x.png)

> **Note**:  As opposed to a content view controller, a container view controller incorporates content from other view controllers into its view hierarchy. [`UINavigationController`](uinavigationcontroller.md) is an example of a container view controller. For information about how to implement a container view controller, see [`Creating a custom container view controller`](creating-a-custom-container-view-controller.md).

To define a content view controller, start by subclassing [`UIViewController`](uiviewcontroller.md). If your interface includes a table view or collection view, subclass [`UITableViewController`](uitableviewcontroller.md) or [`UICollectionViewController`](uicollectionviewcontroller.md) instead. New Xcode projects include one or more content view controller classes for you to modify, and you can add more.

##### Add Views to Your View Controller

[`UIViewController`](uiviewcontroller.md) contains a content view, accessible from the [`view`](uiviewcontroller/view.md) property, which serves as the root view of its view hierarchy. To that root view, you add the custom views you need to present your interface. In storyboards, you add views by dragging them onto the view controller scene. For example, the following figure shows a view controller with an image view and button on an iPhone.

![An image of a view controller interface that contains an image view and button.](https://docs-assets.developer.apple.com/published/05d0eff64845eb8e193d6f58f8c411c8/media-3375403%402x.png)

After adding views to a view controller, always add Auto Layout constraints to set the size and position of those views. Constraints are rules that specify how to size and position each view relative to its parent or sibling view, and they ensure that your views automatically adapt to different environments and devices. For more information, see [`View layout`](view-layout.md).

##### Store References to Important Views

At runtime, you may need to access views from your view controller’s code. For example, you might want to fetch the text in a text view or change the image in an image view. For that, you need a reference to the view in your view hierarchy. You create those references using outlets.

An outlet is a property in your view controller that includes the `IBOutlet` keyword. The presence of that keyword tells Xcode to expose that property in your storyboard. The following example code shows the definitions for two outlets. In Swift, include the `weak` keyword to prevent your view controller from holding a second strong reference to the view—the first originates from the view hierarchy itself.

In your storyboard, connect each outlet to the corresponding view, as described in [`Add an outlet connection to send a message to a UI object`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/devc06f7ee11). You don’t need to store references to all views in your view hierarchy; store references only to the views you modify later.

When you instantiate a view controller, UIKit reconnects any outlets that you configured in your storyboard. UIKit reestablishes these connections before calling your view controller’s [`viewDidLoad()`](uiviewcontroller/viewdidload().md) method, so you can access the objects in those properties from that method. If you create any views programmatically, you must explicitly assign those views to the appropriate properties of your view controller.

##### Handle Events Occurring in Views and Controls

Controls use the target-action design pattern to report user interactions, and some views post notifications or call delegate methods in response to changes. A view controller needs to know about many of these interactions so it can update its views, and you have several ways to make that happen:

- Implement delegate and action methods in your view controller. This option is simple and easy to implement, but it offers less flexibility and makes it harder to test and validate your code.
- Implement delegate and action methods in a class extension on your view controller. This option separates your event-handling code from the rest of your view controller, making it easier to test and validate that code.
- Implement delegate and action methods in dedicated objects that then forward relevant information to your view controller. This option offers the most flexibility and reusability. The separation of responsibilities also makes it easier to write unit tests.

To respond to user interactions with controls, define an action method with one of the signatures shown in the following code listing. In your method definition, you may replace the generic reference to [`UIControl`](uicontrol.md) with a more specific control class.

For information about the target-action design pattern and how to handle control-related events, see [`UIControl`](uicontrol.md).

##### Prepare Your Views to Appear Onscreen

UIKit gives you several opportunities to configure your view controller and views before displaying them onscreen. When you instantiate your view controller from a storyboard, UIKit creates that object using its [`init(coder:)`](uiviewcontroller/init(coder:).md) method.

> **Note**:  If your view controller requires custom initialization beyond what a coder object can provide, you can instantiate it programmatically using the [`instantiateInitialViewController(creator:)`](uistoryboard/instantiateinitialviewcontroller(creator:).md) method of [`UIStoryboard`](uistoryboard.md). That method lets you create the view controller yourself using a block and a UIKit-provided coder object. This option lets you initialize the view controller with any custom data your view controller requires, and still restore the configuration of views and other objects in the storyboard.

When you present a view controller onscreen, UIKit needs to first load and configure the corresponding views, which it does using the following sequence of steps:

1. Creates each view using the view’s [`init(coder:)`](uiview/init(coder:).md) method
2. Connects views to the corresponding actions and outlets in the view controller
3. Calls the [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) method of each view and the view controller
4. Assigns the view hierarchy to the view controller’s [`view`](uiviewcontroller/view.md) property
5. Calls the view controller’s [`viewDidLoad()`](uiviewcontroller/viewdidload().md) method

At load time, perform only the one-time configuration steps you need to prepare the view controller for use. Use load time to create and configure any additional views that aren’t part of your storyboard. Don’t perform tasks that need to happen each time your view controller appears onscreen. For example, don’t start animations or update the values of views.

Perform any final view-related tasks as your views first appear onscreen. UIKit notifies the owning view controller when its views are appearing onscreen, and updates the layout of those views to fit the current environment in the following manner:

1. Calls [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) at the start of the transition
2. Adds the view to the hierarchy
3. Updates the trait collections of the view controller and its view
4. Updates the geometry of the view, including its size and position in its superview. Updates layout margins and the safe area, and calls [`viewLayoutMarginsDidChange()`](uiviewcontroller/viewlayoutmarginsdidchange().md) and [`viewSafeAreaInsetsDidChange()`](uiviewcontroller/viewsafeareainsetsdidchange().md), if needed
5. Calls the [`viewIsAppearing(_:)`](uiviewcontroller/viewisappearing(_:).md) method to let you know the view controller’s view is appearing onscreen
6. Calls the [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) method
7. Updates the layout of the view hierarchy
8. Calls the [`viewDidLayoutSubviews()`](uiviewcontroller/viewdidlayoutsubviews().md) method
9. Displays the views onscreen
10. Calls the view controller’s [`viewDidAppear(_:)`](uiviewcontroller/viewdidappear(_:).md) method after any animations complete

Update the content of your views in the [`viewIsAppearing(_:)`](uiviewcontroller/viewisappearing(_:).md) method of your view controller. When the system calls this method, it has already added the view to the view hierarchy and defined the frame, bounds, margins, and insets. Content that the system adds in `viewIsAppearing(_:)` displays when the view is first visible on the screen.

The system calls the [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) and [`viewDidLayoutSubviews()`](uiviewcontroller/viewdidlayoutsubviews().md) methods, whenever the view performs layout, which can happen at any time while the view is visible. Because the system calls `viewIsAppearing(_:)` only once as part of each appearance transition, changes you make in this method don’t repeat each time the view performs layout.

When the system calls `viewIsAppearing(_:),` the trait collections of the view controller and its view are up to date. You may use the view controller’s [`traitCollection`](uitraitenvironment/traitcollection.md) property to access information about the current environment, such as the display scale or the vertical and horizontal size classes. For more information about the available traits, see [`UITraitCollection`](uitraitcollection.md).

## See Also

- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md)
  Display view controllers using different techniques, and pass data between them during transitions.
- [class UIViewController](uiviewcontroller.md)
  An object that manages a view hierarchy for your UIKit app.
- [class UITableViewController](uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [class UICollectionViewController](uicollectionviewcontroller.md)
  A view controller that specializes in managing a collection view.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/displaying-and-managing-views-with-a-view-controller)*