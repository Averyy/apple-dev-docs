# preload(completionHandler:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Loads an atlas object’s textures into memory, calling a completion handler after the task completes.

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
func preload(completionHandler: @escaping @Sendable () -> Void)
```

```swift
func preload() async
```

```objc
- (void) preloadWithCompletionHandler:(void (^)()) completionHandler;
```

## Mentions

- [Maximizing Texture Performance](../maximizing-texture-performance.md)

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func preload() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

SpriteKit creates a background task that loads the texture data from the atlas object. Then, SpriteKit returns control to your game. After the texture atlas is loaded, your completion handler is called.

If you need to preload multiple texture atlas objects immediately, use the [`preloadTextureAtlases(_:withCompletionHandler:)`](./preloadtextureatlases%28_,withcompletionhandler%29.md) method instead.

## Parameters

- `completionHandler`: A block called after the texture atlas is loaded.

## See Also

### Preloading Textures
- [class func preloadTextureAtlases([SKTextureAtlas], withCompletionHandler: () -> Void)](./preloadtextureatlases%28_,withcompletionhandler%29.md)
  Loads the textures of multiple atlas objects into memory, calling a completion handler after the task completes.
- [class func preloadTextureAtlasesNamed([String], withCompletionHandler: ((any Error)?, [SKTextureAtlas]) -> Void)](./preloadtextureatlasesnamed%28_,withcompletionhandler%29.md)
  Loads the textures of multiple atlases into memory, calling a completion handler after the task completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/preload(completionhandler:))*