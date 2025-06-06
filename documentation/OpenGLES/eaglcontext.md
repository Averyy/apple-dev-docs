# EAGLContext

**Framework**: OpenGL ES  
**Kind**: class

An [`EAGLContext`](eaglcontext.md) object manages an OpenGL ES —the state information, commands, and resources needed to draw using OpenGL ES. To execute OpenGL ES commands, you need a current rendering context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
class EAGLContext
```

#### Overview

Drawing resources, such as textures and renderbuffers, are managed for the [`EAGLContext`](eaglcontext.md) object by an [`EAGLSharegroup`](eaglsharegroup.md) object associated with the context. When you initialize a new [`EAGLContext`](eaglcontext.md) object, you can choose to have it create a new sharegroup, or you can use one obtained from a previously created context.

Before drawing to a context, you must bind a complete framebuffer object to the context. For more information on configuring rendering contexts, see [`OpenGL ES Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793).

## Topics

### Creating Contexts
- [convenience init?(api: EAGLRenderingAPI)](eaglcontext/init(api:).md)
  Initializes and returns a newly allocated rendering context with the specified version of the OpenGL ES rendering API.
- [init?(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup)](eaglcontext/init(api:sharegroup:).md)
  Initializes and returns a newly allocated rendering context with the specified version of OpenGL ES rendering API and the specified sharegroup.
### Setting the Current Context
- [class func setCurrent(EAGLContext?) -> Bool](eaglcontext/setcurrent(_:).md)
  Makes the specified context the current rendering context for the calling thread.
### Attaching Storage to a Renderbuffer
- [func renderbufferStorage(Int, from: (any EAGLDrawable)?) -> Bool](eaglcontext/renderbufferstorage(_:from:).md)
  Binds a drawable object’s storage to an OpenGL ES renderbuffer object.
### Displaying a Renderbuffer
- [func presentRenderbuffer(Int) -> Bool](eaglcontext/presentrenderbuffer(_:).md)
  Displays a renderbuffer’s contents on screen.
### Getting Context Information
- [var api: EAGLRenderingAPI](eaglcontext/api.md)
  The OpenGL ES rendering API version supported by the context. (read-only)
- [var sharegroup: EAGLSharegroup](eaglcontext/sharegroup.md)
  The context’s sharegroup object. (read-only)
- [var debugLabel: String?](eaglcontext/debuglabel.md)
  A label describing the context for use in debugging.
- [class func current() -> EAGLContext?](eaglcontext/current.md)
  Returns the current rendering context for the calling thread.
### Enabling OpenGL ES Multithreading
- [var isMultiThreaded: Bool](eaglcontext/ismultithreaded.md)
  A Boolean value that determines whether OpenGL ES defers work to another thread.
### Constants
- [enum EAGLRenderingAPI](eaglrenderingapi.md)
  Versions of OpenGL ES that a rendering context provides.
### Instance Methods
- [func presentRenderbuffer(Int, afterMinimumDuration: CFTimeInterval) -> Bool](eaglcontext/presentrenderbuffer(_:afterminimumduration:).md)
- [func presentRenderbuffer(Int, atTime: CFTimeInterval) -> Bool](eaglcontext/presentrenderbuffer(_:attime:).md)
- [func texImageIOSurface(IOSurfaceRef, target: Int, internalFormat: Int, width: UInt32, height: UInt32, format: Int, type: Int, plane: UInt32) -> Bool](eaglcontext/teximageiosurface(_:target:internalformat:width:height:format:type:plane:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext)*