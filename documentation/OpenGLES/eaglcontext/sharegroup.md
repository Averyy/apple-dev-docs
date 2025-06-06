# sharegroup

**Framework**: OpenGL ES  
**Kind**: property

The context’s sharegroup object. (read-only)

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
var sharegroup: EAGLSharegroup { get }
```

#### Discussion

Retrieve the sharegroup of a context when you want to create two or more contexts that share rendering resources. Call [`init(api:)`](eaglcontext/init(api:).md) to initialize the first context, retrieve its sharegroup, and then initialize additional contexts by calling [`init(api:sharegroup:)`](eaglcontext/init(api:sharegroup:).md), passing this sharegroup as the parameter.

## See Also

- [init?(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup)](eaglcontext/init(api:sharegroup:).md)
  Initializes and returns a newly allocated rendering context with the specified version of OpenGL ES rendering API and the specified sharegroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext/sharegroup)*