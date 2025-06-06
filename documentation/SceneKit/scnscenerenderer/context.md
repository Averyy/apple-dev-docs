# context

**Framework**: SceneKit  
**Kind**: property  
**Required**: Yes

The OpenGL rendering context that SceneKit uses for rendering the scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- macOS ?+
- tvOS ?+

## Declaration

```swift
var context: UnsafeMutableRawPointer? { get }
```

#### Discussion

In macOS, the value of this property is a Core OpenGL [`cglContextObj`](https://developer.apple.com/documentation/AppKit/NSOpenGLContext/cglContextObj) object.

In iOS, the value of this property is an [`EAGLContext`](https://developer.apple.com/documentation/OpenGLES/EAGLContext) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/context)*