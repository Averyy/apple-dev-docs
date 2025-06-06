# UIPopoverPresentationController

**Framework**: UIKit  
**Kind**: class

An object that manages the display of content in a popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPopoverPresentationController
```

## Mentions

- [Displaying transient content in a popover](displaying-transient-content-in-a-popover.md)

#### Overview

From the time a popover is presented until the time it’s dismissed, UIKit uses an instance of this class to manage the presentation behavior. You use instances of this class as-is to configure aspects of the popover appearance and behavior for view controllers whose presentation style is set to [`UIModalPresentationStyle.popover`](uimodalpresentationstyle/popover.md).

In nearly all cases, you use this class as-is and don’t create instances of it directly. UIKit creates an instance of this class automatically when you present a view controller using the [`UIModalPresentationStyle.popover`](uimodalpresentationstyle/popover.md) style. You can retrieve that instance from the presented view controller’s [`popoverPresentationController`](uiviewcontroller/popoverpresentationcontroller.md) property and use it to configure the popover behavior.

If you don’t want to configure a popover immediately after presenting a view controller, you can use a delegate object to configure the popover instead. During the presentation process, the popover presentation controller calls various methods of its delegate—an object that conforms to the [`UIPopoverPresentationControllerDelegate`](uipopoverpresentationcontrollerdelegate.md) protocol—to ask for information and to inform it about the state of the presentation. Your delegate object can use those methods to configure the popover and adjust its behavior as needed. For information about how to implement a delegate for a popover presentation controller, see [`UIPopoverPresentationControllerDelegate`](uipopoverpresentationcontrollerdelegate.md).

For information about how to display a view controller using a popover presentation controller, see [`Displaying transient content in a popover`](displaying-transient-content-in-a-popover.md).

## Topics

### Customizing the popover behavior
- [var delegate: (any UIPopoverPresentationControllerDelegate)?](uipopoverpresentationcontroller/delegate.md)
  The delegate that handles popover-related messages.
- [protocol UIPopoverPresentationControllerDelegate](uipopoverpresentationcontrollerdelegate.md)
  The interface for a popover presentation delegate, which lets you customize the behavior of a popover-based presentation.
### Configuring the popover appearance
- [var popoverLayoutMargins: UIEdgeInsets](uipopoverpresentationcontroller/popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](uipopoverpresentationcontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var passthroughViews: [UIView]?](uipopoverpresentationcontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](uipopoverpresentationcontroller/popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.
- [var canOverlapSourceViewRect: Bool](uipopoverpresentationcontroller/canoverlapsourceviewrect.md)
  A Boolean value indicating whether the popover can overlap its view rectangle.
### Specifying the popover’s anchor point
- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](uipopoverpresentationcontroller/sourceitem.md)
  The item on which to anchor the popover.
- [protocol UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
  A type that can be an anchor for a popover presentation controller.
- [var sourceView: UIView?](uipopoverpresentationcontroller/sourceview.md)
  The view containing the anchor rectangle for the popover.
- [var sourceRect: CGRect](uipopoverpresentationcontroller/sourcerect.md)
  The area in the source view in which you anchor the popover.
- [var barButtonItem: UIBarButtonItem?](uipopoverpresentationcontroller/barbuttonitem.md)
  The bar button item on which to anchor the popover.
### Configuring the popover arrows
- [var permittedArrowDirections: UIPopoverArrowDirection](uipopoverpresentationcontroller/permittedarrowdirections.md)
  The arrow directions that you allow for the popover.
- [var arrowDirection: UIPopoverArrowDirection](uipopoverpresentationcontroller/arrowdirection.md)
  The arrow direction in use by the popover.
### Displaying the popover as a sheet
- [var adaptiveSheetPresentationController: UISheetPresentationController](uipopoverpresentationcontroller/adaptivesheetpresentationcontroller.md)
  The sheet presentation controller the popover adapts to in compact size classes.

## Relationships

### Inherits From
- [UIPresentationController](uipresentationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)

## See Also

- [Displaying transient content in a popover](displaying-transient-content-in-a-popover.md)
  Show a temporary interface on top of your app’s content on iPad.
- [class UIPopoverBackgroundView](uipopoverbackgroundview.md)
  The background appearance for a popover.
- [protocol UIPopoverBackgroundViewMethods](uipopoverbackgroundviewmethods.md)
  A set of methods that popover background view subclasses must implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller)*