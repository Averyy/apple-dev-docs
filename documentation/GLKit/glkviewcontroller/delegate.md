# delegate

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s delegate.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
@IBOutlet
unowned(unsafe) var delegate: (any GLKViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<GLKViewControllerDelegate> delegate;
```

## Discussion

The delegate is optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontroller/delegate)*