# preload(completionHandler:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Load texture data into memory, calling a completion handler after the task completes.

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

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func preload() async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

SpriteKit creates a background task to load the texture data from the associated file, then returns control to your game. After the texture data is loaded, your completion handler is called. Typically, you use this method when you want to guarantee that a particular texture is in memory before accessing it.

If you need to preload multiple textures at once, use the [`preload(_:withCompletionHandler:)`](./preload%28_,withcompletionhandler%29.md) method instead.

## Parameters

- `completionHandler`: A block called after the texture data is loaded.

## See Also

### Preloading a Texture for Performance
- [Preloading Textures into Memory](../preloading-textures-into-memory.md)
  Decompress images ahead of time to avoid performance issues during gameplay.
- [class func preload([SKTexture], withCompletionHandler: () -> Void)](./preload%28_,withcompletionhandler%29.md)
  Load the data of multiple textures into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/preload(completionhandler:))*