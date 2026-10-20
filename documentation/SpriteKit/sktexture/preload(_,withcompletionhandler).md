# preload(_:withCompletionHandler:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Load the data of multiple textures into memory.

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
class func preload(_ textures: [SKTexture], withCompletionHandler completionHandler: @escaping @Sendable () -> Void)
```

```swift
class func preload(_ textures: [SKTexture]) async
```

```objc
+ (void) preloadTextures:(NSArray<SKTexture *> *) textures withCompletionHandler:(void (^)()) completionHandler;
```

## Mentions

- [Maximizing Texture Performance](../maximizing-texture-performance.md)
- [Preloading Textures into Memory](../preloading-textures-into-memory.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func preload(_ textures: [SKTexture]) async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

SpriteKit creates a background task that loads the texture data for all of the textures in the array, then returns control to your game. Your completion handler is called after all of the textures are loaded.

## Parameters

- `textures`: An array of [`SKTexture`](../sktexture.md) objects.
- `completionHandler`: A block called after all of the textures are loaded.

## See Also

### Preloading a Texture for Performance
- [Preloading Textures into Memory](../preloading-textures-into-memory.md)
  Decompress images ahead of time to avoid performance issues during gameplay.
- [func preload(completionHandler: () -> Void)](./preload%28completionhandler%29.md)
  Load texture data into memory, calling a completion handler after the task completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/preload(_:withcompletionhandler:))*