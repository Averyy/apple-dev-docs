# init(api:)

**Framework**: OpenGL ES  
**Kind**: init

Initializes and returns a newly allocated rendering context with the specified version of the OpenGL ES rendering API.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
convenience init?(api: EAGLRenderingAPI)
```

#### Return Value

An initialized context object, or `nil` if the object couldn’t be created.

#### Discussion

To issue OpenGL ES commands to this context, you must first make the context current by calling [`setCurrent(_:)`](eaglcontext/setcurrent(_:).md).

Calling [`init(api:)`](eaglcontext/init(api:).md) creates a new [`EAGLSharegroup`](eaglsharegroup.md) object and attaches it to this context.

## Parameters

- `api`: The desired version of the OpenGL ES rendering API. For legal values, see  .

## See Also

- [OpenGL ES Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/init(api:))*