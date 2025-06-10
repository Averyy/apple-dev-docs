# newTextures(names:scaleFactor:displayGamut:bundle:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method

Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [any MTLTexture]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [MTLTexture]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `names`: An array of strings, each the name of a texture in an asset catalog.
- `scaleFactor`: In macOS, pass the   value of the window where you plan to display texture content.
- `displayGamut`: To determine the appropriate parameter value, pass the widest   value that returns   when queried against the   method of  .
- `bundle`: The resource bundle containing the asset catalog to load textures from.
- `options`: When using this method, the texture loader ignores the  ,  ,  , and   options.
- `completionHandler`: A block called after all assets have been processed. See the   signature to determine whether each texture has successfully loaded.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtextures(names:scalefactor:displaygamut:bundle:options:completionhandler:))*