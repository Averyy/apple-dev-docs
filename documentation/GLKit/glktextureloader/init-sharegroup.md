# init(sharegroup:)

**Framework**: GLKit  
**Kind**: init

Initializes a new texture loader object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
init(sharegroup: EAGLSharegroup)
```

#### Return Value

A newly initialized texture loader.

#### Discussion

You only create a texture loader object when your app needs to load textures asynchronously.

## Parameters

- `sharegroup`: The sharegroup used to store new textures.

## See Also

- [init(share: NSOpenGLContext)](glktextureloader/init(share:).md)
  Initializes a new texture loader object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/init(sharegroup:))*