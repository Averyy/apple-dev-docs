# shouldRasterize

**Framework**: SpriteKit  
**Kind**: property

A Boolean value that indicates whether the results of rendering the child nodes should be cached.

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
@MainActor
var shouldRasterize: Bool { get set }
```

## Mentions

- [Creating a New Node By Rendering To a Texture](creating-a-new-node-by-rendering-to-a-texture.md)

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the effect node caches the filtered image for use in future frames. If the value is [`false`](https://developer.apple.com/documentation/swift/false), then SpriteKit discards the rendered image and redraws it from scratch the next time the node is rendered. The default value is [`false`](https://developer.apple.com/documentation/swift/false). Caching the rendered image uses more memory and may take more time to render. However, if the effect node’s descendants rarely change, caching can improve performance.

When caching is enabled, changes to the effect node’s children trigger updates to the cached image in the next frame of animation. However, changing the filter’s properties does not.

## See Also

- [Improving the Performance of Static Content](improving-the-performance-of-static-content.md)
  Flatten a portion of your node hierarchy to a single texture to improve performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skeffectnode/shouldrasterize)*