# init(api:)

**Framework**: OpenGL ES  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated rendering context with the specified version of the OpenGL ES rendering API.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
convenience init?(api: EAGLRenderingAPI)
```

```objc
- (instancetype) initWithAPI:(EAGLRenderingAPI) api;
```

## Return Value

An initialized context object, or `nil` if the object couldn’t be created.

## Discussion

To issue OpenGL ES commands to this context, you must first make the context current by calling [`setCurrent(_:)`](./setcurrent%28_%29.md).

Calling [`init(api:)`](./init%28api%29-q09o.md) creates a new [`EAGLSharegroup`](../eaglsharegroup.md) object and attaches it to this context.

## Parameters

- `api`: The desired version of the OpenGL ES rendering API. For legal values, see [`EAGLRenderingAPI`](../eaglrenderingapi.md).

## See Also

### Related Documentation
- [OpenGL ES Programming Guide](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/init(api:)-q09o)*