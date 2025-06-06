# UIControl

**Framework**: UIKit  
**Kind**: class

The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIControl
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Overview

Controls implement elements such as buttons and sliders, which your app can use to facilitate navigation, gather user input, or manipulate content. Controls use the target-action mechanism to report user interactions to your app.

![Examples of UIKit controls.](https://docs-assets.developer.apple.com/published/6b1386718d569d3ca35a66e82a339ecc/media-1965830%402x.png)

You don’t create instances of this class directly. The [`UIControl`](uicontrol.md) class is a subclassing point that you extend to implement custom controls. You can also subclass existing control classes to extend or modify their behaviors. For example, you might override the methods of this class to track touch events yourself or to determine when the state of the control changes.

A control’s state determines its appearance and its ability to support user interactions. Controls can be in one of several states, which the [`UIControl.State`](uicontrol/state-swift.struct.md) type defines. You can change the state of a control programmatically according to your app’s needs. For example, you might disable a control to prevent the user from interacting with it. User interactions can also change the state of a control.

##### Respond to User Interaction

The target-action mechanism simplifies the code that you write to use controls in your app. Instead of writing code to track touch events, you write action methods to respond to control-specific events. For example, you might write an action method that responds to changes in the value of a slider. The control handles all the work of tracking incoming touch events and determining when to call your methods.

When adding an action method to a control, you specify both the action method and an object that defines that method to the [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md) method. (You can also configure the target and action of a control in Interface Builder.) The target object can be any object, but it’s typically the view controller’s root view that contains the control. If you specify `nil` for the target object, the control searches the responder chain for an object that defines the specified action method.

The signature of an action method takes one of three forms. The `sender` parameter corresponds to the control that calls the action method, and the `event` parameter corresponds to the [`UIEvent`](uievent.md) object that triggered the control-related event.

The system calls action methods when the user interacts with the control in specific ways. The [`UIControl.Event`](uicontrol/event.md) type defines the types of user interactions that a control can report and those interactions mostly correlate to specific touch events within the control. When configuring a control, you must specify which events trigger the calling of your method. For a button control, you might use the [`touchDown`](uicontrol/event/touchdown.md) or [`touchUpInside`](uicontrol/event/touchupinside.md) event to trigger calls to your action method. For a slider, you might care only about changes to the slider’s value, so you might choose to attach your action method to [`valueChanged`](uicontrol/event/valuechanged.md) events.

When a control-specific event occurs, the control calls any associated action methods immediately. The current [`UIApplication`](uiapplication.md) object dispatches action methods and finds an appropriate object to handle the message, following the responder chain, if necessary. For more information about responders and the responder chain, see [`Event Handling Guide for UIKit Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html#//apple_ref/doc/uid/TP40009541).

##### Configure Control Attributes in Interface Builder

The following table lists the attributes for instances of the [`UIControl`](uicontrol.md) class.

| Attribute | Description |
| --- | --- |
| Alignment | The horizontal and vertical alignment of a control’s content. For controls that contain text or images, such as buttons and text fields, use these attributes to configure the position of that content within the control’s bounds. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) These alignment options apply to the content of a control and not to the control itself. For information about how to align controls with respect to other controls and views, see [`Auto Layout Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html#//apple_ref/doc/uid/TP40010853). |
| Content | The initial state of the control. Use the checkboxes to configure whether the control is in an enabled, selected, or highlighted state initially. |

##### Support Localization

Because [`UIControl`](uicontrol.md) is an abstract class, you don’t internationalize it specifically. However, you do internationalize the content of subclasses like [`UIButton`](uibutton.md). For information about internationalizing a specific control, see the reference for that control.

##### Make Controls Accessible

Controls are accessible by default. To be useful, an accessible user interface element must provide accurate and helpful information about its screen position, name, behavior, value, and type. This is the information VoiceOver speaks to users. Users who are blind or have low vision can rely on VoiceOver to help them use their devices.

Controls support the following accessibility attributes:

-  A short, localized word or phrase that succinctly describes the control or view, but doesn’t identify the element’s type. Examples are  and .
-  A combination of one or more individual traits, each of which describes a single aspect of an element’s state, behavior, or usage. For example, you might use a combination of the Keyboard Key and the Selected traits to describe an element that behaves like a keyboard key and that’s in a selected state.
-  A brief, localized phrase that describes the results of an action on an element. Examples are  and .
-  The frame of the element in screen coordinates, which the `CGRect` structure specifies for an element’s screen location and size.
-  The current value of an element when the label doesn’t represent the value. For example, the label for a slider might be , but its current value might be .

The `UIControl` class provides default content for the value and frame attributes. Many controls automatically enable additional specific traits as well. You can configure other accessibility attributes programmatically or with the Identity inspector in Interface Builder.

For more information about accessibility attributes, see [`Accessibility Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/iPhoneAccessibility/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008785).

##### Subclassing Notes

Subclassing [`UIControl`](uicontrol.md) gives you access to the built-in target-action mechanism and simplified event-handling support. You can subclass existing controls and modify their behavior in one of two ways:

- Override the [`sendAction(_:to:for:)`](uicontrol/sendaction(_:to:for:).md) method of an existing subclass to observe or modify the dispatching of action methods to the control’s associated targets. You might use this method to modify the dispatch behavior for the specified object, selector, or event.
- Override the [`beginTracking(_:with:)`](uicontrol/begintracking(_:with:).md), [`continueTracking(_:with:)`](uicontrol/continuetracking(_:with:).md), [`endTracking(_:with:)`](uicontrol/endtracking(_:with:).md), and [`cancelTracking(with:)`](uicontrol/canceltracking(with:).md) methods to track touch events occurring in the control. You can use the tracking information to perform additional actions. Always use these methods to track touch events instead of the methods that the [`UIResponder`](uiresponder.md) class defines.

If you subclass [`UIControl`](uicontrol.md) directly, your subclass is responsible for setting up and managing your control’s visual appearance. Use the methods for tracking events to update your control’s state and to send an action when the control’s value changes.

## Topics

### Creating a control
- [convenience init(frame: CGRect, primaryAction: UIAction?)](uicontrol/init(frame:primaryaction:).md)
  Creates a control with the specified frame and primary action.
- [init(frame: CGRect)](uicontrol/init(frame:).md)
  Creates a control with the specified frame.
- [init?(coder: NSCoder)](uicontrol/init(coder:).md)
  Creates a control from data in an unarchiver.
### Managing state
- [var state: UIControl.State](uicontrol/state-swift.property.md)
  The state of the control, specified as a bit mask value.
- [UIControl.State](uicontrol/state-swift.struct.md)
  Constants describing the state of a control.
- [var isEnabled: Bool](uicontrol/isenabled.md)
  A Boolean value indicating whether the control is in the enabled state.
- [var isSelected: Bool](uicontrol/isselected.md)
  A Boolean value indicating whether the control is in the selected state.
- [var isHighlighted: Bool](uicontrol/ishighlighted.md)
  A Boolean value indicating whether the control draws a highlight.
### Specifying content alignment
- [var contentVerticalAlignment: UIControl.ContentVerticalAlignment](uicontrol/contentverticalalignment-swift.property.md)
  The vertical alignment of content within the control’s bounds.
- [UIControl.ContentVerticalAlignment](uicontrol/contentverticalalignment-swift.enum.md)
  Constants for specifying the vertical alignment of content (text and images) in a control.
- [var contentHorizontalAlignment: UIControl.ContentHorizontalAlignment](uicontrol/contenthorizontalalignment-swift.property.md)
  The horizontal alignment of content within the control’s bounds.
- [var effectiveContentHorizontalAlignment: UIControl.ContentHorizontalAlignment](uicontrol/effectivecontenthorizontalalignment.md)
  The horizontal alignment currently in effect for the control.
- [UIControl.ContentHorizontalAlignment](uicontrol/contenthorizontalalignment-swift.enum.md)
  The horizontal alignment of content (text and images) within a control.
### Managing the control’s targets and actions
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](uicontrol/addtarget(_:action:for:).md)
  Associates a target object and action method with the control.
- [func removeTarget(Any?, action: Selector?, for: UIControl.Event)](uicontrol/removetarget(_:action:for:).md)
  Stops the delivery of events to the specified target object.
- [var allTargets: Set<AnyHashable>](uicontrol/alltargets.md)
  Returns all target objects associated with the control.
- [func addAction(UIAction, for: UIControl.Event)](uicontrol/addaction(_:for:).md)
- [func removeAction(UIAction, for: UIControl.Event)](uicontrol/removeaction(_:for:).md)
- [func removeAction(identifiedBy: UIAction.Identifier, for: UIControl.Event)](uicontrol/removeaction(identifiedby:for:).md)
- [func actions(forTarget: Any?, forControlEvent: UIControl.Event) -> [String]?](uicontrol/actions(fortarget:forcontrolevent:).md)
  Returns the actions performed on a target object when the specified event occurs.
- [var allControlEvents: UIControl.Event](uicontrol/allcontrolevents.md)
  Returns the events for which the control has associated actions.
- [func enumerateEventHandlers((UIAction?, (Any?, Selector)?, UIControl.Event, inout Bool) -> Void)](uicontrol/enumerateeventhandlers(_:).md)
### Triggering actions
- [func performPrimaryAction()](uicontrol/performprimaryaction.md)
  Calls the method associated with the control’s primary action.
- [func sendAction(UIAction)](uicontrol/sendaction(_:).md)
- [func sendAction(Selector, to: Any?, for: UIEvent?)](uicontrol/sendaction(_:to:for:).md)
  Calls the specified action method.
- [func sendActions(for: UIControl.Event)](uicontrol/sendactions(for:).md)
  Calls the action methods associated with the specified events.
### Tracking touches and redrawing controls
- [func beginTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/begintracking(_:with:).md)
  Notifies the control when a touch event enters the control’s bounds.
- [func continueTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/continuetracking(_:with:).md)
  Notifies the control when a touch event for the control updates.
- [func endTracking(UITouch?, with: UIEvent?)](uicontrol/endtracking(_:with:).md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](uicontrol/canceltracking(with:).md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTracking: Bool](uicontrol/istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.
- [var isTouchInside: Bool](uicontrol/istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.
### Managing context menus
- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [var contextMenuInteraction: UIContextMenuInteraction?](uicontrol/contextmenuinteraction.md)
  A context menu interaction for the control.
- [var isContextMenuInteractionEnabled: Bool](uicontrol/iscontextmenuinteractionenabled.md)
  A Boolean value that determines whether the control enables its context menu interaction.
- [var showsMenuAsPrimaryAction: Bool](uicontrol/showsmenuasprimaryaction.md)
  A Boolean value that determines whether the context menu interaction is the control’s primary action.
- [func contextMenuInteraction(UIContextMenuInteraction, configurationForMenuAtLocation: CGPoint) -> UIContextMenuConfiguration?](uicontrol/contextmenuinteraction(_:configurationformenuatlocation:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForDismissingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontrol/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uicontrol/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, willDisplayMenuFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontrol/contextmenuinteraction(_:willdisplaymenufor:animator:).md)
- [func contextMenuInteraction(UIContextMenuInteraction, willEndFor: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uicontrol/contextmenuinteraction(_:willendfor:animator:).md)
- [func menuAttachmentPoint(for: UIContextMenuConfiguration) -> CGPoint](uicontrol/menuattachmentpoint(for:).md)
### Showing tooltips
- [var toolTip: String?](uicontrol/tooltip.md)
  The default text to display in the control’s tooltip.
- [var toolTipInteraction: UIToolTipInteraction?](uicontrol/tooltipinteraction.md)
  The tooltip interaction associated with the control.
### Constants
- [UIControl.Event](uicontrol/event.md)
  Constants describing the types of events possible for controls.
### Instance Properties
- [var isSymbolAnimationEnabled: Bool](uicontrol/issymbolanimationenabled.md)
  A Boolean value that indicates whether symbol effects animate.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Inherited By
- [UIButton](uibutton.md)
- [UIColorWell](uicolorwell.md)
- [UIDatePicker](uidatepicker.md)
- [UIPageControl](uipagecontrol.md)
- [UIPasteControl](uipastecontrol.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISlider](uislider.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITextField](uitextfield.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
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

- [Responding to control-based events using target-action](responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class UIButton](uibutton.md)
  A control that executes your custom code in response to user interactions.
- [class UIColorWell](uicolorwell.md)
  A control that displays a color picker.
- [class UIDatePicker](uidatepicker.md)
  A control for inputting date and time values.
- [class UIPageControl](uipagecontrol.md)
  A control that displays a horizontal series of dots, each of which corresponds to a page in the app’s document or other data-model entity.
- [class UISegmentedControl](uisegmentedcontrol.md)
  A horizontal control that consists of multiple segments, each segment functioning as a discrete button.
- [class UISlider](uislider.md)
  A control for selecting a single value from a continuous range of values.
- [class UIStepper](uistepper.md)
  A control for incrementing or decrementing a value.
- [class UISwitch](uiswitch.md)
  A control that offers a binary choice, such as on/off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol)*