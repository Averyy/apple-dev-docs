# spotExponent

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A value indicating how focused the spotlight is.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var spotExponent: GLfloat { get set }
```

```objc
@property (nonatomic, assign) GLfloat spotExponent;
```

## Discussion

The higher the value stored in the [`spotExponent`](./spotexponent.md) property, the tighter the focus of the spotlight. The default value is `0.0`.

## See Also

### Configuring Spotlight Properties
- [var spotCutoff: GLfloat](./spotcutoff.md)
  The angle in degrees where the spotlight is cut off.
- [var spotDirection: GLKVector3](./spotdirection.md)
  A vector indicating the direction the spotlight is projecting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/spotexponent)*