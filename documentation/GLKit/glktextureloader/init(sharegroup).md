# init(sharegroup:)

**Framework**: GLKit  
**Kind**: init  
**Role**: Initializer

Initializes a new texture loader object.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init(sharegroup: EAGLSharegroup)
```

```objc
- (instancetype) initWithSharegroup:(EAGLSharegroup *) sharegroup;
```

#### Return Value

A newly initialized texture loader.

#### Discussion

You only create a texture loader object when your app needs to load textures asynchronously.

## Parameters

- `sharegroup`: The sharegroup used to store new textures.

## See Also

### Initialization
- [init(share: NSOpenGLContext)](./init%28share%29.md)
  Initializes a new texture loader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/init(sharegroup:))*