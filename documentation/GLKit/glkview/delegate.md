# delegate

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The view’s delegate.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
@IBOutlet
unowned(unsafe) var delegate: (any GLKViewDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<GLKViewDelegate> delegate;
```

#### Discussion

A delegate is optional. If a delegate is provided, it is called instead of calling a [`draw(_:)`](../../UIKit/uiview/draw%28_%29.md) method whenever the view’s contents need to be drawn. You should either subclass the view to override the `draw` method, or provide a delegate, but not both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/delegate)*