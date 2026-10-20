# GLKViewController

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

A view controller that manages an OpenGL ES rendering loop.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKViewController
```

```objc
@interface GLKViewController : UIViewController
```

#### Overview

A [`GLKViewController`](./glkviewcontroller.md) object works in conjunction with a [`GLKView`](./glkview.md) object to display frames of animation in the view, and also provides standard view controller functionality.

To use this class, allocate and initialize a new [`GLKViewController`](./glkviewcontroller.md) subclass and set its [`view`](../UIKit/uiviewcontroller/view.md) property to point to a [`GLKView`](./glkview.md) object. Then, configure the view controller’s [`preferredFramesPerSecond`](./glkviewcontroller/preferredframespersecond.md) property to the desired frame rate your application requires. You can set a delegate or configure other properties on the view controller, such as whether the animation loop is automatically paused or resumed when the application moves into the background.

> **Note**:  When you set the [`view`](../UIKit/uiviewcontroller/view.md) property to point to a [`GLKView`](./glkview.md) object, if the view does not already have a delegate, then the view controller is automatically set as the view’s delegate.

When active, rendering loop automatically updates the view’s contents each time a new frame must be displayed. Each frame is rendered by the view controller using these steps:

1. The view controller calls its delegate’s [`glkViewControllerUpdate(_:)`](./glkviewcontrollerdelegate/glkviewcontrollerupdate%28_%29.md) method. Your delegate should update frame data that does not involve rendering the results to the screen.
2. The view controller calls its view’s [`display()`](./glkview/display%28%29.md) method. Your view should redraw the frame.

##### Subclassing Notes

Your application should subclass [`GLKViewController`](./glkviewcontroller.md) and override the [`viewDidLoad()`](../UIKit/uiviewcontroller/viewdidload%28%29.md) and [`viewDidUnload`](../UIKit/uiviewcontroller/viewdidunload.md) methods. Your `viewDidLoad` method should set up your context and any drawable properties and can perform other resource allocation and initialization. Similarly, your class’s `viewDidUnload` method should delete the drawable object and free any unneeded resources.

As an alternative to implementing a [`glkViewControllerUpdate(_:)`](./glkviewcontrollerdelegate/glkviewcontrollerupdate%28_%29.md) method in a delegate, your subclass can provide an update method instead. The method must have the following signature:

```objc
- (void)update;
```

## Topics

### Configuring the Frame rate
- [var preferredFramesPerSecond: Int](./glkviewcontroller/preferredframespersecond.md)
  The rate you want the view controller to call the view to update the contents of the view.
- [var framesPerSecond: Int](./glkviewcontroller/framespersecond.md)
  The actual rate that the view controller attempts to call the view to update its contents.
### Configuring the Delegate
- [var delegate: (any GLKViewControllerDelegate)?](./glkviewcontroller/delegate.md)
  The view controller’s delegate.
### Controlling Frame Updates
- [var isPaused: Bool](./glkviewcontroller/ispaused.md)
  A Boolean value that indicates whether the rendering loop is paused.
- [var pauseOnWillResignActive: Bool](./glkviewcontroller/pauseonwillresignactive.md)
  A Boolean value that indicates whether the view controller automatically pauses the rendering loop when the application resigns the active state.
- [var resumeOnDidBecomeActive: Bool](./glkviewcontroller/resumeondidbecomeactive.md)
  A Boolean value that indicates whether the view controller automatically resumes the rendering loop when the application becomes active.
### Obtaining Information About View Updates
- [var framesDisplayed: Int](./glkviewcontroller/framesdisplayed.md)
  The number of frame updates that have been sent by the view controller since it was created.
- [var timeSinceFirstResume: TimeInterval](./glkviewcontroller/timesincefirstresume.md)
  The amount of time that has passed since first time the view controller resumed sending update events.
- [var timeSinceLastResume: TimeInterval](./glkviewcontroller/timesincelastresume.md)
  The amount of time that has passed since the last time the view controller resumed sending update events.
- [var timeSinceLastUpdate: TimeInterval](./glkviewcontroller/timesincelastupdate.md)
  The amount of time that has passed since the last time the view controller called the delegate’s [`glkViewControllerUpdate(_:)`](./glkviewcontrollerdelegate/glkviewcontrollerupdate%28_%29.md) method.
- [var timeSinceLastDraw: TimeInterval](./glkviewcontroller/timesincelastdraw.md)
  The amount of time that has passed since the last time the view controller called the view’s [`display()`](./glkview/display%28%29.md) method.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GLKViewDelegate](./glkviewdelegate.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### OpenGL ES View Rendering
- [class GLKView](./glkview.md)
  A default implementation for views that draw their content using OpenGL ES.
- [protocol GLKViewDelegate](./glkviewdelegate.md)
  Drawing callback methods for use with a [`GLKView`](./glkview.md) object.
- [protocol GLKViewControllerDelegate](./glkviewcontrollerdelegate.md)
  Rendering loop callback methods for use with a [`GLKViewController`](./glkviewcontroller.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller)*