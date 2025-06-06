# EAGLSharegroup

**Framework**: OpenGL ES  
**Kind**: class

An `EAGLSharegroup` object manages OpenGL ES resources associated with one or more `EAGLContext` objects. It is created when an `EAGLContext` object is initialized and disposed of when the last `EAGLContext` object that references it is released. As an opaque object, there is no developer accessible API.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
class EAGLSharegroup
```

#### Overview

Currently, the sharegroup manages textures, buffers, framebuffers, and renderbuffers. It is your application’s responsibility to manage state changes to shared objects when those objects are accessed from multiple contexts in the sharegroup. The results of changing the state of a shared object while it is being used for rendering in another context are undefined. To obtain deterministic results, your application must take explicit steps to ensure that the shared object is not currently being used for rendering while your application modifies it. Further, state changes are not guaranteed to be noticed by another context in the sharegroup until that context rebinds the shared object.

To ensure defined results of state changes to shared objects across contexts in the sharegroup, your application must perform the following tasks, in this order:

1. Call `glFlush` on the rendering context that issues the state-modifying routines.
2. Call `glBindTexture` or `glBindBuffer` on the rendering context that depends on the texture or vertex buffer object state changes, respectively.

A shared object is not deleted until it is no longer bound to any context.

## Topics

### Instance Properties
- [var debugLabel: String?](eaglsharegroup/debuglabel.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [OpenGL ES Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglsharegroup)*