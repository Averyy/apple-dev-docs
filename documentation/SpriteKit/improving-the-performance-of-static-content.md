# Improving the Performance of Static Content

**Framework**: SpriteKit

Flatten a portion of your node hierarchy to a single texture to improve performance.

#### Overview

An effect node normally discards its private framebuffer after rendering is complete. Rendering the content is necessary because it typically changes every frame. However, if the content is static, discarding the rendered framebuffer is unnecessary, and it might make more sense to keep it.

If the content of the effect node is static, set the node’s `shouldRasterize` property to [`true`](https://developer.apple.com/documentation/Swift/true). Setting this property causes the following changes in behavior:

- The framebuffer is not discarded at the end of rasterization. This also means that more memory is being used by the effect node, and rendering may take slightly longer.
- When a new frame is rendered, the framebuffer is rendered only if the contents of the effect node’s descendants have changed.
- If the effect node has a Core Image filter, changes to its properties no longer automatically update the framebuffer. You can force it to be updated by setting the `shouldRasterize` property to [`false`](https://developer.apple.com/documentation/Swift/false).

You can use effect nodes to cache static content even when you aren’t applying a filter to the rendered image. This technique can be useful when the contents of a subtree are static and expensive to render.

## See Also

- [var shouldRasterize: Bool](skeffectnode/shouldrasterize.md)
  A Boolean value that indicates whether the results of rendering the child nodes should be cached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/improving-the-performance-of-static-content)*