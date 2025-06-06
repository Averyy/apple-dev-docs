# init(cubeWithImagesNamed:bundle:)

**Framework**: Model I/O  
**Kind**: init

Loads a cube texture from the specified image files in the specified bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(cubeWithImagesNamed names: [String], bundle bundleOrNil: Bundle?)
```

#### Return Value

A new cube texture object, or `nil` if the specified files could not be found.

#### Discussion

You can create a cube texture with any of the following combinations of images:

- 6 square images of the same size, containing the +X, -X, +Y, -Y, +Z, and -Z faces of the cube in that order.
- 3 images, each of which has height twice its width. Each image contains both the positive and negative faces for one axis of the cube, and the three images are in the order X, Y, then Z.
- 2 images, each of which has height three times its width. The first image contains the +X, +Y, and +Z faces of the cube, and the second image contains the -X, -Y, and -Z faces.
- A single image. If the image’s height is six times its width, Model I/O assumes it to contain the the +X, -X, +Y, -Y, +Z, and -Z faces of the cube in that order and leaves the image data unchanged. If the images width is six times its height, Model I/O rearranges the image data into the vertical format.

Calling this method with any other arrangement of images returns `nil`.

After initialization, the texture’s data (accessible through the methods listed in Accessing Texture Data) is organized such that the six faces are in one image whose height is six times its width, and its [`dimensions`](mdltexture/dimensions.md) property reflects this arrangement.

This method does not cache the texture objects it creates.

## Parameters

- `names`: An array of strings, each the name (including extension) of an image file.
- `bundleOrNil`: The bundle the image files are located in, or   to use the main bundle.

## See Also

- [convenience init?(named: String)](mdltexture/init(named:).md)
  Loads the texture with the specified filename from the app’s main bundle.
- [convenience init?(named: String, bundle: Bundle?)](mdltexture/init(named:bundle:).md)
  Loads the texture with the specified filename from the specified bundle.
- [convenience init?(cubeWithImagesNamed: [String])](mdltexture/init(cubewithimagesnamed:).md)
  Loads a cube texture from the specified image files in the app’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltexture/init(cubewithimagesnamed:bundle:))*