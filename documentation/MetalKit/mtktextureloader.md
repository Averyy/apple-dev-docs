# MTKTextureLoader

**Framework**: MetalKit  
**Kind**: class

An object that creates textures from existing data in common image formats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTKTextureLoader
```

#### Overview

Use the [`MTKTextureLoader`](mtktextureloader.md) class to create a Metal texture from existing image data.

This class supports common file formats, like PNG, JPEG, and TIFF. It also loads image data from KTX and PVR files, asset catalogs, Core Graphics images, and other sources. It infers the output texture format and pixel format from the image data.

You create textures synchronously or asynchronously using [`MTKTextureLoader`](mtktextureloader.md) methods that return [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) instances. Pass options to these methods that customize the image-loading and texture-creation process.

First create an [`MTKTextureLoader`](mtktextureloader.md) instance, passing the device that it uses to create textures. Then use one of the texture loader’s methods to create a texture. The code example below synchronously creates a texture from data at a URL, using the default options:

If you use custom data formats, or change the image data at runtime, use [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) methods instead. For more information, see [`Creating and sampling textures`](https://developer.apple.com/documentation/Metal/creating-and-sampling-textures).

## Topics

### Creating a Texture Loader
- [init(device: any MTLDevice)](mtktextureloader/init(device:).md)
  Initializes a new texture loader object.
- [var device: any MTLDevice](mtktextureloader/device.md)
  The device object that the texture loader uses to create textures.
### Loading Textures from URLs
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(url:options:).md)
  Synchronously loads image data and creates a new Metal texture from a given URL.
- [func newTexture(URL: URL, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(url:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given URL.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, error: NSErrorPointer) -> [any MTLTexture]](mtktextureloader/newtextures(urls:options:error:).md)
  Synchronously loads image data and creates new Metal textures from the specified list of URLs.
- [func newTextures(URLs: [URL], options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(urls:options:completionhandler:).md)
  Asynchronously loads image data and creates new Metal textures from the specified list of URLs.
### Loading Textures from Asset Catalogs
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(name:scalefactor:bundle:options:).md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(name:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:).md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog, using a specified display gamut.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:displaygamut:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.
### Loading Textures from Core Graphics Images
- [func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(cgimage:options:).md)
  Synchronously loads image data and creates a new Metal texture from a given bitmap image.
- [func newTexture(cgImage: CGImage, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(cgimage:options:completionhandler:).md)
  Asynchronously loads image data and creates a new Metal texture from a given bitmap image.
### Loading Textures from In-Memory Data Representations
- [func newTexture(data: Data, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(data:options:).md)
  Synchronously creates a new Metal texture from an in-memory representation of the texture’s data.
- [func newTexture(data: Data, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(data:options:completionhandler:).md)
  Asynchronously creates a new Metal texture from an in-memory representation of the texture’s data.
### Loading Textures from Model I/O Representations
- [func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(texture:options:).md)
  Synchronously loads image data and creates a Metal texture from the specified Model I/O texture.
- [func newTexture(texture: MDLTexture, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(texture:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the specified Model I/O texture.
### Specifying Loading Options
- [MTKTextureLoader.Option](mtktextureloader/option.md)
  Keys and values used to specify loading options.
### Completing a Texture Loading Operation
- [MTKTextureLoader.ArrayCallback](mtktextureloader/arraycallback.md)
  The signature for the block executed after an asynchronous loading operation for multiple textures has completed.
- [MTKTextureLoader.Callback](mtktextureloader/callback.md)
  The signature for the block executed after an asynchronous loading operation for a single texture has completed.
### Handling Errors
- [MTKTextureLoader.Error](mtktextureloader/error.md)
  Errors returned by the texture loader.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader)*