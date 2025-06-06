# preload(completionHandler:)

**Framework**: SpriteKit  
**Kind**: method

Loads an atlas object’s textures into memory, calling a completion handler after the task completes.

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
func preload() async
```

## Mentions

- [Maximizing Texture Performance](maximizing-texture-performance.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func preload() async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func preload() async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

SpriteKit creates a background task that loads the texture data from the atlas object. Then, SpriteKit returns control to your game. After the texture atlas is loaded, your completion handler is called.

If you need to preload multiple texture atlas objects immediately, use the [`preloadTextureAtlases(_:withCompletionHandler:)`](sktextureatlas/preloadtextureatlases(_:withcompletionhandler:).md) method instead.

## Parameters

- `completionHandler`: A block called after the texture atlas is loaded.

## See Also

- [class func preloadTextureAtlases([SKTextureAtlas], withCompletionHandler: () -> Void)](sktextureatlas/preloadtextureatlases(_:withcompletionhandler:).md)
  Loads the textures of multiple atlas objects into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlasesNamed([String], withCompletionHandler: ((any Error)?, [SKTextureAtlas]) -> Void)](sktextureatlas/preloadtextureatlasesnamed(_:withcompletionhandler:).md)
  Loads the textures of multiple atlases into memory, calling a completion handler after the task completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/preload(completionhandler:))*