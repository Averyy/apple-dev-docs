# newTextures(names:scaleFactor:bundle:options:completionHandler:)

**Framework**: MetalKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil, completionHandler: @escaping @Sendable ([any MTLTexture], (any Error)?) -> Void)
```

```swift
func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [any MTLTexture]
```

```objc
- (void) newTexturesWithNames:(NSArray<NSString *> *) names scaleFactor:(CGFloat) scaleFactor bundle:(NSBundle *) bundle options:(NSDictionary<NSString *,id> *) options completionHandler:(MTKTextureLoaderArrayCallback) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func newTextures(names: [String], scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]? = nil) async throws -> [MTLTexture]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `names`: An array of strings, each the name of a texture in an asset catalog.
- `scaleFactor`: The scale factor of texture to request.

  In iOS and tvOS, pass the [`contentsScale`](../../QuartzCore/calayer/contentsscale.md) value of the view where you plan to display texture content.

  In macOS, pass the [`backingScaleFactor`](../../AppKit/nswindow/backingscalefactor.md) value of the window where you plan to display texture content.
- `bundle`: The resource bundle containing the asset catalog to load textures from.
- `options`: A dictionary describing any additional texture loading steps. See `Texture Loading Options`.

  When using this method, the texture loader ignores the [`generateMipmaps`](./option/generatemipmaps.md), [`SRGB`](./option/srgb.md), [`cubeLayout`](./option/cubelayout.md), and [`origin`](./option/origin.md) options.
- `completionHandler`: A block called after all assets have been processed. See the [`MTKTextureLoader.ArrayCallback`](./arraycallback.md) signature to determine whether each texture has successfully loaded.

## See Also

### Loading Textures from Asset Catalogs
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](./newtexture%28name,scalefactor,bundle,options%29.md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28name,scalefactor,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?) throws -> any MTLTexture](./newtexture%28name,scalefactor,displaygamut,bundle,options%29.md)
  Synchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog, using a specified display gamut.
- [func newTexture(name: String, scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ((any MTLTexture)?, (any Error)?) -> Void)](./newtexture%28name,scalefactor,displaygamut,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates a Metal texture from the named texture asset in an asset catalog.
- [func newTextures(names: [String], scaleFactor: CGFloat, displayGamut: NSDisplayGamut, bundle: Bundle?, options: [MTKTextureLoader.Option : Any]?, completionHandler: ([any MTLTexture], (any Error)?) -> Void)](./newtextures%28names,scalefactor,displaygamut,bundle,options,completionhandler%29.md)
  Asynchronously loads image data and creates Metal textures from the specified list of named texture assets in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtktextureloader/newtextures(names:scalefactor:bundle:options:completionhandler:))*