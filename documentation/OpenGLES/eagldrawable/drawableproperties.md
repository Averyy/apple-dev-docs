# drawableProperties

**Framework**: OpenGL ES  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A dictionary of values that specify the desired characteristics of the drawable surface.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var drawableProperties: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * drawableProperties;
```

#### Discussion

The `drawableProperties` dictionary specifies the properties that are used by this object when it is attached to an OpenGL ES renderbuffer. Your application should set these properties before passing this object into the `EAGLContext` method [`renderbufferStorage(_:from:)`](../eaglcontext/renderbufferstorage%28_,from%29.md). If you change the `drawableProperties` dictionary, your application must call [`renderbufferStorage(_:from:)`](../eaglcontext/renderbufferstorage%28_,from%29.md) again on the context for the new values to take effect.

## See Also

### Related Documentation
- [OpenGL ES Programming Guide](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eagldrawable/drawableproperties)*