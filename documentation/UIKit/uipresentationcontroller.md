# UIPresentationController

**Framework**: UIKit  
**Kind**: class

An object that manages the transition animations and the presentation of view controllers onscreen.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPresentationController
```

## Mentions

- [Choosing a specific interface style for your iOS app](choosing-a-specific-interface-style-for-your-ios-app.md)

#### Overview

From the time a view controller is presented until the time it’s dismissed, UIKit uses a presentation controller to manage various aspects of the presentation process for that view controller. The presentation controller can add its own animations on top of those provided by animator objects, it can respond to size changes, and it can manage other aspects of how the view controller is presented onscreen.

When you present a view controller using the [`present(_:animated:completion:)`](uiviewcontroller/present(_:animated:completion:).md) method, UIKit always manages the presentation process. Part of that process involves creating the presentation controller that’s appropriate for the given presentation style. For the built-in styles (such as the [`UIModalPresentationStyle.pageSheet`](uimodalpresentationstyle/pagesheet.md) style), UIKit defines and creates the needed presentation controller object. The only time your app can provide a custom presentation controller is when you set the [`modalPresentationStyle`](uiviewcontroller/modalpresentationstyle.md) property of your view controller [`UIModalPresentationStyle.custom`](uimodalpresentationstyle/custom.md). You might provide a custom presentation controller when you want to add a shadow view or decoration views underneath the view controller being presented or when you want to modify the presentation behavior in other ways.

You vend your custom presentation controller object through your view controller’s transitioning delegate. UIKit maintains a reference to your presentation controller object while the presented view controller is onscreen. For information about the transitioning delegate and the objects it provides, see [`UIViewControllerTransitioningDelegate`](uiviewcontrollertransitioningdelegate.md).

##### Understand the Presentation Process

The presentation process managed by a presentation controller is divided into three phases:

- The  involves moving the new view controller onscreen through a series of transition animations.
- The  involves responding to environment changes (such as device rotations) while the new view controller is onscreen.
- The  involves moving the new view controller off screen through a series of transition animations

The presentation controller’s role during all of these phases is to manage its own custom views and state information. During the presentation and dismissal phases, the presentation controller adds its custom views (if any) to the view hierarchy and creates any appropriate transition animations for those views. The animation of the view controller’s view onto the screen is still managed by an animator object — that is, an object that adopts the [`UIViewControllerAnimatedTransitioning`](uiviewcontrolleranimatedtransitioning.md) protocol. UIKit calls separate presentation controller methods at the beginning and end of the presentation and dismissal phases so that the presentation controller can perform any needed cleanup.

##### Add Custom Views to a Presentation

The [`UIPresentationController`](uipresentationcontroller.md) class defines specific entry points for manipulating the view hierarchy when presenting a view controller. When a view controller is about to be presented, UIKit calls the presentation controller’s [`presentationTransitionWillBegin()`](uipresentationcontroller/presentationtransitionwillbegin().md) method. You can use that method to add views to the view hierarchy and set up any animations related to those views. At the end of the presentation phase, UIKit calls the [`presentationTransitionDidEnd(_:)`](uipresentationcontroller/presentationtransitiondidend(_:).md) method to let you know that the transition finished.

The following code shows a sample implementation of the [`presentationTransitionWillBegin()`](uipresentationcontroller/presentationtransitionwillbegin().md) and [`presentationTransitionDidEnd(_:)`](uipresentationcontroller/presentationtransitiondidend(_:).md) methods for a custom presentation controller. In this example, the view controller adds a dimming view as a backdrop to the presented view controller. (The `_dimmingView` variable refers to a custom [`UIView`](uiview.md) object that you would provide.) When presenting the view controller, the [`presentationTransitionWillBegin()`](uipresentationcontroller/presentationtransitionwillbegin().md) method adds the dimming view first and embeds the view controller content inside that dimming view. It then configures a fade-in animation to run alongside the other transition animations. If the user aborts the presentation process, perhaps through an interactive gesture, the [`presentationTransitionDidEnd(_:)`](uipresentationcontroller/presentationtransitiondidend(_:).md) removes the dimming view. If the presentation succeeds, both the dimming view and the presented view controller remain onscreen until they’re dismissed.

```objc
- (void)presentationTransitionWillBegin {
   // Add a custom dimming view behind the presented view controller's view.
   [[self containerView] addSubview:_dimmingView];
   [_dimmingView addSubview:[[self presentedViewController] view]];
 
   // Use the transition coordinator to set up the animations.
    id <UIViewControllerTransitionCoordinator> transitionCoordinator =
          [[self presentingViewController] transitionCoordinator];
 
   // Fade in the dimming view during the transition.
    [_dimmingView setAlpha:0.0];
    [transitionCoordinator animateAlongsideTransition:
       ^(id<UIViewControllerTransitionCoordinatorContext> context) {
          [_dimmingView setAlpha:1.0];
       } completion:nil];
}
 
- (void)presentationTransitionDidEnd:(BOOL)completed {
   // Remove the dimming view if the presentation is terminated.
   if (!completed) {
      [_dimmingView removeFromSuperview];
   }
}
```

When dismissing the view controller, use the [`dismissalTransitionWillBegin()`](uipresentationcontroller/dismissaltransitionwillbegin().md) method to configure any animations and use the [`dismissalTransitionDidEnd(_:)`](uipresentationcontroller/dismissaltransitiondidend(_:).md) method to remove any custom views from the view hierarchy.

##### Adapt to Size Class Changes

Size class changes signal large-scale changes to how your app should present its content. Presentation controllers manage size class changes by adjusting the presentation style (as needed) for their presented view controller. Adjustments are made only when the current presentation style doesn’t make sense in the new environment. For example, a popover becomes a full-screen presentation when the size class changes from horizontally regular to horizontally compact. For presentation styles that already make sense in the new environment, such as a full-screen presentation style, no adaptive change is made.

When the size class of the presented view controller changes from horizontally regular to horizontally compact, the presentation controller calls its [`adaptivePresentationStyle`](uipresentationcontroller/adaptivepresentationstyle.md) method to determine which new style (if any) to apply. When a new style is needed, the presentation controller initiates a transition to the new style, which may also involve replacing the current presentation controller object with a new object. Because the presentation controller object may change, always retrieve the presentation controller from [`presentationController`](uiviewcontroller/presentationcontroller.md) property of the presented view controller.

When the presentation style changes, the presentation controller also gives you the opportunity to specify a new presented view controller. Before initiating the transition, the presentation controller calls the [`presentationController(_:viewControllerForAdaptivePresentationStyle:)`](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:viewcontrollerforadaptivepresentationstyle:).md) method of its delegate object. If you implement that method, you can use it to make major or minor adjustments to the presented content. A major adjustment would be to replace the current view controller with an entirely new view controller that was designed specifically for the given size class. A minor adjustment would be to install the current view controller inside a navigation controller to facilitate navigation in the new size class.

##### Respond to Size Changes

Size changes represent small changes to the width or height of a view controller’s view. Typically, these changes happen when the device rotates between portrait and landscape orientations. When a size change occurs, UIKit calls the presentation controller’s [`viewWillTransition(to:with:)`](uicontentcontainer/viewwilltransition(to:with:).md) method. In a custom presentation, use that method to modify your presentation controller’s custom views or make changes to the view hierarchy. For example, you might swap out custom decoration views with ones that fit the new size better.

After notifying your presentation controller of an impending size change, UIKit begins the normal view layout process. Apps that use auto layout shouldn’t need to do anything because the auto layout mechanism resizes views as needed. But if a custom presentation controller needs to make layout-specific changes, it can do so in its [`containerViewWillLayoutSubviews()`](uipresentationcontroller/containerviewwilllayoutsubviews().md) and [`containerViewDidLayoutSubviews()`](uipresentationcontroller/containerviewdidlayoutsubviews().md) methods. These methods are equivalent to the [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) and [`viewDidLayoutSubviews()`](uiviewcontroller/viewdidlayoutsubviews().md) methods of the [`UIViewController`](uiviewcontroller.md) class and used in the same way. UIKit calls them before and after it calls the [`layoutSubviews()`](uiview/layoutsubviews().md) methods of the views in the view hierarchy.

##### Subclassing Notes

For custom presentation styles, you should subclass [`UIPresentationController`](uipresentationcontroller.md) and override at least some of its methods to implement your custom presentation behaviors. Use your custom presentation controller to customize the presentation process.

For custom presentation controllers, you must call the [`init(presentedViewController:presenting:)`](uipresentationcontroller/init(presentedviewcontroller:presenting:).md) method during initialization. That method is the designated initializer of the class. UIKit uses it to perform required initialization for all presentation controller objects.

###### Methods to Override

If your [`UIPresentationController`](uipresentationcontroller.md) subclasses manages one or more custom views, you should consider overriding the following methods:

- Use the [`presentationTransitionWillBegin()`](uipresentationcontroller/presentationtransitionwillbegin().md) method to add your custom views to the view hierarchy and to animate the appearance of those views. If the view controller can’t be presented, you can remove those views in the [`presentationTransitionDidEnd(_:)`](uipresentationcontroller/presentationtransitiondidend(_:).md) method as needed.
- Use the [`dismissalTransitionWillBegin()`](uipresentationcontroller/dismissaltransitionwillbegin().md) method to perform animations related to the dismissal of the presented view controller. Don’t remove your custom views from the view hierarchy until the [`dismissalTransitionDidEnd(_:)`](uipresentationcontroller/dismissaltransitiondidend(_:).md) method is called.
- Use the [`viewWillTransition(to:with:)`](uicontentcontainer/viewwilltransition(to:with:).md) method to make any size-related changes to your custom views.

Subclasses may override other methods of this class as needed to provide custom behavior. For example, you might override the [`shouldPresentInFullscreen`](uipresentationcontroller/shouldpresentinfullscreen.md) or [`frameOfPresentedViewInContainerView`](uipresentationcontroller/frameofpresentedviewincontainerview.md) methods and return different values than those provided by the default implementations.

## Topics

### Creating a presentation controller
- [init(presentedViewController: UIViewController, presenting: UIViewController?)](uipresentationcontroller/init(presentedviewcontroller:presenting:).md)
  Initializes and returns a presentation controller for transitioning between the specified view controllers.
### Adapting your presentations dynamically
- [var delegate: (any UIAdaptivePresentationControllerDelegate)?](uipresentationcontroller/delegate.md)
  The delegate object for managing adaptive presentations.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
### Getting the presentation objects
- [var presentingViewController: UIViewController](uipresentationcontroller/presentingviewcontroller.md)
  The view controller that is the starting point for the presentation.
- [var presentedViewController: UIViewController](uipresentationcontroller/presentedviewcontroller.md)
  The view controller being presented.
- [var containerView: UIView?](uipresentationcontroller/containerview.md)
  The view in which the presentation occurs.
- [var presentedView: UIView?](uipresentationcontroller/presentedview.md)
  The view to be animated by the animator objects during a transition.
### Adjusting the size and layout of the presentation
- [var frameOfPresentedViewInContainerView: CGRect](uipresentationcontroller/frameofpresentedviewincontainerview.md)
  The frame rectangle to assign to the presented view at the end of the animations.
- [func containerViewWillLayoutSubviews()](uipresentationcontroller/containerviewwilllayoutsubviews.md)
  Notifies the presentation controller that layout is about to begin on the views of the container view.
- [func containerViewDidLayoutSubviews()](uipresentationcontroller/containerviewdidlayoutsubviews.md)
  Notifies the presentation controller when layout ends on the views of the container view.
### Tracking the transition’s start and end
- [func presentationTransitionWillBegin()](uipresentationcontroller/presentationtransitionwillbegin.md)
  Notifies the presentation controller that the presentation animations are about to start.
- [func presentationTransitionDidEnd(Bool)](uipresentationcontroller/presentationtransitiondidend(_:).md)
  Notifies the presentation controller that the presentation animations finished.
- [func dismissalTransitionWillBegin()](uipresentationcontroller/dismissaltransitionwillbegin.md)
  Notifies the presentation controller that the dismissal animations are about to start.
- [func dismissalTransitionDidEnd(Bool)](uipresentationcontroller/dismissaltransitiondidend(_:).md)
  Notifies the presentation controller that the dismissal animations finished.
### Getting the presentation attributes
- [var presentationStyle: UIModalPresentationStyle](uipresentationcontroller/presentationstyle.md)
  The presentation style of the presented view controller.
- [func adaptivePresentationStyle(for: UITraitCollection) -> UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle(for:).md)
  Returns the presentation style to use for the specified set of traits.
- [var adaptivePresentationStyle: UIModalPresentationStyle](uipresentationcontroller/adaptivepresentationstyle.md)
  Returns the presentation style to use when the presented view controller becomes horizontally compact.
- [var shouldPresentInFullscreen: Bool](uipresentationcontroller/shouldpresentinfullscreen.md)
  A Boolean value indicating whether the presentation covers the entire screen.
- [var shouldRemovePresentersView: Bool](uipresentationcontroller/shouldremovepresentersview.md)
  A Boolean value indicating whether the presenting view controller’s view should be removed when the presentation animations finish.
### Observing trait changes
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
### Overriding trait values
- [var traitOverrides: UITraitOverrides](uipresentationcontroller/traitoverrides-629ka.md)
- [struct UITraitOverrides](uitraitoverrides-swift.struct.md)
  A mutable container of traits you use to set trait changes for an object and its descendants.
### Deprecated
- [var overrideTraitCollection: UITraitCollection?](uipresentationcontroller/overridetraitcollection.md)
  Interface traits for the presented view controller, to use in place of traits from the iOS environment.
### Instance Properties
- [var backgroundEffect: UIVisualEffect?](uipresentationcontroller/backgroundeffect.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIPopoverPresentationController](uipopoverpresentationcontroller.md)
- [UISheetPresentationController](uisheetpresentationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)

## See Also

- [Disabling the pull-down gesture for a sheet](disabling-the-pull-down-gesture-for-a-sheet.md)
  Ensure a positive user experience when presenting a view controller as a sheet.
- [class UISheetPresentationController](uisheetpresentationcontroller.md)
  A presentation controller that manages the appearance and behavior of a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipresentationcontroller)*