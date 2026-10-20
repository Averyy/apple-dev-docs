# GLKViewControllerDelegate

**Framework**: GLKit  
**Kind**: protocol  
**Role**: Protocol

Rendering loop callback methods for use with a [`GLKViewController`](./glkviewcontroller.md) object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
protocol GLKViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol GLKViewControllerDelegate <NSObject>
```

#### Overview

A delegate is called each time the controller is about to display a new frame of animation. It is also called before the view controller’s rendering loop pauses or resumes sending updates.

## Topics

### Handling an Update Event
- [func glkViewControllerUpdate(GLKViewController)](./glkviewcontrollerdelegate/glkviewcontrollerupdate%28_%29.md)
  Called before each frame is displayed.
### Pause and Resume Notifications
- [func glkViewController(GLKViewController, willPause: Bool)](./glkviewcontrollerdelegate/glkviewcontroller%28_,willpause%29.md)
  Called before the rendering loop is paused or resumed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### OpenGL ES View Rendering
- [class GLKView](./glkview.md)
  A default implementation for views that draw their content using OpenGL ES.
- [protocol GLKViewDelegate](./glkviewdelegate.md)
  Drawing callback methods for use with a [`GLKView`](./glkview.md) object.
- [class GLKViewController](./glkviewcontroller.md)
  A view controller that manages an OpenGL ES rendering loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate)*