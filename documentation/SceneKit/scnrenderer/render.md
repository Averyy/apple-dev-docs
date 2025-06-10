# render()

**Framework**: SceneKit  
**Kind**: method

Renders the scene’s contents in the renderer’s OpenGL context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func render()
```

#### Discussion

This method can be used only with an [`SCNRenderer`](scnrenderer.md) object created with the [`SCNRenderer`](scnrenderer.md) initializer. Call this method to tell SceneKit to draw the renderer’s scene into the OpenGL context you created the renderer with.

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the current system time, and then draws the scene.

## See Also

- [func render(atTime: CFTimeInterval)](scnrenderer/render(attime:).md)
  Renders the scene’s contents at the specified system time in the renderer’s OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/render())*