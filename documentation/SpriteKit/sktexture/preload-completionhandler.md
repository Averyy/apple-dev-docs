# preload(completionHandler:)

**Framework**: SpriteKit  
**Kind**: method

Load texture data into memory, calling a completion handler after the task completes.

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

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func preload() async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func preload() async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

SpriteKit creates a background task to load the texture data from the associated file, then returns control to your game. After the texture data is loaded, your completion handler is called. Typically, you use this method when you want to guarantee that a particular texture is in memory before accessing it.

If you need to preload multiple textures at once, use the [`preload(_:withCompletionHandler:)`](sktexture/preload(_:withcompletionhandler:).md) method instead.

## Parameters

- `completionHandler`: A block called after the texture data is loaded.

## See Also

- [Preloading Textures into Memory](preloading-textures-into-memory.md)
  Decompress images ahead of time to avoid performance issues during gameplay.
- [class func preload([SKTexture], withCompletionHandler: () -> Void)](sktexture/preload(_:withcompletionhandler:).md)
  Load the data of multiple textures into memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/preload(completionhandler:))*