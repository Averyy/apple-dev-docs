# init(api:sharegroup:)

**Framework**: OpenGL ES  
**Kind**: init

Initializes and returns a newly allocated rendering context with the specified version of OpenGL ES rendering API and the specified sharegroup.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
init?(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup)
```

#### Return Value

An initialized context object, or `nil` if the object couldn’t be created.

#### Discussion

To issue OpenGL ES commands to this context, you must first make it the current drawing context by calling [`setCurrent(_:)`](eaglcontext/setcurrent(_:).md).

OpenGL ES objects such as textures, renderbuffers, framebuffers and vertex buffers are shared across all contexts that are created with the same sharegroup. To specify that a new context should be initialized in an existing sharegroup, retrieve the [`sharegroup`](eaglcontext/sharegroup.md) property from a previously initialized context and pass it as a parameter to this initialization method. Pass `nil` as the `sharegroup` parameter to create a new [`EAGLSharegroup`](eaglsharegroup.md) object attached to the context.

## Parameters

- `api`: The desired version of the OpenGL ES rendering API. For legal values, see  .
- `sharegroup`: A sharegroup obtained from another   object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/init(api:sharegroup:))*