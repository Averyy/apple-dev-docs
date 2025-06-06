# init(named:)

**Framework**: Model I/O  
**Kind**: init

Loads the texture with the specified filename from the app’s main bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(named name: String)
```

#### Return Value

A new texture object for the specified image file, or `nil` if no such file exists.

#### Discussion

Calling this method immediately loads image data from the specified file. To instead create a texture object referencing a file and defer loading image data, use the [`MDLURLTexture`](mdlurltexture.md) class.

This method does not cache the texture objects it creates; calling this method again with the same `name` parameter as a previous call will load image data from the file again.

## Parameters

- `name`: The name, including extension, of the image file to load as a texture.

## See Also

- [convenience init?(named: String, bundle: Bundle?)](mdltexture/init(named:bundle:).md)
  Loads the texture with the specified filename from the specified bundle.
- [convenience init?(cubeWithImagesNamed: [String])](mdltexture/init(cubewithimagesnamed:).md)
  Loads a cube texture from the specified image files in the app’s main bundle.
- [convenience init?(cubeWithImagesNamed: [String], bundle: Bundle?)](mdltexture/init(cubewithimagesnamed:bundle:).md)
  Loads a cube texture from the specified image files in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/init(named:))*