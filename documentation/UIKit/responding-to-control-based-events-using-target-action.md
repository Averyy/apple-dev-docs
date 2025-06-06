# Responding to control-based events using target-action

**Framework**: UIKit

Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.

#### Overview

User interactions generate thousands of events for your app. Every swipe of the finger or button click, for instance, results in numerous events your app has to process.

`Target-action` is a design pattern to help you handle these user interactions efficiently. By only registering actions against specific events on your controls, you simplify your event processing, while making your code more maintainable and easier to read.

Use `target-action` to connect events directly from controls in your UI to methods in your code.

##### Designate an Object to Handle Control Related Events

When a person interacts with your control, the control needs to know where to send the event. The destination for the event is the . View controllers make good targets because they’re adept at handling user interactions, as well as hosting UI controls.

![A diagram that depicts the relationship between a control and its corresponding target and action. The control on the left has one arrow pointing to its target on the right, which is a view controller. Underneath this is a parallel arrow pointing from the control on the left to its action method on the right, which is a function with the name buttonTapped.](https://docs-assets.developer.apple.com/published/e4d1af298b6b4942ba4ae92e7b9142e1/media-4142878%402x.png)

##### Define the Action Methods You Use to Respond to Events

With a control assigned to the target, provide a function to call on that target when the event occurs. This is the  method.

Action methods have a distinct signature:

Xcode uses the `@IBAction` keyword to connect controls in Interface Builder to functions in your code. The keyword also bridges the Swift and Objective-C runtimes, enabling Swift code to call into Objective-C, which is where the target-action functionality lives.

The `sender` parameter defines where the event comes from; for example, a button. Use the generic type `Any` to allow any control to call the action method, or specify the `sender` type when you need more information about the control for event processing. For example, set the `sender` type to [`UISlider`](uislider.md) to read the slider thumb value when someone moves the slider left or right.

UIKit also supports coupling action methods to specific event types (see [`UIControl.Event`](uicontrol/event.md)). For example, to set up target-action for a user dragging their finger inside the bounds of a control, register for the event type [`touchDragInside`](uicontrol/event/touchdraginside.md).

##### Connect Controls to the Action Methods in Interface Builder

With the `target` and `action` methods defined, you’re ready to connect them visually to the controls in Interface Builder.

1. Select the control (the `target`) you want to connect to the code (the `action`).
2. Control-drag the control to the view controller in the document outline.
3. Select the action method that the control connects to.

![A screenshot showing how to connect a control to an action in Xcode using Interface Builder.  The screenshot consists of Xcode’s document outline view on the left displaying a connection to the view controller, with the Interface Builder canvas on the right containing a single button. A Control-drag arrow connects the button on the canvas to the view controller in the document outline.](https://docs-assets.developer.apple.com/published/90613da3ff62308359f7e291584b3279/media-4109954%402x.png)

![A screenshot in Xcode showing a modal alert of connection options after completing a Control-drag action. The modal lists several action segue options including Show, Show Detail, and Present Modally. An arrow points to the signInButton Tapped option.](https://docs-assets.developer.apple.com/published/8a11490cb7c3caab14480f0f5cbb893f/media-4109951%402x.png)

You can verify that the control and action are connected by moving the pointer over the circular dot to the left of the action method. When you do, Xcode highlights the control.

![A screenshot  in Xocde showing how moving the pointer over an action method in the code editor highlights the control it’s connected to in Interface Builder. Interface Builder is on the left with a highlighted button. The Assistant code editor is open on the right with the mouse tip hovering over the grey circle immediately to the left of the function definition.](https://docs-assets.developer.apple.com/published/3ad0351f2669de731034412de0ab3116/media-4110023%402x.png)

Another way to connect is to Control-drag the control from Interface Builder into the view controller.

![A screenshot in Xcode showing how Control-dragging a control from Interface Builder into the Assistant editor generates the target-action method. Interface Builder is open on the left. The Assistant editor is open beside it on the right. An arrow points from the button into the code editor with the words Control-drag appearing above it.](https://docs-assets.developer.apple.com/published/594b61e310e61c568d772d70c38e5b03/media-4109950%402x.png)

Enter the name of the `action` method you’d like the control to call and then click Connect.

![A screenshot in Xcode showing a modal alert resulting from a Control-drag action between Interface Builder and the Assistant editor. The modal shows the fields Connection, Object, Name, Type, Event, and Arguments. Two buttons appear at the bottom: a Cancel button on the left and a Connect button on the right.](https://docs-assets.developer.apple.com/published/28a830c43c2151941d9d2d44293e7cc5/media-4110161%402x.png)

The following table lists the parameters available for configuration.

| Parameter | Description |
| --- | --- |
| Connection | The type of connection to make. Select Action to establish a target-action relationship between the control and the target. |
| Object | The `target` or object your control is connecting to. |
| Name | The name of the function, or `action`, your control calls when the event occurs. |
| Type | The type of the control sending the event. Choose `Any` if you don’t require any further information regarding the control’s state. Specify the control type if you require more information from the control for event processing. |
| Event | The [`UIEvent`](uievent.md) associated with the action. This feature is only available in UIKit. |
| Arguments | The arguments to include in the signature or your target-action method. Choose None to include no arguments. Choose Sender to pass in the control type as the sender. Choose Sender and Event to pass in both the control type and the event that caused the action. This feature is available only in UIKit. |

Connecting the target-action this way ensures the method signature and parameters are correct as Xcode generates the action method for you.

![A screenshot in Xcode showing the generated code resulting from a Control-drag action from Interface Builder into the Assistant code editor. Interface Builder is open on the left. The Assistant editor is open beside it on the right. And inside the editor is the generated code. An arrow with the title Generated is pointing to the newly generated code.](https://docs-assets.developer.apple.com/published/5638d104c958057f451b05e8129b1637/media-4110163%402x.png)

##### Connect a Control to Your Code Programmatically

In UIKit, use the [`addTarget(_:action:for:)`](uicontrol/addtarget(_:action:for:).md) method to set up target-action programmatically on a control:

In AppKit, use the control’s `target` and `action` properties to set target-action programmatically:

##### Enable Other Objects to Respond to Control Related Events

When the object hosting the control isn’t the one you want handling the event, invoke the responder chain by passing in `nil` as the target. This causes the control to search the responder chain for the specified action method and invoke it when found. For more information, see [`Using responders and the responder chain to handle events`](using-responders-and-the-responder-chain-to-handle-events.md).

## See Also

- [class UIControl](uicontrol.md)
  The base class for controls, which are visual elements that convey a specific action or intention in response to user interactions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/responding-to-control-based-events-using-target-action)*