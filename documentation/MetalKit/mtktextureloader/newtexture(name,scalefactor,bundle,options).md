# newTexture(name:scaleFactor:bundle:options:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) throws -> any MTLTexture
```

```objc
- (id<MTLTexture>) newTextureWithName:(NSString *) name scaleFactor:(CGFloat) scaleFactor bundle:(NSBundle *) bundle options:(NSDictionary<NSString *,id> *) options error:(NSError **) error;
```

#### Return Value

A fully loaded and initialized Metal texture, or `nil` if an error occurred.

## Parameters

- `name`: The name of a texture in an asset catalog.
- `scaleFactor`: The scale factor of texture to request.

  In iOS and tvOS, pass the [`contentsScale`](../../QuartzCore/calayer/contentsscale.md) value of the view where you plan to display texture content.

  In macOS, pass the [`backingScaleFactor`](../../AppKit/nswindow/backingscalefactor.md) value of the window where you plan to display texture content.
- `bundle`: The resource bundle containing the asset catalog to load textures from.
- `options`: A dictionary describing any additional texture loading steps. See  [Texture Loading Options](../../GLKit/texture-loading-options.md).

  When using this method, the texture loader ignores the [`generateMipmaps`](./option/generatemipmaps.md), [`SRGB`](./option/srgb.md), [`cubeLayout`](./option/cubelayout.md), and [`origin`](./option/origin.md) options.

## See Also

### Loading Textures from Asset Catalogs
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28name,scalefactor,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](./newtextures%28names,scalefactor,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](./newtexture%28name,scalefactor,displaygamut,bundle,options%29.md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog, using a specified display gamut.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28name,scalefactor,displaygamut,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](./newtextures%28names,scalefactor,displaygamut,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtexture(name:scalefactor:bundle:options:))*