# Touches, presses, and gestures

**Framework**: UIKit

Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.

#### Overview

If you build your apps using standard UIKit views and controls, UIKit automatically handles touch events (including Multitouch events) for you. However, if you use custom views to display your content, you must handle all touch events that occur in your views. There are two ways to handle touch events yourself.

- Use gesture recognizers to track the touches; see [`Handling UIKit gestures`](handling-uikit-gestures.md).
- Track the touches directly in your [`UIView`](uiview.md) subclass; see [`Handling touches in your view`](handling-touches-in-your-view.md).

## Topics

### Essentials
- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md)
  Learn how to handle events that propagate through your app.
- [class UIResponder](uiresponder.md)
  An abstract interface for responding to and handling events.
- [class UIEvent](uievent.md)
  An object that describes a single user interaction with your app.
### Touches
- [Handling touches in your view](handling-touches-in-your-view.md)
  Use touch events directly on a view subclass if touch handling is intricately linked to the view’s content.
- [Handling input from Apple Pencil](handling-input-from-apple-pencil.md)
  Learn how to detect and respond to touches from Apple Pencil.
- [Tracking the force of 3D Touch events](tracking-the-force-of-3d-touch-events.md)
  Manipulate your content based on the force of touches.
- [Illustrating the force, altitude, and azimuth properties of touch input](illustrating-the-force-altitude-and-azimuth-properties-of-touch-input.md)
  Capture Apple Pencil and touch input in views.
- [Leveraging touch input for drawing apps](leveraging-touch-input-for-drawing-apps.md)
  Capture touches as a series of strokes and render them efficiently on a drawing canvas.
- [class UITouch](uitouch.md)
  An object representing the location, size, movement, and force of a touch occurring on the screen.
### Button presses
- [class UIPress](uipress.md)
  An object that represents the presence or movement of a button press on the screen for a particular event.
- [class UIPressesEvent](uipressesevent.md)
  An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller.
### Standard gestures
- [Handling UIKit gestures](handling-uikit-gestures.md)
  Use gesture recognizers to simplify touch handling and create a consistent user experience.
- [Coordinating multiple gesture recognizers](coordinating-multiple-gesture-recognizers.md)
  Discover how to use multiple gesture recognizers on the same view.
- [Adopting hover support for Apple Pencil](adopting-hover-support-for-apple-pencil.md)
  Enhance user feedback for your iPadOS app with a hover preview for Apple Pencil input.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.
- [class UIHoverGestureRecognizer](uihovergesturerecognizer.md)
  A continuous gesture recognizer that interprets pointer movement over a view.
- [class UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
  A continuous gesture recognizer that interprets long-press gestures.
- [class UIPanGestureRecognizer](uipangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures.
- [class UIPinchGestureRecognizer](uipinchgesturerecognizer.md)
  A continuous gesture recognizer that interprets pinching gestures involving two touches.
- [class UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
  A continuous gesture recognizer that interprets rotation gestures involving two touches.
- [class UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
  A continuous gesture recognizer that interprets panning gestures that start near an edge of the screen.
- [class UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
  A discrete gesture recognizer that interprets swiping gestures in one or more directions.
- [class UITapGestureRecognizer](uitapgesturerecognizer.md)
  A discrete gesture recognizer that interprets single or multiple taps.
### Custom gestures
- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md)
  Discover when and how to build your own gesture recognizers.
- [class UIGestureRecognizer](uigesturerecognizer.md)
  The base class for concrete gesture recognizers.
- [protocol UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)
  A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md)
  Enrich your app’s user experience by supporting standard and custom gesture interaction.
### 3D Touch interactions
- [class UIPreviewInteraction](uipreviewinteraction.md)
  A class that registers a view to provide a custom user experience in response to 3D Touch interactions.
- [protocol UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md)
  A set of methods for communicating the progress of a preview interaction.
- [protocol UIPreviewActionItem](uipreviewactionitem.md)
  A set of methods that defines the styles you can apply to peek quick actions and peek quick action groups, and defines a read-only accessor for the user-visible title of a peek quick action.

## See Also

- [Menus and shortcuts](menus-and-shortcuts.md)
  Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Drag and drop](drag-and-drop.md)
  Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Focus-based navigation](focus-based-navigation.md)
  Navigate the interface of your UIKit app using a remote, game controller, or keyboard.
- [Accessibility for UIKit](accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/touches-presses-and-gestures)*