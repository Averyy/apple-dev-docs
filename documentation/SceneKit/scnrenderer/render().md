# render()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Renders the scene’s contents in the renderer’s OpenGL context.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func render()
```

```objc
- (void) render;
```

#### Discussion

This method can be used only with an [`SCNRenderer`](../scnrenderer.md) object created with the [`SCNRenderer`](../scnrenderer.md) initializer. Call this method to tell SceneKit to draw the renderer’s scene into the OpenGL context you created the renderer with.

When you call this method, SceneKit updates its hierarchy of presentation nodes based on the current system time, and then draws the scene.

## See Also

### Rendering a Scene Using OpenGL
- [func render(atTime: CFTimeInterval)](./render%28attime%29.md)
  Renders the scene’s contents at the specified system time in the renderer’s OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnrenderer/render())*