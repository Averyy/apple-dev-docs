# context

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The OpenGL rendering context that SceneKit uses for rendering the scene.

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
var context: UnsafeMutableRawPointer? { get }
```

```objc
@property (nonatomic, readonly, nullable) void * context;
```

## Discussion

In macOS, the value of this property is a Core OpenGL [`cglContextObj`](../../AppKit/nsopenglcontext/cglcontextobj.md) object.

In iOS, the value of this property is an [`EAGLContext`](../../OpenGLES/eaglcontext.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnscenerenderer/context)*