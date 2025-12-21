# GLKViewController

**Framework**: GLKit  
**Kind**: class

A view controller that manages an OpenGL ES rendering loop.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@MainActor
class GLKViewController
```

#### Overview

A [`GLKViewController`](glkviewcontroller.md) object works in conjunction with a [`GLKView`](glkview.md) object to display frames of animation in the view, and also provides standard view controller functionality.

To use this class, allocate and initialize a new [`GLKViewController`](glkviewcontroller.md) subclass and set its [`view`](https://developer.apple.com/documentation/UIKit/UIViewController/view) property to point to a [`GLKView`](glkview.md) object. Then, configure the view controller’s [`preferredFramesPerSecond`](glkviewcontroller/preferredframespersecond.md) property to the desired frame rate your application requires. You can set a delegate or configure other properties on the view controller, such as whether the animation loop is automatically paused or resumed when the application moves into the background.

> **Note**:  When you set the [`view`](https://developer.apple.com/documentation/UIKit/UIViewController/view) property to point to a [`GLKView`](glkview.md) object, if the view does not already have a delegate, then the view controller is automatically set as the view’s delegate.

When active, rendering loop automatically updates the view’s contents each time a new frame must be displayed. Each frame is rendered by the view controller using these steps:

1. The view controller calls its delegate’s [`glkViewControllerUpdate(_:)`](glkviewcontrollerdelegate/glkviewcontrollerupdate(_:).md) method. Your delegate should update frame data that does not involve rendering the results to the screen.
2. The view controller calls its view’s [`display()`](glkview/display().md) method. Your view should redraw the frame.

##### Subclassing Notes

Your application should subclass [`GLKViewController`](glkviewcontroller.md) and override the [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) and [`viewDidUnload`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidUnload) methods. Your `viewDidLoad` method should set up your context and any drawable properties and can perform other resource allocation and initialization. Similarly, your class’s `viewDidUnload` method should delete the drawable object and free any unneeded resources.

As an alternative to implementing a [`glkViewControllerUpdate(_:)`](glkviewcontrollerdelegate/glkviewcontrollerupdate(_:).md) method in a delegate, your subclass can provide an update method instead. The method must have the following signature:

```objc
- (void)update;
```

## Topics

### Configuring the Frame rate
- [var preferredFramesPerSecond: Int](glkviewcontroller/preferredframespersecond.md)
  The rate you want the view controller to call the view to update the contents of the view.
- [var framesPerSecond: Int](glkviewcontroller/framespersecond.md)
  The actual rate that the view controller attempts to call the view to update its contents.
### Configuring the Delegate
- [var delegate: (any GLKViewControllerDelegate)?](glkviewcontroller/delegate.md)
  The view controller’s delegate.
### Controlling Frame Updates
- [var isPaused: Bool](glkviewcontroller/ispaused.md)
  A Boolean value that indicates whether the rendering loop is paused.
- [var pauseOnWillResignActive: Bool](glkviewcontroller/pauseonwillresignactive.md)
  A Boolean value that indicates whether the view controller automatically pauses the rendering loop when the application resigns the active state.
- [var resumeOnDidBecomeActive: Bool](glkviewcontroller/resumeondidbecomeactive.md)
  A Boolean value that indicates whether the view controller automatically resumes the rendering loop when the application becomes active.
### Obtaining Information About View Updates
- [var framesDisplayed: Int](glkviewcontroller/framesdisplayed.md)
  The number of frame updates that have been sent by the view controller since it was created.
- [var timeSinceFirstResume: TimeInterval](glkviewcontroller/timesincefirstresume.md)
  The amount of time that has passed since first time the view controller resumed sending update events.
- [var timeSinceLastResume: TimeInterval](glkviewcontroller/timesincelastresume.md)
  The amount of time that has passed since the last time the view controller resumed sending update events.
- [var timeSinceLastUpdate: TimeInterval](glkviewcontroller/timesincelastupdate.md)
  The amount of time that has passed since the last time the view controller called the delegate’s [`glkViewControllerUpdate(_:)`](glkviewcontrollerdelegate/glkviewcontrollerupdate(_:).md) method.
- [var timeSinceLastDraw: TimeInterval](glkviewcontroller/timesincelastdraw.md)
  The amount of time that has passed since the last time the view controller called the view’s [`display()`](glkview/display().md) method.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GLKViewDelegate](glkviewdelegate.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class GLKView](glkview.md)
  A default implementation for views that draw their content using OpenGL ES.
- [protocol GLKViewDelegate](glkviewdelegate.md)
  Drawing callback methods for use with a [`GLKView`](glkview.md) object.
- [protocol GLKViewControllerDelegate](glkviewcontrollerdelegate.md)
  Rendering loop callback methods for use with a [`GLKViewController`](glkviewcontroller.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller)*