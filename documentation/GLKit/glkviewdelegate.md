# GLKViewDelegate

**Framework**: GLKit  
**Kind**: protocol

Drawing callback methods for use with a [`GLKView`](glkview.md) object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
protocol GLKViewDelegate : NSObjectProtocol
```

#### Overview

An object that implements the [`GLKViewDelegate`](glkviewdelegate.md) protocol can be set as a [`GLKView`](glkview.md) object’s delegate. A delegate allows your application to provide a drawing method to a [`GLKView`](glkview.md) object without subclassing the [`GLKView`](glkview.md) class.

## Topics

### Drawing the View’s Contents
- [func glkView(GLKView, drawIn: CGRect)](glkviewdelegate/glkview(_:drawin:).md)
  Draws the view’s contents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [GLKViewController](glkviewcontroller.md)

## See Also

- [class GLKView](glkview.md)
  A default implementation for views that draw their content using OpenGL ES.
- [class GLKViewController](glkviewcontroller.md)
  A view controller that manages an OpenGL ES rendering loop.
- [protocol GLKViewControllerDelegate](glkviewcontrollerdelegate.md)
  Rendering loop callback methods for use with a [`GLKViewController`](glkviewcontroller.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewdelegate)*