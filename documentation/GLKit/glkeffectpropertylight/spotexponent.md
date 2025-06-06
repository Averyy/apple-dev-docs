# spotExponent

**Framework**: GLKit  
**Kind**: property

A value indicating how focused the spotlight is.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var spotExponent: GLfloat { get set }
```

#### Discussion

The higher the value stored in the [`spotExponent`](glkeffectpropertylight/spotexponent.md) property, the tighter the focus of the spotlight. The default value is `0.0`.

## See Also

- [var spotCutoff: GLfloat](glkeffectpropertylight/spotcutoff.md)
  The angle in degrees where the spotlight is cut off.
- [var spotDirection: GLKVector3](glkeffectpropertylight/spotdirection.md)
  A vector indicating the direction the spotlight is projecting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/spotexponent)*