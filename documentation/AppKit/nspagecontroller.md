# NSPageController

**Framework**: Appkit  
**Kind**: class

An object that controls swipe navigation and animations between views or view content.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
class NSPageController
```

#### Overview

[`NSPageController`](nspagecontroller.md) is useful for user interfaces which control navigating multiple pages as in a book or a web browser history. Page controller inherits from the [`NSViewController`](nsviewcontroller.md) class . You must assign the `view` property to a view in your view hierarchy. The [`NSPageController`](nspagecontroller.md) class does not vend a view and does insert itself into the responder chain.

Conceptually, the page controller manages swiping between an array of pages, the [`arrangedObjects`](nspagecontroller/arrangedobjects.md). Using the [`selectedIndex`](nspagecontroller/selectedindex.md) property, you can determine how many pages forward or backward the user may navigate.

> **Note**:  When using history mode, do not wire `pageController.view` to an [`NSSplitView`](nssplitview.md) subview. This will actually cause a 3rd split when the private transition view is put in the view hierarchy. You can work around this by using an empty [`NSView`](nsview.md) instance as the [`NSSplitView`](nssplitview.md) subview and placing the real contents in a subview of the empty view.

##### Page Controller Modes

There are two modes that an `NSPageController` instance may operate in, history mode and book mode. The main difference between the two modes is that  expects `pageController.view` to be the content and  expects `pageController.view` to be be a container for the content that you will supply by returning `viewControllers` in your delegate methods.

###### History Mode

History mode is designed to be the easiest way to create a history user interface. The page controller will manage the history (the `arrangedObjects` property), snapshots, and user navigation between pages in the history.

As the user navigates to new content, add to the history by calling [`navigateForward(to:)`](nspagecontroller/navigateforward(to:).md). The page controller will remove any `arrangedObjects` after the [`selectedIndex`](nspagecontroller/selectedindex.md) and then add the object to the end of the `arrangedObjects` array and update the `selectedIndex` property. Just like navigating in a new direction in a web browser, all forward history is lost once the user starts navigating a new path. After returning from `navigateForwardToObject:` you are free to update the contents of `pageController.view`.

###### Delegate Method Invocation During History Mode Swiping

During swiping, the following optional delegate methods are called in the specified order:

The [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) delegate method is invoked when the user starts a swipe action. This is the appropriate point at which to save information that you may need to restore, such as a page’s scrolled location.

Upon returning from the this delegate method, `pageController.view` is hidden. In it’s place the page controller shows a private view hierarchy to animate previously taken snapshots of the page history. This allows the page controller to remain responsive to the user without any required action by your application.Next, if implemented, the [`pageController(_:didTransitionTo:)`](nspagecontrollerdelegate/pagecontroller(_:didtransitionto:).md) delegate method is invoked. This delegate method is called after a physically successful swipe, but before the animation has completed. The supplied object is the page the user navigated to – the new `selectedIndex` object in `arrangedObjects`. If background loading tasks need to be initiated this is the appropriate time to do so. However, do not block the main thread or the animation will stutter or pause.

Finally, the pageControllerDidEndLiveTransition: delegate method is invoked after the swipe and swipe animations are complete. You should any position settings or other display specific state stored in the [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) implementation. The `pageController.view` is still hidden at this point and you must call [`completeTransition()`](nspagecontroller/completetransition().md) on the page controller instance to inform the instance to hide the private transition view and show `pageController.view`. Often you do this immediately, however, if your content is not ready you can call this at a later.

###### Book Mode View Controller Mode

Book mode is designed to give you more control over the swiping process and to facilitate more user interface designs than just history, although you can use book mode to create a history user interface.

In this mode, `pageController.view` is a container view and the content views are vended by view controller instances supplied by the delegate object.

To enable book mode, you must implement the following two methods in your delegate: [`pageController(_:identifierFor:)`](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md) and [`pageController(_:viewControllerForIdentifier:)`](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md).

The page controller instance caches the view controllers supplied for each identifier and only asks it’s delegate to create more if one does not already exists in its cache. If you have different type of views you want to swipe in, then supply a different identifier for each type.

When needed, you will be asked to prepare a view controller instance with a page via the optional delegate method [`pageController(_:prepare:with:)`](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md). If you do not implement this method, then the `representedObject` of the view controller that would have been passed to this delegate method is set as the object.

The delegate will be asked to prepare a view controller with a `nil` object for each unique identifier it encounters. The NSPageController instance will use this to generate a default snapshot for that identifier.

When using the book mode, if `pageController.view` is layer backed, live layers are used during transition instead of snapshots.

Generally, when using book mode, the set of pages are known and it is your responsibility to set the `arrangedObjects` array property and initially selected page using the `selectedIndex` property.

###### Delegate Method Invocation During Book Mode Swiping

During swiping, the following optional delegate methods are called in the specified order:

The delegate method [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) is invoked when the user starts a swipe action. As in history mode, this is the appropriate point at which to save information that you may need to restore, such as a page’s scrolled location.

After returning from the [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) delegate method, the page controller takes a snapshot of the `view` in the specified [`selectedViewController`](nspagecontroller/selectedviewcontroller.md) and then removes it from `pageController.view`. The page controller replaces it with a private view hierarchy to animate previously taken snapshots. Unlike when building up a history, snapshots may not yet exist for the page being navigated to. In this case, a previously gathered default snapshot is used for that page’s identifier. Regardless, if using a default snapshot or a previously gathered snapshot of actual contents, a view controller is prepared for the page being navigated to, and passed to the delegate. This `viewController.view` is then asked to draw on a background thread while swiping continues. Note that at this point the view does not reside within a window. Once the background threaded drawing completes, the initial snapshot is replaced with the newly generated snapshot.

Next the [`pageController(_:didTransitionTo:)`](nspagecontrollerdelegate/pagecontroller(_:didtransitionto:).md) delegate method is invoked after a physically successful swipe, but before the animation has completed. The supplied object is the page the user navigated to - the new object in the [`arrangedObjects`](nspagecontroller/arrangedobjects.md) array at the [`selectedIndex`](nspagecontroller/selectedindex.md). Note that the page controller’s [`selectedViewController`](nspagecontroller/selectedviewcontroller.md) has not been updated yet. If you need to start some background loading tasks, now is the time to do it. Do not block the main thread or the animation will stutter or pause.

Finally the [`pageControllerDidEndLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md) method is invoked after the swipe and swipe animations are complete. The `selectedViewController.view` is still detached at this point and you must call [`completeTransition()`](nspagecontroller/completetransition().md) on the page controller to hide the private transition view and update the [`selectedViewController`](nspagecontroller/selectedviewcontroller.md). Often you do this immediately, however, if your content is not ready you can call this at a later.

##### Completing the Page Controller Transition

An `NSPageController` instance uses a private view hierarchy during swiping. To create a seamless transition to the new content, it is your responsibility to inform the page controller when you are ready to draw the new content. Ideally, the new content should match the snapshot so the user is none the wiser. You inform the page controller to complete the transition by calling [`completeTransition()`](nspagecontroller/completetransition().md). If needed, a view controller is prepared and then the content view is shown (or added) to the view hierarchy and the private transition view is hidden.

During page controller initiated animations, [`pageControllerWillStartLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md) and [`pageControllerDidEndLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md) are invoked on the delegate. Generally during [`pageControllerDidEndLiveTransition(_:)`](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md) you will call [`completeTransition()`](nspagecontroller/completetransition().md). Programatic animations via the animator proxy do not call the delegate methods and you are responsible for calling [`completeTransition()`](nspagecontroller/completetransition().md) when the animation completes.This is easily done via a completion handler on an [`NSAnimationContext`](nsanimationcontext.md) grouping. For example:

```objc
 //To instantly change the selectedIndex:
  pageController.selectedIndex = newIndex;
 
  //To animate a selectedIndex change:
  [NSAnimationContext runAnimationGroup:^(NSAnimationContext *context) {
    [[pageController animator] setSelectedIndex:newIndex];
  } completionHandler:^{
    [pageController completeTransition];
  }];
```

## Topics

### Customizing the Paged Interface Behavior
- [var delegate: (any NSPageControllerDelegate)?](nspagecontroller/delegate.md)
  The page controller’s delegate object.
- [protocol NSPageControllerDelegate](nspagecontrollerdelegate.md)
  The `NSPageControllerDelegate` protocol allows you to customize the behavior of instances of the NSPageController class.
### Page Controller Items
- [var arrangedObjects: [Any]](nspagecontroller/arrangedobjects.md)
  An array containing the objects displayed in the page controller’s view.
- [func navigateForward(to: Any)](nspagecontroller/navigateforward(to:).md)
  Navigates to the specific object.
- [var selectedIndex: Int](nspagecontroller/selectedindex.md)
  The currently selected object in the arranged objects array.
### Page Controller Navigation
- [func navigateBack(Any?)](nspagecontroller/navigateback(_:).md)
  Navigates backwards in the page controller’s arranged objects array.
- [func navigateForward(Any?)](nspagecontroller/navigateforward(_:).md)
  Navigates to the next object in the page controller’s arranged objects array, if appropriate.
- [func takeSelectedIndexFrom(Any?)](nspagecontroller/takeselectedindexfrom(_:).md)
  Navigates to the selected index, which is taken from the sender.
### Transition Style
- [var transitionStyle: NSPageController.TransitionStyle](nspagecontroller/transitionstyle-swift.property.md)
  The transition style the page controller uses when changing pages.
### Completing Page Transition
- [func completeTransition()](nspagecontroller/completetransition.md)
  Invoked when the page transition is completed.
### Getting the View Controller
- [var selectedViewController: NSViewController?](nspagecontroller/selectedviewcontroller.md)
  The view controller associated with the selected object..
### Constants
- [NSPageController.TransitionStyle](nspagecontroller/transitionstyle-swift.enum.md)
  These constants control the transition style of the page controller.

## Relationships

### Inherits From
- [NSViewController](nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](nseditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](nssegueperforming.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nspagecontroller)*