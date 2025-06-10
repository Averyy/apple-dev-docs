# preloadTextureAtlases(_:withCompletionHandler:)

**Framework**: SpriteKit  
**Kind**: method

Loads the textures of multiple atlas objects into memory, calling a completion handler after the task completes.

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
class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas]) async
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func preloadTextureAtlases(_ textureAtlases: [SKTextureAtlas]) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

SpriteKit creates a background task that loads the texture data from all of the specified atlas objects. Then, SpriteKit returns control to your game. After the atlas objects are loaded, your completion handler is called.

## Parameters

- `textureAtlases`: An array of   objects.
- `completionHandler`: A block called after all of the texture atlases are loaded.

## See Also

- [func preload(completionHandler: () -> Void)](sktextureatlas/preload(completionhandler:).md)
  Loads an atlas object’s textures into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlasesNamed([String], withCompletionHandler: ((any Error)?, [SKTextureAtlas]) -> Void)](sktextureatlas/preloadtextureatlasesnamed(_:withcompletionhandler:).md)
  Loads the textures of multiple atlases into memory, calling a completion handler after the task completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/preloadtextureatlases(_:withcompletionhandler:))*