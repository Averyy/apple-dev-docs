# sharegroup

**Framework**: OpenGL ES  
**Kind**: property  
**Role**: Instance Property

The context’s sharegroup object. (read-only)

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var sharegroup: EAGLSharegroup { get }
```

```objc
@property (readonly, nonnull) EAGLSharegroup * sharegroup;
```

## Discussion

Retrieve the sharegroup of a context when you want to create two or more contexts that share rendering resources. Call [`init(api:)`](./init%28api%29-q09o.md) to initialize the first context, retrieve its sharegroup, and then initialize additional contexts by calling [`init(api:sharegroup:)`](./init%28api,sharegroup%29-2rt8m.md), passing this sharegroup as the parameter.

## See Also

### Related Documentation
- [init?(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup)](./init%28api,sharegroup%29-2rt8m.md)
  Initializes and returns a newly allocated rendering context with the specified version of OpenGL ES rendering API and the specified sharegroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/sharegroup)*