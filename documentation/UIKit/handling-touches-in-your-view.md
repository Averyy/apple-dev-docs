# Handling touches in your view

**Framework**: UIKit

Use touch events directly on a view subclass if touch handling is intricately linked to the view’s content.

#### Overview

If you don’t plan to use gesture recognizers with a custom view, you can handle touch events directly from the view itself. Because views are responders, they can handle Multi-Touch events and many other types of events. When UIKit determines that a touch event occurred in a view, it calls the view’s [`touchesBegan(_:with:)`](uiresponder/touchesbegan(_:with:).md), [`touchesMoved(_:with:)`](uiresponder/touchesmoved(_:with:).md), or [`touchesEnded(_:with:)`](uiresponder/touchesended(_:with:).md) method. You can override these methods in your custom views and use them to provide a response to touch events.

The methods you override in your views (or in any responder) to handle touches correspond to different phases of the touch event-handling process. For example, the following image illustrates the different phases of a touch event. When a finger (or Apple Pencil) touches the screen, UIKit creates a [`UITouch`](uitouch.md) object, sets the touch location to the appropriate point, and sets its [`phase`](uitouch/phase-swift.property.md) property to [`UITouch.Phase.began`](uitouch/phase-swift.enum/began.md). When the same finger moves around the screen, UIKit updates the touch location and changes the [`phase`](uitouch/phase-swift.property.md) property of the touch object to [`UITouch.Phase.moved`](uitouch/phase-swift.enum/moved.md). When the user lifts the finger from the screen, UIKit changes the [`phase`](uitouch/phase-swift.property.md) property to [`UITouch.Phase.ended`](uitouch/phase-swift.enum/ended.md) and the touch sequence ends.

![A touch begins when the user’s finger touches the screen. The system updates the touch when the user’s finger moves or the touch parameters change. The touch ends when the user lifts the same finger from the screen. If an interruption such as an incoming call occurs, the system cancels any active touches.](https://docs-assets.developer.apple.com/published/57360c42fdb7ff48fdce0fb3f3f9148c/media-3004382%402x.png)

Similarly, the system may cancel an ongoing touch sequence at any time; for example, when an incoming phone call interrupts the app. When it does, UIKit notifies your view by calling the [`touchesCancelled(_:with:)`](uiresponder/touchescancelled(_:with:).md) method. You use that method to perform any needed cleanup of your view’s data structures.

UIKit creates a new [`UITouch`](uitouch.md) object for each new finger that touches the screen. The touches themselves are delivered with the current [`UIEvent`](uievent.md) object. UIKit distinguishes between touches originating from a finger and from Apple Pencil, and you can treat each of them differently.

> ❗ **Important**:  In its default configuration, a view receives only the first [`UITouch`](uitouch.md) object associated with an event, even if more than one finger is touching the view. To receive the additional touches, you must set the view’s [`isMultipleTouchEnabled`](uiview/ismultipletouchenabled.md) property to true. You can also configure this property in Interface Builder using the Attributes inspector.

 In its default configuration, a view receives only the first [`UITouch`](uitouch.md) object associated with an event, even if more than one finger is touching the view. To receive the additional touches, you must set the view’s [`isMultipleTouchEnabled`](uiview/ismultipletouchenabled.md) property to true. You can also configure this property in Interface Builder using the Attributes inspector.

## Topics

### Advanced touch handling
- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
  Learn how to create a simple app that handles multitouch input.
- [Getting high-fidelity input with coalesced touches](getting-high-fidelity-input-with-coalesced-touches.md)
  Learn how to support high-precision touches in your app.
- [Minimizing latency with predicted touches](minimizing-latency-with-predicted-touches.md)
  Create a smooth and responsive drawing experience using UIKit’s predictions for touch locations.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/handling-touches-in-your-view)*