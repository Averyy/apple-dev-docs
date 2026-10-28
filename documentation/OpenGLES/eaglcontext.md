# EAGLContext

**Framework**: OpenGL ES  
**Kind**: class  
**Role**: Class

An [`EAGLContext`](./eaglcontext.md) object manages an OpenGL ES *rendering context*—the state information, commands, and resources needed to draw using OpenGL ES. To execute OpenGL ES commands, you need a current rendering context.

**Availability**:
- iOS 2.0+ - Deprecated in 12.0
- iPadOS 2.0+ - Deprecated in 12.0
- Mac Catalyst 2.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class EAGLContext
```

```objc
@interface EAGLContext : NSObject
```

## Overview

Drawing resources, such as textures and renderbuffers, are managed for the [`EAGLContext`](./eaglcontext.md) object by an [`EAGLSharegroup`](./eaglsharegroup.md) object associated with the context. When you initialize a new [`EAGLContext`](./eaglcontext.md) object, you can choose to have it create a new sharegroup, or you can use one obtained from a previously created context.

Before drawing to a context, you must bind a complete framebuffer object to the context. For more information on configuring rendering contexts, see [OpenGL ES Programming Guide](https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793).

## Topics

### Creating Contexts
- [convenience init?(api: EAGLRenderingAPI)](./eaglcontext/init%28api%29-q09o.md)
  Initializes and returns a newly allocated rendering context with the specified version of the OpenGL ES rendering API.
- [init?(api: EAGLRenderingAPI, sharegroup: EAGLSharegroup)](./eaglcontext/init%28api,sharegroup%29-2rt8m.md)
  Initializes and returns a newly allocated rendering context with the specified version of OpenGL ES rendering API and the specified sharegroup.
### Setting the Current Context
- [class func setCurrent(EAGLContext?) -> Bool](./eaglcontext/setcurrent%28_%29.md)
  Makes the specified context the current rendering context for the calling thread.
### Attaching Storage to a Renderbuffer
- [func renderbufferStorage(Int, from: (any EAGLDrawable)?) -> Bool](./eaglcontext/renderbufferstorage%28_,from%29.md)
  Binds a drawable object’s storage to an OpenGL ES renderbuffer object.
### Displaying a Renderbuffer
- [func presentRenderbuffer(Int) -> Bool](./eaglcontext/presentrenderbuffer%28_%29.md)
  Displays a renderbuffer’s contents on screen.
### Getting Context Information
- [var api: EAGLRenderingAPI](./eaglcontext/api.md)
  The OpenGL ES rendering API version supported by the context. (read-only)
- [var sharegroup: EAGLSharegroup](./eaglcontext/sharegroup.md)
  The context’s sharegroup object. (read-only)
- [var debugLabel: String?](./eaglcontext/debuglabel.md)
  A label describing the context for use in debugging.
- [class func current() -> EAGLContext?](./eaglcontext/current%28%29.md)
  Returns the current rendering context for the calling thread.
### Enabling OpenGL ES Multithreading
- [var isMultiThreaded: Bool](./eaglcontext/ismultithreaded.md)
  A Boolean value that determines whether OpenGL ES defers work to another thread.
### Constants
- [enum EAGLRenderingAPI](./eaglrenderingapi.md)
  Versions of OpenGL ES that a rendering context provides.
### Instance Methods
- [func presentRenderbuffer(Int, afterMinimumDuration: CFTimeInterval) -> Bool](./eaglcontext/presentrenderbuffer%28_,afterminimumduration%29.md)
- [func presentRenderbuffer(Int, atTime: CFTimeInterval) -> Bool](./eaglcontext/presentrenderbuffer%28_,attime%29.md)
- [func texImageIOSurface(IOSurfaceRef, target: Int, internalFormat: Int, width: UInt32, height: UInt32, format: Int, type: Int, plane: UInt32) -> Bool](./eaglcontext/teximageiosurface%28_,target,internalformat,width,height,format,type,plane%29.md)
### Initializers
- [convenience init?(API: EAGLRenderingAPI)](./eaglcontext/init%28api%29-54mtn.md)
- [init?(API: EAGLRenderingAPI, sharegroup: EAGLSharegroup)](./eaglcontext/init%28api,sharegroup%29-3gr8h.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/eaglcontext)*