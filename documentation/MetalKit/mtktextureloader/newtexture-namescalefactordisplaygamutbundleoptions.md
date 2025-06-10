# newTexture(name:scaleFactor:displayGamut:bundle:options:)

**Framework**: MetalKit  
**Kind**: method

Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog, using a specified display gamut.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `name`: The name of a texture in an asset catalog.
- `scaleFactor`: In macOS, pass the   value of the window where you plan to display texture content.
- `displayGamut`: To determine the appropriate parameter value, pass the widest   value that returns   when queried against the   method of  .
- `bundle`: The resource bundle containing the asset catalog to load textures from.
- `options`: When using this method, the texture loader ignores the  ,  ,  , and   options.

## See Also

- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(name:scalefactor:bundle:options:).md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(name:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:displaygamut:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:))*