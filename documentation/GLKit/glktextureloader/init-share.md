# init(share:)

**Framework**: GLKit  
**Kind**: init

Initializes a new texture loader object.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(share context: NSOpenGLContext)
```

#### Return Value

A newly initialized texture loader.

#### Discussion

You only create a texture loader object when your app needs to load textures asynchronously.

## Parameters

- `context`: The share context used to store new textures.

## See Also

- [init(sharegroup: EAGLSharegroup)](glktextureloader/init(sharegroup:).md)
  Initializes a new texture loader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/init(share:))*