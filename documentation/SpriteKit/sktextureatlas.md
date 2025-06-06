# SKTextureAtlas

**Framework**: SpriteKit  
**Kind**: class

A collection of textures optimized for storage and drawing performance.

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
class SKTextureAtlas
```

## Mentions

- [About Texture Atlases](about-texture-atlases.md)
- [Maximizing Texture Performance](maximizing-texture-performance.md)
- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)

#### Overview

An `SKTextureAtlas` is a collection of textures that were either created from an `.atlas` folder in the app bundle, or created at runtime. Texture atlases improve memory usage and rendering performance by reducing draw calls. Whenever you have textures that are always used together, store them in an atlas for best results.

SpriteKit implicitly loads an atlas when one of the atlas’s textures is accessed. Use [`textureNamed(_:)`](sktextureatlas/texturenamed(_:).md) when you want to explicitly access a texture atlas’s contents.

The preferred place to create a texture atlas is within an asset catalog (see [`Creating a Sprite Atlas`](about-texture-atlases#Creating-a-Sprite-Atlas.md)), but you can also put your source textures in an `.atlas` folder in the app bundle.

## Topics

### First Steps
- [About Texture Atlases](about-texture-atlases.md)
  Learn about the benefits of having a texture atlas, and the process for using it.
### Accessing Textures
- [func textureNamed(String) -> SKTexture](sktextureatlas/texturenamed(_:).md)
  Creates a texture from data stored in the texture atlas.
### Creating a Texture Atlas Programmatically
- [convenience init(named: String)](sktextureatlas/init(named:).md)
  Creates a texture atlas from data stored in the app bundle.
- [convenience init(dictionary: [String : Any])](sktextureatlas/init(dictionary:).md)
  Creates a texture atlas from a set of image files.
### Preloading Textures
- [func preload(completionHandler: () -> Void)](sktextureatlas/preload(completionhandler:).md)
  Loads an atlas object’s textures into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlases([SKTextureAtlas], withCompletionHandler: () -> Void)](sktextureatlas/preloadtextureatlases(_:withcompletionhandler:).md)
  Loads the textures of multiple atlas objects into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlasesNamed([String], withCompletionHandler: ((any Error)?, [SKTextureAtlas]) -> Void)](sktextureatlas/preloadtextureatlasesnamed(_:withcompletionhandler:).md)
  Loads the textures of multiple atlases into memory, calling a completion handler after the task completes.
### Reading Source Image Filenames
- [var textureNames: [String]](sktextureatlas/texturenames.md)
  The names of the texture images stored in the atlas.
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](sktextureatlas/customplaygroundquicklook.md)
  A custom playground quick look for this instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Maximizing Texture Performance](maximizing-texture-performance.md)
  Speed up image display and enable more images to be displayed at one time.
- [class SKTexture](sktexture.md)
  An image, decoded on the GPU, that can be used to render various SpriteKit objects.
- [class SKMutableTexture](skmutabletexture.md)
  A texture whose contents can be dynamically updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas)*