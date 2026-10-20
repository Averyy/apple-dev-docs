# init(share:)

**Framework**: GLKit  
**Kind**: init  
**Role**: Initializer

Initializes a new texture loader object.

**Availability**:
- macOS 10.8+ - Deprecated in 10.14

> **Deprecated**: OpenGL API deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init(share context: NSOpenGLContext)
```

```objc
- (instancetype) initWithShareContext:(NSOpenGLContext *) context;
```

#### Return Value

A newly initialized texture loader.

#### Discussion

You only create a texture loader object when your app needs to load textures asynchronously.

## Parameters

- `context`: The share context used to store new textures.

## See Also

### Initialization
- [init(sharegroup: EAGLSharegroup)](./init%28sharegroup%29.md)
  Initializes a new texture loader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/init(share:))*