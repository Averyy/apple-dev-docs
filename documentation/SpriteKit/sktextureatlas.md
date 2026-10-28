# SKTextureAtlas

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

A collection of textures optimized for storage and drawing performance.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class SKTextureAtlas
```

```objc
@interface SKTextureAtlas : NSObject
```

## Mentions

- [About Texture Atlases](./about-texture-atlases.md)
- [Maximizing Node Drawing Performance](./maximizing-node-drawing-performance.md)
- [Maximizing Texture Performance](./maximizing-texture-performance.md)

## Overview

An `SKTextureAtlas` is a collection of textures that were either created from an `.atlas` folder in the app bundle, or created at runtime. Texture atlases improve memory usage and rendering performance by reducing draw calls. Whenever you have textures that are always used together, store them in an atlas for best results.

SpriteKit implicitly loads an atlas when one of the atlas’s textures is accessed. Use [`textureNamed(_:)`](./sktextureatlas/texturenamed%28_%29.md) when you want to explicitly access a texture atlas’s contents.

The preferred place to create a texture atlas is within an asset catalog (see [Creating a Sprite Atlas](./about-texture-atlases.md#Creating-a-Sprite-Atlas)), but you can also put your source textures in an `.atlas` folder in the app bundle.

## Topics

### First Steps
- [About Texture Atlases](./about-texture-atlases.md)
  Learn about the benefits of having a texture atlas, and the process for using it.
### Accessing Textures
- [func textureNamed(String) -> SKTexture](./sktextureatlas/texturenamed%28_%29.md)
  Creates a texture from data stored in the texture atlas.
### Creating a Texture Atlas Programmatically
- [convenience init(named: String)](./sktextureatlas/init%28named%29.md)
  Creates a texture atlas from data stored in the app bundle.
- [convenience init(dictionary: [String : Any])](./sktextureatlas/init%28dictionary%29.md)
  Creates a texture atlas from a set of image files.
### Preloading Textures
- [func preload(completionHandler: () -> Void)](./sktextureatlas/preload%28completionhandler%29.md)
  Loads an atlas object’s textures into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlases([SKTextureAtlas], withCompletionHandler: () -> Void)](./sktextureatlas/preloadtextureatlases%28_,withcompletionhandler%29.md)
  Loads the textures of multiple atlas objects into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlasesNamed([String], withCompletionHandler: ((any Error)?, [SKTextureAtlas]) -> Void)](./sktextureatlas/preloadtextureatlasesnamed%28_,withcompletionhandler%29.md)
  Loads the textures of multiple atlases into memory, calling a completion handler after the task completes.
### Reading Source Image Filenames
- [var textureNames: [String]](./sktextureatlas/texturenames.md)
  The names of the texture images stored in the atlas.
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](./sktextureatlas/customplaygroundquicklook.md)
  A custom playground quick look for this instance.
### Initializers
- [init?(coder: NSCoder)](./sktextureatlas/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Textures
- [Maximizing Texture Performance](./maximizing-texture-performance.md)
  Speed up image display and enable more images to be displayed at one time.
- [class SKTexture](./sktexture.md)
  An image, decoded on the GPU, that can be used to render various SpriteKit objects.
- [class SKMutableTexture](./skmutabletexture.md)
  A texture whose contents can be dynamically updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas)*