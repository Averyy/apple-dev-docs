# newTexture(name:scaleFactor:displayGamut:bundle:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method

Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> any MTLTexture
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> MTLTexture
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously).

## Parameters

- `name`: The name of a texture in an asset catalog.
- `scaleFactor`: The scale factor of texture to request. In iOS and tvOS, pass the [`contentsScale`](https://developer.apple.com/documentation/quartzcore/calayer/contentsscale) value of the view where you plan to display texture content. In macOS, pass the [`backingScaleFactor`](https://developer.apple.com/documentation/appkit/nswindow/backingscalefactor) value of the window where you plan to display texture content.
- `displayGamut`: The version of the texture based on the *Gamut* trait in Xcode. To determine the appropriate parameter value, pass the widest `NSDisplayGamut` value that returns [`true`](https://developer.apple.com/documentation/swift/true) when queried against the `canRepresentDisplayGamut:` method of `NSWindow`.
- `bundle`: The resource bundle containing the asset catalog to load the texture from.
- `options`: A dictionary describing any additional texture loading steps. See `Texture Loading Options`. When using this method, the texture loader ignores the [`generateMipmaps`](mtktextureloader/option/generatemipmaps.md), [`SRGB`](mtktextureloader/option/srgb.md), [`cubeLayout`](mtktextureloader/option/cubelayout.md), and [`origin`](mtktextureloader/option/origin.md) options.
- `completionHandler`: A block called when the texture has been loaded and fully initialized.

## See Also

- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(name:scalefactor:bundle:options:).md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](mtktextureloader/newtexture(name:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:).md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog, using a specified display gamut.
- [func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](mtktextureloader/newtextures(names:scalefactor:displaygamut:bundle:options:completionhandler:).md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(name:scalefactor:displaygamut:bundle:options:completionhandler:))*