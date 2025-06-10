# SKTexture

**Framework**: SpriteKit  
**Kind**: class

An image, decoded on the GPU, that can be used to render various SpriteKit objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SKTexture
```

## Mentions

- [Loading and Using Textures](loading-and-using-textures.md)
- [Getting Started with Sprite Nodes](getting-started-with-sprite-nodes.md)
- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
- [Maximizing Texture Performance](maximizing-texture-performance.md)
- [About Texture Atlases](about-texture-atlases.md)
- [Preloading Textures into Memory](preloading-textures-into-memory.md)

#### Overview

An [`SKTexture`](sktexture.md) object is an image that can be applied to [`SKSpriteNode`](skspritenode.md) and [`SKShapeNode`](skshapenode.md) objects, particles created by an [`SKEmitterNode`](skemitternode.md) object, or tiles used in an [`SKTileMapNode`](sktilemapnode.md). A texture object manages the texture data and graphics resources that are needed to render the image. Most texture objects are created from source images stored in your app bundle—your game’s artwork. Once created, a texture object’s contents are immutable. Multiple sprites can share the same texture object, sharing a single resource.

##### Deallocating a Texture

After a texture is loaded into the graphics hardware memory, it stays in memory until the referencing [`SKTexture`](sktexture.md) object is deleted. This means that between levels (or in a dynamic game), you may need to make sure a texture object is deleted. Delete a [`SKTexture`](sktexture.md) object by removing any strong references to it, including:

- All texture references from [`SKSpriteNode`](skspritenode.md) and [`SKEffectNode`](skeffectnode.md) objects in your game
- Any strong references to the texture in your own code
- An [`SKTextureAtlas`](sktextureatlas.md) object that was used to create the texture object

## Topics

### First Steps
- [Loading and Using Textures](loading-and-using-textures.md)
  Learn the basics about using textures in SpriteKit.
- [Texture Initializers](texture-initializers.md)
  See the various ways to create and use textures in SpriteKit.
### Reading a Texture’s Size and Optional Source Location
- [func size() -> CGSize](sktexture/size.md)
  Gets the size of the texture.
- [func textureRect() -> CGRect](sktexture/texturerect.md)
  Gets a rectangle that defines the portion of the texture used to render its image.
### Configuring a Texture’s Behavior for Scaling
- [var filteringMode: SKTextureFilteringMode](sktexture/filteringmode.md)
  The filtering mode used when the size of a sprite drawn with the texture is not drawn at the texture’s native size.
- [enum SKTextureFilteringMode](sktexturefilteringmode.md)
  Texture filtering modes to use when the texture is drawn in a size other than its native size.
- [var usesMipmaps: Bool](sktexture/usesmipmaps.md)
  A Boolean value that indicates whether the texture attempts to generate mipmaps.
### Getting a Texture’s Underlying Image
- [func cgImage() -> CGImage](sktexture/cgimage.md)
  Returns the texture’s image data as a Quartz 2D image.
### Preloading a Texture for Performance
- [Preloading Textures into Memory](preloading-textures-into-memory.md)
  Decompress images ahead of time to avoid performance issues during gameplay.
- [func preload(completionHandler: () -> Void)](sktexture/preload(completionhandler:).md)
  Load texture data into memory, calling a completion handler after the task completes.
- [class func preload([SKTexture], withCompletionHandler: () -> Void)](sktexture/preload(_:withcompletionhandler:).md)
  Load the data of multiple textures into memory.
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](sktexture/customplaygroundquicklook.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SKMutableTexture](skmutabletexture.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Maximizing Texture Performance](maximizing-texture-performance.md)
  Speed up image display and enable more images to be displayed at one time.
- [class SKTextureAtlas](sktextureatlas.md)
  A collection of textures optimized for storage and drawing performance.
- [class SKMutableTexture](skmutabletexture.md)
  A texture whose contents can be dynamically updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture)*