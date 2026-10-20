# spotDirection

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A vector indicating the direction the spotlight is projecting.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var spotDirection: GLKVector3 { get set }
```

```objc
@property (nonatomic, assign) GLKVector3 spotDirection;
```

#### Discussion

The default direction is `[0.0, 0.0, -1.0]`.

## See Also

### Configuring Spotlight Properties
- [var spotCutoff: GLfloat](./spotcutoff.md)
  The angle in degrees where the spotlight is cut off.
- [var spotExponent: GLfloat](./spotexponent.md)
  A value indicating how focused the spotlight is.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/spotdirection)*